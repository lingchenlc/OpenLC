#!/bin/bash
#
# OpenClaw Queue Monitor
# 监控 delivery-queue 积压，发现积压时执行健康检查或重启服务
#

set -euo pipefail

QUEUE_DIR="$HOME/.openclaw/delivery-queue"
QUEUE_THRESHOLD=${QUEUE_THRESHOLD:-3}
LOG_FILE="$HOME/.openclaw/logs/queue-monitor.log"
MAX_LOG_SIZE=5242880

NOTIFY_CHANNEL="${OPENCLAW_NOTIFY_CHANNEL:-telegram}"
NOTIFY_TARGET="${OPENCLAW_NOTIFY_TARGET}"

CLASH_API="${CLASH_API:-http://127.0.0.1:9097}"
CLASH_SECRET="${CLASH_SECRET:-}"

mkdir -p "$(dirname "$LOG_FILE")"

log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    if [[ -f "$LOG_FILE" ]]; then
        local size=$(stat -c%s "$LOG_FILE" 2>/dev/null || stat -f%z "$LOG_FILE" 2>/dev/null || echo 0)
        if [[ $size -gt $MAX_LOG_SIZE ]]; then
            mv "$LOG_FILE" "${LOG_FILE}.$(date +%Y%m%d-%H%M%S).old"
        fi
    fi

    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
}

notify_boss() {
    local message="$1"
    if [[ -z "$NOTIFY_TARGET" ]]; then return; fi
    openclaw message send \
        --channel "$NOTIFY_CHANNEL" \
        --target "$NOTIFY_TARGET" \
        --message "$message" \
        > /dev/null 2>&1 || log "WARN" "Notification failed"
}

check_queue_backlog() {
    if [[ ! -d "$QUEUE_DIR" ]]; then
        log "ERROR" "Queue directory not found: $QUEUE_DIR"
        echo "0"
        return 0
    fi
    local count=$(find "$QUEUE_DIR" -maxdepth 1 -name "*.json" 2>/dev/null | wc -l | tr -d ' ')
    echo "$count"
}

restart_gateway() {
    log "INFO" "Self-healing: Restarting gateway due to queue backlog..."
    openclaw gateway restart > /dev/null 2>&1
    sleep 5
}

main() {
    local backlog=$(check_queue_backlog)
    
    if [[ "$backlog" -le "$QUEUE_THRESHOLD" ]]; then
        log "INFO" "Queue normal: $backlog items"
        exit 0
    fi
    
    log "WARN" "Queue backlog detected: $backlog items (Threshold: $QUEUE_THRESHOLD)"
    
    # Simple self-healing logic: if queue is backlogged, it might be due to a frozen gateway or network issue.
    # In a full clash setup, it would switch proxies.
    # Here we restart the gateway as a fallback self-healing step if Clash is not used or proxy switch is skipped.
    
    if curl -s -m 2 -H "Authorization: Bearer $CLASH_SECRET" "$CLASH_API/version" >/dev/null; then
        log "INFO" "Clash API available, but advanced proxy switching is omitted for brevity. You can integrate find_healthy_proxy_in_region here."
    else
        log "WARN" "Network proxy API unavailable. Falling back to Gateway restart."
    fi
    
    restart_gateway
    
    # Check again
    local new_backlog=$(check_queue_backlog)
    if [[ "$new_backlog" -gt "$QUEUE_THRESHOLD" ]]; then
        notify_boss "🚨 Queue Monitor: Queue backlog persists after restart ($new_backlog items). Please check manually."
    else
        notify_boss "✅ Queue Monitor: Gateway restarted and queue processing resumed."
    fi
}

main

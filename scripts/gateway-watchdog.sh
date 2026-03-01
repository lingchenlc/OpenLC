#!/bin/bash
#
# OpenClaw Gateway Watchdog
# Automatically monitors and restarts the Gateway service if it crashes.
#

CHECK_INTERVAL=${CHECK_INTERVAL:-60}
HEALTH_URL="${OPENCLAW_HEALTH_URL:-http://127.0.0.1:18789/healthz}"
LOCK_FILE="/tmp/openclaw-restart.lock"
LOG_FILE="$HOME/.openclaw/logs/watchdog.log"
MAX_LOG_SIZE=1048576
MAX_RETRY=${MAX_RETRY:-3}

NOTIFY_CHANNEL="${OPENCLAW_NOTIFY_CHANNEL:-telegram}"
NOTIFY_TARGET="${OPENCLAW_NOTIFY_TARGET}"

mkdir -p "$(dirname "$LOG_FILE")"

log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    if [[ -f "$LOG_FILE" ]] && [[ $(stat -c%s "$LOG_FILE" 2>/dev/null || stat -f%z "$LOG_FILE" 2>/dev/null) -gt $MAX_LOG_SIZE ]]; then
        mv "$LOG_FILE" "${LOG_FILE}.old"
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
        > /dev/null 2>&1
}

check_health() {
    curl -s -m 5 "$HEALTH_URL" > /dev/null 2>&1
    return $?
}

check_lock() {
    if [[ -f "$LOCK_FILE" ]]; then
        local lock_age=$(( $(date +%s) - $(stat -c%Y "$LOCK_FILE" 2>/dev/null || stat -f%m "$LOCK_FILE" 2>/dev/null) ))
        if [[ $lock_age -gt 300 ]]; then
            log "WARN" "Lock file stale (${lock_age}s), removing"
            rm -f "$LOCK_FILE"
            return 1
        fi
        return 0
    fi
    return 1
}

restart_gateway() {
    log "INFO" "Attempting to restart gateway..."
    touch "$LOCK_FILE"
    
    openclaw gateway restart > /dev/null 2>&1
    local result=$?
    
    sleep 5
    rm -f "$LOCK_FILE"
    
    return $result
}

main() {
    log "INFO" "Watchdog started (interval: ${CHECK_INTERVAL}s)"
    
    local consecutive_failures=0
    
    while true; do
        sleep "$CHECK_INTERVAL"
        
        if check_lock; then continue; fi
        
        if check_health; then
            consecutive_failures=0
        else
            consecutive_failures=$((consecutive_failures + 1))
            log "WARN" "Gateway unreachable (attempt $consecutive_failures/$MAX_RETRY)"
            
            if [[ $consecutive_failures -ge $MAX_RETRY ]]; then
                log "ERROR" "Gateway failed $MAX_RETRY consecutive checks, attempting restart..."
                
                if restart_gateway && check_health; then
                    log "OK" "Gateway restart successful"
                    notify_boss "✅ OpenClaw Watchdog: Gateway 自动重启成功 (Self-healed)"
                    consecutive_failures=0
                else
                    log "ERROR" "Gateway restart FAILED"
                    notify_boss "🚨 OpenClaw Watchdog: Gateway 重启失败！需要人工干预。"
                    consecutive_failures=0
                    sleep 300
                fi
            fi
        fi
    done
}

main

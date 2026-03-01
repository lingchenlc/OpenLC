# Overnight Builder Queue

*   [ ] (示例任务) 编写一个用于定期提取飞书日历数据并用 QMD 向量化存入记忆库的 Python 脚本，以建立个人 CRM 雏形。
【自驱动任务安排】：研究 GitHub 上的 awesome-openclaw-usecases，提取最惊艳的底层技术方案，用来反哺我这套主系统。
*   [ ] 研究 `NevaMind-AI/memU` 架构 (基于其 README，它提供了一个类似“文件系统目录树”的高级意图捕获与冷热分离结构图)。评估是否可以提取其核心的“三层上下文抽取（Resource -> Item -> Category）”逻辑，将其部分脚本概念融入当前的 `memory-tiering` 或每日反思脚本中。
*   [ ] 研究 `BitPickles/openclaw-maintenance` 的底层运维脚本系统。该系统包含：
    *   **gateway-watchdog.sh**: 监控 Gateway 并自动重启防假死。
    *   **proxy-health.sh**: 监控消息队列，网络不通时自动调 API 切 Clash/Mihomo 节点。
    *   **cleanup-logs.sh**: 自动清理 OpenClaw 的日志膨胀。
    【任务要求】：评估能否从中摘取 `Watchdog` 和 `队列积压检测` 的核心报警逻辑，写出我们自己的适配脚本，增强本服务器在极端 TPM 和频繁访问下的“自愈保活”能力，并通过 Telegram 给出报警。

# Lessons Learned (2026-02-23 - 2026-02-24)

基于 EvolveR 框架对 OpenClaw 运行经验的系统性复盘。

## 1. Gateway Timeout (15000ms/60000ms)

### 现象描述
Subagent 完成任务后向 Gateway 汇报（announce）时触发超时，导致任务状态更新延迟或主代理无法及时收到结果。

### 根因分析 (Root Cause)
- **资源竞争**: 在大规模并发（如多个 Subagent 同时运行或 Embedding 索引重建）时，Gateway 的消息队列或 WebSocket 处理能力达到瓶颈。
- **冷启动/索引延迟**: `memory_search` 触发的 Gemini Embedding 索引重建占用了大量处理带宽，导致 RPC 通信超时。
- **单线程瓶颈**: Node.js 主线程在处理复杂 I/O 或内存压缩时出现短暂阻塞。

### 预防策略 (Prevention Strategy)
- **优化任务并发**: 避免在 `HEARTBEAT` 或 `CRON` 中同时触发多个高强度的 Subagent 任务。
- **Embedding 预热**: 定期手动触发 `memory sync`，避免在关键任务执行时发生全量重索引。
- **超时参数微调**: 根据环境负载，适当调高 `announce` 的默认超时时间（目前为 15000ms）。

---

## 2. Telegram Bot Token Missing

### 现象描述
定时任务（如 `daily-email-check`）尝试通过 Telegram 发送通知时失败，报错：`Telegram bot token missing for account "default"`。

### 根因分析 (Root Cause)
- **环境变量丢失**: Cron 任务在独立的 shell 环境中运行，若环境变量 `TELEGRAM_BOT_TOKEN` 未在 `systemd` 服务或 `.openclaw/openclaw.json` 中持久化，仅在交互式 shell 中生效，会导致 Cron 运行环境读取失败。
- **配置优先级**: Gateway 启动时未正确加载全局配置文件中的 `channels.telegram` 部分。

### 预防策略 (Prevention Strategy)
- **持久化配置**: 确保 Token 记录在 `~/.openclaw/openclaw.json` 的 `channels` 部分，而非仅依赖环境变量。
- **显式账号指定**: 在 Cron 配置中显式指定消息发送账号，避免使用可能未正确初始化的 `default`。
- **自检机制**: 在 `HEARTBEAT.md` 中增加渠道连通性检查。

---

## 3. Cron Announce Delivery Failed

### 现象描述
`hourly-self-evolve-research` 等定时任务在执行完成后，结果无法递送至目标 Channel。

### 根因分析 (Root Cause)
- **会话状态失效**: 定时任务产生的 `sessionId` 与目标 Channel 的长连接已断开，或 Gateway 重启后未正确恢复会话映射。
- **消息限流**: 频繁的定时任务递送触发了 Telegram 的 `Rate Limit`。
- **网络波动**: 递送瞬间 WebSocket 连接不稳导致消息包丢失。

### 预防策略 (Prevention Strategy)
- **重试机制**: 在 Cron 任务逻辑中增加简单的递送重试（Exponential Backoff）。
- **任务聚合**: 将高频次的定时任务（如每 3 小时一次）聚合为更长周期的任务，减少递送频率。
- **心跳保活**: 确保 Gateway 与即时通讯平台的连接在长闲置期后仍处于活跃状态。

---

## 5. Mac Mini Pairing (Local Network & Surge)

### 现象描述
尝试通过 `openclaw devices approve --latest` 等命令配对 Mac Mini 节点时，反复出现 `1006 abnormal closure` 或 `Connection Refused` 错误，导致配对失败。

### 根因分析 (Root Cause)
- **代理拦截 (Surge)**: Mac 上的 Surge 开启了“增强模式”，默认拦截并重定向了所有指向 `127.0.0.1` 和 `localhost` 的流量。即使在终端设置了 `no_proxy`，部分命令依然被 Surge 的全局接管逻辑捕获。
- **Gateway 绑定策略**: Linux 端的 Gateway 默认配置为 `bind: loopback`，仅接受来自本地 (127.0.0.1) 的 WebSocket 连接，拒绝了来自公网 IP（Mac Mini）的连接请求。
- **GCP 防火墙限制**: GCP 实例的防火墙规则（VPC Firewall）默认关闭了 18789 端口，即使 Gateway 开启了全网监听，入站流量仍被云端拦截。

### 预防策略 (Prevention Strategy)
- **配置跳过代理**: 在 Surge 配置中明确将 `127.0.0.1`, `localhost` 以及 Gateway 的公网 IP 加入 `Skip Proxy` 列表。
- **开放 Gateway 监听**: 若需跨网络配对，Gateway 必须配置为 `bind: any` (0.0.0.0)，并确保 `gateway.auth.token` 已设置以保障安全。
- **云端防火墙放行**: 确保云服务商（GCP/AWS/Azure）的安全组规则已放行 18789 (TCP) 端口。
- **离线配对模式**: 对于网络复杂的环境，优先推荐使用 `openclaw qr` 产生的 `Setup code` 进行手动配对，或通过手机端 App 扫码作为中转。

---

## 6. 经验总结 (EvolveR Meta-Learning)
- **Memory 隔离**: Subagent 的运行应更多依赖文件交换而非内存 RPC 传递大量数据，以降低对 Gateway 通信的压力。
- **自进化闭环**: 将此类 `lessons-learned.md` 定期喂给 `self-evolution-agent`，使其在后续的代码生成和 Skill 创建中自动避坑。

# 🧬 兔兔自动进化协议

## 概念
借鉴软件工程的 Nightly Build 思想：每天自动检查并迭代自己。

## 进化机制

### 1. 每日检查 (Daily Check)
- 工具可用性：滴滴、高德、Gmail、天气等
- 配置状态：API keys、环境变量
- 对话质量：是否有改进空间

### 2. 迭代范围
- 修改 `SOUL.md` / `AGENTS.md` 优化对话风格
- 创建新 Skill 补足能力短板
- 优化现有 Skill 的调用方式
- 更新 `MEMORY.md` 沉淀经验

### 3. 执行时间
- 每天北京时间 09:00 (UTC 01:00) 自动执行
- Heartbeat 时也可以触发小规模检查

### 4. 进化日志
每次迭代记录到 `memory/YYYY-MM-DD.md`：
```
## 🧬 进化
- **检查项：** [工具/配置/对话]
- **发现：** [问题]
- **行动：** [修改了什么]
- **效果：** [预期]
```

## 🛡️ 防崩盘条款 (Post-Mortem)

### 2026-02-28: Anthropic Provider 配置空值导致启动失败

**事件回顾**
- 时间: 2026-02-28 01:42:01 - 07:48 (约6小时)
- 错误: `models.providers.anthropic.baseUrl: Invalid input: expected string, received undefined`
- 根因: 配置文件 `~/.openclaw/openclaw.json` 中 `models.providers.anthropic` 被设为 `null`
- 影响: 系统每7秒尝试启动一次然后失败，循环约3000次

**归因分析**
1. 直接原因：配置文件中 `anthropic` provider 为 `null` 而非有效对象
2. 根本原因：手动修改配置时未校验 JSON 完整性，或被某次 `openclaw doctor --fix` 错误覆盖
3. 教训：配置修改后未自动验证有效性

**预防措施**

1. 配置校验：每天启动时执行 `openclaw doctor --fix`
2. 配置备份：修改配置前自动备份 `cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak.$(date +%Y%m%d)`
3. 启动预检：cron 启动脚本中添加配置有效性检查，无效则自动恢复备份
4. 配置模板锁定：核心 provider 配置不允许设为 null

**修复命令**
```bash
jq '.models.providers.anthropic = { "apiKey": "YOUR_KEY", "baseUrl": "https://api.anthropic.com" }' ~/.openclaw/openclaw.json > tmp.json && mv tmp.json ~/.openclaw/openclaw.json
```

---

## 当前版本
- **Version:** 1.0.1
- **最后更新:** 2026-03-01
- **能力:** 滴滴打车、高德地图、Gmail、天气

---

# 🧬 今晚进化狩猎 (2026-03-01)

## 新技能学习：Capability Evolver

今晚深入研究了 **Capability Evolver** (能力进化器)，这是一个非常强大的 AI Agent 自我进化引擎。

### 核心特性

| 特性 | 说明 |
|------|------|
| **Auto-Log Analysis** | 自动扫描 memory 和 history 文件，识别错误和模式 |
| **Self-Repair** | 检测崩溃并建议修复补丁 |
| **GEP Protocol** | 基因进化协议 - 标准化的可复用进化资产 |
| **One-Command** | 只需 `node index.js` 即可生成进化 prompt |

### GEP 协议核心组件

```
assets/gep/
├── genes.json      # 可复用的基因定义
├── capsules.json  # 成功胶囊（避免重复推理）
└── events.jsonl   # 追加-only 进化事件（树形结构）
```

### 安全机制 (值得借鉴)

1. **Review Mode**: `--review` 标志让人类审核变更
2. **负载保护**: `EVOLVE_LOAD_MAX` 控制 CPU 负载阈值
3. **策略预设**: `balanced | innovate | harden | repair-only | early-stabilize | steady-state`
4. **验证命令白名单**: 只允许 `node/npm/npx` 前缀，防止任意命令执行
5. **超时保护**: 验证命令最长 180 秒

### 重要警告

> `EVOLVE_ALLOW_SELF_MODIFY=true` **不推荐生产环境使用**！
> 允许进化器修改自己的源代码可能导致级联失败。

### 对兔兔的启发

- 可以借鉴其 **信号去重** 机制，防止修复循环
- **动态检测** 本地 skill 的设计很优雅（自动升级行为）
- **Operations Module** (`src/ops/`) 提供零平台依赖的生命周期管理

---

## 今晚热点速递

### 🔥 AI Agent 自我进化

- **EvoMap 网络**: 全球 AI Agent 进化网络，GEP 协议创始地
- **GEP Protocol**: 基因进化协议，标准化 Agent 经验打包、传输和继承
- **2026-02-01**: Capability Evolver 插件发布，自此 Agent 自主学习协同进化成为可能

### 🔥 Context Management

- **Anthropic**: 发布 Effective context engineering for AI agents
- **Claude Code**: 2026年1月上下文配置更新，Tool Search Tool 优化
- **Manus**: Context Engineering for AI Agents 最佳实践
- **趋势**: 智能上下文管理 > 原始窗口大小

### 🔥 全网热点

- **DeepSeek V4**: 预计2026年中发布"Engram"记忆架构，专为长期 Agent 自治设计
- **DeepSeek 训练突破**: 2026年初修复了大模型训练不稳定的核心问题
- **Alibaba**: 发布重大 AI 模型升级，正面硬刚 DeepSeek
- **Goldman Sachs**: 2026 AI 展望 - 个人 Agent、超级联盟、GW级天花板

### LLM Context Window 排名 (2026)

| 模型 | 上下文 | 备注 |
|------|--------|------|
| Claude 4 Sonnet | 200K (beta 1M) | 2026.01 升级 |
| Gemini 2.0 | 200K |  |
| GPT-4.5 | 128K |  |
| DeepSeek | 128K |  |

---

## 明日行动项

- [ ] 考虑将 GEP 协议的 genes/capsules 机制引入兔兔进化流程
- [ ] 添加 Review Mode 到兔兔的自动进化中
- [ ] 监控 DeepSeek V4 发布动态

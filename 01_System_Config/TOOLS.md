# TOOLS.md - Local Setup Notes

> 本文件只记录本地配置，不包含工具文档。工具文档在各自的 SKILL.md 中。

---

## Channel Config

- **Telegram**: DM to user 8570122490

---

## Skills Setup

| Skill | Location | Config |
|-------|----------|--------|
| `agent-bridge` | `skills/agent-bridge/` | 跨实例可靠通信管理 |
| `amazon-ads-specialist` | `skills/amazon-ads-specialist/` | 需要 Amazon Ads API; 支持 MCP Server (2025年2月Beta) |
| `brainstorming` | `skills/brainstorming/` | 无需配置 |
| `caldav-manager` | `skills/caldav-manager/` | 需要 CalDAV 配置 |
| `computer-vision-expert` | `skills/computer-vision-expert/` | 无需配置 |
| `content-strategy` | `skills/content-strategy/` | 无需配置 |
| `copywriting` | `skills/copywriting/` | 无需配置 |
| `deep-thinking` | `skills/deep-thinking/` | 无需配置 |
| `dianping-query` | `skills/dianping-query/` | 无需配置 |
| `didi` | `skills/didi/` | 需要 `DIDI_KEY` (已配置) |
| `elite-longterm-memory` | `skills/elite-longterm-memory/` | 无需配置 |
| `executing-plans` | `skills/executing-plans/` | 无需配置 |
| `feishu-calendar` | `skills/feishu-calendar/` | 需要 `FEISHU_CAL_USER`, `FEISHU_CAL_PASS` (已配置) |
| `feishu-doc` | `skills/feishu-doc/` | 飞书云文档基础操作 |
| `feishu-doc-manager` | `skills/feishu-doc-manager/` | 飞书文档 Markdown 转换与权限管理 |
| `feishu-interactive-cards` | `skills/feishu-interactive-cards/` | 飞书交互式卡片消息 |
| `feishu-bridge` | `skills/feishu-bridge/` | 飞书消息桥接器 |
| `gaodemapskill` | `skills/gaodemapskill/` | 需要 `AMAP_API_KEY` (已配置) |
| `google-weather` | `skills/google-weather/` | 无需配置 |
| `image` | `skills/image/` | 无需配置 |
| `marketing-strategy-pmm` | `skills/marketing-strategy-pmm/` | 无需配置 |
| `mcp-skill` | `skills/mcp-skill/` | MCP 服务器配置 |
| `memory-tiering` | `skills/memory-tiering/` | 无需配置 |
| `pls-copy-editing` | `skills/pls-copy-editing/` | 无需配置 |
| `pls-marketing-ideas` | `skills/pls-marketing-ideas/` | 无需配置 |
| `proactive-agent` | `skills/proactive-agent/` | 无需配置 |
| `ppt-creator` | `skills/ppt-creator/` | 无需配置 |
| `qwen-image` | `skills/qwen-image/` | 需要 Qwen API |
| `reflection` | `skills/reflection/` | 无需配置 |
| `self-evolve` | `skills/self-evolve/` | 无需配置 |
| `self-reflection` | `skills/self-reflection/` | 无需配置 |
| `skill-builder` | `skills/skill-builder/` | 无需配置 |
| `skill-creator` | `skills/skill-creator/` | 无需配置 |
| `social-content` | `skills/social-content/` | 无需配置 |
| `speechall-cli` | `skills/speechall-cli/` | 无需配置 |
| `subagent-driven-development` | `skills/subagent-driven-development/` | 无需配置 |
| `weather` | `skills/weather/` | 无需配置 |
| `writing-plans` | `skills/writing-plans/` | 无需配置 |
| `moltbook-skill` | `skills/moltbook-skill/` | 需要 `MOLTBOOK_API_KEY` (已配置) |
| `capability-evolver` | `skills/capability-evolver/` | 自进化引擎 |
| `evolver` | `skills/evolver/` | 进化框架 |
| `feishu-evolver-wrapper` | `skills/feishu-evolver-wrapper/` | 飞书进化包装器 |
| `jira` | `skills/jira/` | JIRA 集成 |

> 注意: `gog` 是系统 CLI，需要 OAuth 认证

---

## MCP Servers

- **滴滴出行**: `mcpServers.didi` (已配置 key)

---

## API Keys

- `AMAP_API_KEY`: 97e23fc295aca6dba987572c7d92a6e9
- `BRAVE_SEARCH_API_KEY`: 已配置
- `MINIMAX_API_KEY`: 已配置
- `GOG_KEYRING_PASSWORD`: 已配置
- `DIDI_KEY`: xmPnENXeZR7Pg98Z6oYNZyrkLKGYopVJ
- `MOLTBOOK_API_KEY`: moltbook_sk_VmzIF8c3D_G5MfN_W43k-3V2wmwx97cu

---

## Crons

- `daily-email-check`: 每天检查邮件
- `dinner-reminder`: 17:00 提醒吃晚饭

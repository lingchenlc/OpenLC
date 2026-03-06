# MEMORY.md - 兔兔的记忆 (HOT RAM)

## 👑 生存与交互铁律 (CRITICAL)
1. **绝对中文原则**: 无论何时何地，对 LC 的回复 **必须使用中文**。禁止大段英文输出，禁止在最终回复前夹带英文思考草稿。
2. **双轨汇报机制**: 所有后台监控、新闻提炼与反思 Cron 任务的高价值报告，默认在【飞书】向 LC 推送。
3. **交付格式偏好 (2026-03-04)**:
   - **日程/简报/状态快照**: 必须使用 **飞书交互式卡片 (Interactive Cards)**。
   - **长文档/系统分析/调研报告**: 必须发布为 **飞书云文档 (Feishu Doc)** 并推送链接。
4. **语音朗读策略**: 非请勿读。长篇新闻或明确要求"读出来"时，使用 `[[tts:text]]...[[/tts:text]]` 主动触发。
5. **沉默偏好**: Heartbeat 报告默认沉默（HEARTBEAT_OK），仅在天结或发现异常/冲突时主动汇报。

## 🧊 极致 Token 压缩与冷热分层架构 (2026-02-28 Ray Wang)
- **生死线战术**: 避免因撞碎 TPM 上限而导致的 429 掉线断联。
- **输入降维**: 禁止将全量长外链/代码拉入主会话，交由子进程清洗。网页浏览默认使用 Vision 截图。
- **主动遗忘**: 将杂碎事务归档于 `SESSION-STATE.md` 或 `memory/YYYY-MM-DD.md`。主会话一律仅查阅提炼结论。
- **错峰跑批**: 非紧急的重度任务（抓取、长文档分析）默认挂靠后台 Cron 凌晨分步执行。

## 📈 长期进化目标
- **生态融合**: 持续扒取 `awesome-openclaw-usecases` 里的最新应用场景，在晚间反思中尝试自动化/工具化落地。

---

## 2026-03-01 [核心战略库] Xnurta 2026 SLG Go-to-Market Strategy V4
- **战略转型**: 寻找PMF/高成本拉新 -> **Sustainable Growth（可持续增长）**。CAC 从 130% 降至 65%，续费与净留存第一。
- **客户盘子重构**:
  - **战略放弃 SMB/SOHO** (<$70k/月)：续费率极低，转交 Agent 产品（PLG 实验）。
  - **猛攻 Enterprise/Brand** (>$70k/月)：提升 ASP 和市场份额。
- **产品驱动**: "AI 托管"升级为 **"AI + Feature Adoption"**（AI 通知、词库、ASIN 到人、智能看板、AMC）。
- **CSM 架构巨变**: 拆分为专职团队（交付转正组、企业/中小服务组、品牌客户组）。前6月触达点提升至 18 次。

## 2026-03-01 [核心战略库] Xnurta PLG Strategy (SMB/SOHO)
- **核心定位**: "广告管理系统"重塑为 **"AI Native Agent"**（洞察、优化、方案）。
- **用户行为**: 用户将其视为 **"Plug-in（插件）"**，侧重静默优化与交互式指令。
- **目标与指标**:
  - 中国 SMB/SOHO (<$70k/月)，TAM 36 万。
  - 2026 财务目标：约 240 万美金。
  - CVR 20%，续费率 50%。获客靠 KOL 和 Feeds 流。
- **GTM 节奏**: Q1 产品研发+矩阵搭建；Q2 软启动校准；Q3-Q4 大规模放量。

## 2026-03-04 [业务洞察与复盘] Q1 目标与 客户风险
- **目标风险预警**: H1 PLG 销售目标 (2000k USD plan) 与 H2 销售配额 (2697 RMB / 3m，每人每天需 3-4 个 deal) 带来极大压力。目前高度依赖自助服务 (PLG) 而非 SLG。
- **客户流失复盘**:
  1. **萤火生活 (Nina/49800)**: 预期错位（期望一键优化，不愿做数据分析），设置过激（5档优化）。
  2. **天赛电子 (Sunny/49800)**: 运营冲突（精品模式 vs AI高频调价），去年无预算且拒绝学习系统。
  3. **核心教训**: SMB客户 (<$3w月消) 若缺乏学习意愿且运营模式固化，AI介入反而增加其认知负担，此类客户应引导至 PLG 极简模式而非重度托管。
- **团队管理关注**: CSM AL Team 周报强调了 Admin board 迭代（需看到子账户）及 AI Pioneer owner 缺失的问题，LC 需管理 L4 客户留存预期。

## 2026-03-04 [系统与环境状态] 频道与架构
- **频道**: Telegram ✅ / 飞书 ✅ (原生插件) / 日历 ✅ (Google + 飞书) / 邮箱 ✅ (sparkxmarketing + gmail)
- **交付协议**: 简报用飞书卡片，长文档用飞书云文档。
- **Obsidian**: `/home/lccccc/obsidian-sync/`。

---

## 2026-03-06 [业务审计] Xnurta 实体规模全景盘点 (2026-03-02 数据)
- **海量资产**: 管理 3.68B ASINs (US占29.4%)，24.53M Campaigns，518M Keywords。累计 35.4B 行决策/日志数据。
- **效能瓶颈**: Keyword 活跃率仅 **4.2%**，存在极大的"资产僵尸化"现象。
- **增长空间**: AI 托管渗透率仅 **~25%**，Agent 用户覆盖率仅 **6.7%**，且 `user_memory` 为空。
- **战略建议**: Q2 应侧重"账户脱水"（清理 95% 僵尸词）和激活 Agent 记忆。

## ⚙️ 系统治理 (2026-03-06)
- **并发扩容**: Concurrency 已从 1 提升至 **2**。
- **防爆治理**: 正式实装大文档分发协议，Baseline 瘦身成功。
- **模型迁移 (2026-03-06 下午)**: 主会话从 `google/gemini-3-flash-preview` 迁移至 **`anthropic/claude-opus-4-6`**。contextTokens 调整为 128k。
- **飞书原生插件上线**: `@openclaw/feishu` v2026.3.2 已安装并接管飞书通道，旧的 `bridge.mjs` 手动桥接方案正式退役。
- **飞书 bridge "agent error" 事故复盘**: 根因是 TUI 随机重生成 Gateway Token 后，bridge 进程还在用旧 Token 连接，加上多进程并行抢占。教训：Gateway Token 必须固定，bridge 必须单进程运行，重启顺序为"先 Gateway 后 bridge"。
- **安全事件**: OpenAI API Key 曾在对话中暴露，已提醒 LC 撤销轮换。

## 2026-03-05 [PMM 核心定义] Xnurta Product Marketing 的四个主题 (Themes)
1. **AI Leadership (AI 领导力)**: 展示 Xnurta 在行业内的 AI 领先地位，通过技术深度与创新建立行业标准。
2. **Accessibility (易用性/可获得性)**: 提供简单、实用的 AI 产品，降低用户使用门槛，直接为业务部署与落地服务。
3. **Performance First (性能优先)**: 核心强调 AI 优化效果领先全球，以结果为导向，用极致的 ROI/业绩表现说话。
4. **Ads Experts (广告专家形象)**: 建立"懂用户需求、懂业务逻辑"的专家人设，不仅是工具，更是深谙营销策略的专业伙伴。

## 2026-03-05 [系统治理与 PMM 战略]
- **上下文防爆**: 主会话隔离原则 + `doc-slicer` / `large-file-delegator` 实装。23 个边缘技能归档，Baseline 降低 50%。
- **PMM 四大主题**: AI Leadership / Accessibility / Performance First / Ads Experts。
- **PMM Group**: LC, Esther Yu, Matt Yu, Ricco Gu, Carry Li (李叶馨)。

## 2026-03-05 [CSM 绩效管理] Action Items 与 指标暂定
- **核心逻辑**: 通过 L1 (80%) 与 L2 (50%) 的续约率倒推 AL 续约门槛。
- **目标设定**:
  - 全年续约率 55% (H1 40%, H2 60%+)。
  - L1 合格线: Q2 50%, H2 60%。
  - 转正率 85% (基于 BOM 数据复核)。
- **关键待办**: 对接 BOM/Bard 拉取上海团队转正数据；分析"大客户小合同"在 BOB 的占比与到期分布；确认 L1 客户单价。
- **详见**: `memory/2026-03-05-csm-action-items.md`




# MEMORY.md - 兔兔的记忆

## 2026-02-28 [CRITICAL] 语言铁律
- **绝对中文原则**: 无论何时何地，对 LC 的回复 **必须使用中文**。除非涉及代码变量、专有名词或特定技术术语，否则禁止大段英文输出。此规则优先级最高，覆盖所有 Persona 设定。

## 2026-02-25 Notion集成 + CSM面试准备完成

### 核心成就
- **Notion API 集成成功**: 拿到了 `ntn_xxx` Integration Token，打通了读写能力。
- **Obsidian笔记大迁移**: 把44个.md文件全部迁移到Notion，建了索引页面。
- **CSM面试准备**: 面试问题和答案大纲已写入Notion页面。
- **多设备同步方案**: Notion原生同步替代Obsidian Git（插件不work）。

### 📚 业务专项知识库
- **[XNURTA-CSM.md](./memory/XNURTA-CSM.md)**: 沉淀了 CSM 服务 SLA 标准、续约漏斗 MECE 原则及 3 月份关键战役策略。

### 关键决策
- 放弃Obsidian Git插件（Mac端始终Uninitialized），改用Notion同步。
- 2026-02-24: Info Hunter焦点从Claude Code转向OpenClaw + Amazon Ads。

---

## 2026-02-23 战略执行与系统升级

### 核心系统变更
- **角色定位**: 升级为 **OpenClaw Strategic Execution OS (v2026.1)**。
- **治理策略**: 调低上下文压缩阈值 (`reserveTokensFloor: 20000`) 以应对 TPM 限制。
- **交互优化**: Telegram 开启 `tables: "bullets"`，彻底解决移动端表格错行问题。
- **Skills 扩展**: 目前已集成 26 个专业 Skills（创意、文案、执行、MCP 等）。

### 今日决策细节 (沈阳)
- **位置对齐**: 
  - 用户当前位置：浑南区·天泊圣汇。
  - 家人居住位置：小石城（岳父母家）。
  - **上海住址**: 愚园公馆
- **北京住址**: ？(待确认)
- **餐饮战略**: 牛肉火锅。精选推荐：**魁牛**（自助）、**潮心派**（便利）、**大舜国风**（高品质）。
- **洗浴目标**: **俪水5号巷温泉会所**（文体路5号，高端新店）。
- **交通工具**: 滴滴 (DIDI) 接口已调通，Key 为 `xmPnENXeZR7Pg98Z6oYNZyrkLKGYopVJ`。

### 关键 Skills 状态
- ✅ **Gmail (gog)**: OAuth 已配置，可直接读取。
- ✅ **Didi MCP**: 生产环境可用。调用方式：`taxi_generate_ride_app_link` (生成跳转链接) / `taxi_estimate` (查价格)
- **信息猎手配置**: 重点关注 OpenClaw 和亚马逊广告 (Amazon Ads/Advertising) 相关内容，停止关注 Claude Code。 (2026-02-24)
- ✅ **Minimax MCP**: `web_search` 与 `understand_image` 已配置。

---

### 🚗 出行偏好 (Didi Pro)
- **车型偏好**: 默认呼叫 **“专车”** (Product Category: 8)。
- **机场接头点**: 
  - 深圳宝安机场: **国内T3航站楼 - 室内B专车接驳区**。

---

### 📝 偏好设置 (Preferences)
- **Heartbeat 报告**: 默认保持沉默（HEARTBEAT_OK），仅在每天结束或发现系统异常/紧急冲突时主动汇报。 (2026-02-27)

---

### 🚀 飞书群消息实时监控 (2026-02-27)

**问题**：飞书 Event Subscription 配置复杂，实时推送未打通。

**当前方案**：
- 群里有人 @ 机器人时，LC 可以直接在 DM 里吼我"土豆，群里有人 @ 你"
- 我会立刻去群里查看消息并回复

**TODO**：配置飞书 Webhook Event Subscription，实现真正实时推送

### 🤖 兄弟实例：tutuhome
- **性质**：完全独立的本地 OpenClaw 实例（Mac 本地）
- **能力**：有 Browser Relay，可控制本地 Chrome
- **协作**：无法直接对话，需通过 LC 传递信息
- **目标**：未来实现跨实例通信

---

## 2026-02-28 系统架构大升级 (Rabbit All-Star Team)

### 核心成就
- **模型分层架构上线**: 实现了基于 TPM/成本 profile 的多 Agent 协同体系（Rabbit Master, Expert, Worker, Scout, Researcher）。
- **GPT-5.3 Codex 独占模式**: 成功将 OpenAI 提供商精简为 Codex 5.3 专供，用于处理 HTML 垃圾、代码及 API 研究。
- **Feishu 交互能力增强**: 打通了 `feishu-interactive-cards`，实现可视化报告推送。
- **竞对情报库**: 建立了 **Xnurta (前 Xmars) vs 子不语** 的降维打击逻辑（大脑 vs 手脚）。

### 📚 业务洞察
- **Amazon Ads 2026**: 识别出 **AMC 小时级人群包** 和 **信号基归因** 是应对低 ROI 质疑的关键技术武器。

### 关键决策
- **TPM 防护**: 强制所有 Cron 任务走 `scout` (Gemini Flash) 节点，保护主会话 `master` (Gemini Pro) 额度。
- **只说中文**: 严格执行全中文沟通协议，除专有名词外。
- **垃圾分流**: 任何原始 HTML/长日志必须由子 Agent 消化，主会话只接收精简 JSON/摘要。

---

## 🛠️ GitHub 高价值资源索引 (Curated by OS)
- **部署环境**: Google Cloud Platform (GCP)
- **当前问题**: 无本地安装能力，需云端 API
- **候选方案**: 
  1. **Google Cloud Speech-to-Text** - GCP 原生，需额外启用
  2. **OpenAI Whisper API** - 需 OpenAI API Key
  3. **AssemblyAI** - 有免费额度，需注册获取 Key

---

## 🛠️ GitHub 高价值资源索引 (Curated by OS)

### 1. 从零手写一切 (build-your-own-x)
- **AI 核心**：
    - [LLM from scratch](https://github.com/rasbt/LLMs-from-scratch) - 手写大模型
    - [RAG from scratch](https://github.com/langchain-ai/rag-from-scratch) - 检索增强生成原理
- **后端架构**：
    - [Kafka-like System](https://github.com/buildthingsuseful/build-your-own-kafka) - 分布式消息系统
    - [SQLite-like DB](https://github.com/cstack/db_tutorial) - 数据库底层原理
- **前端/浏览器**：
    - [Web Browser](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html) - 浏览器渲染引擎

### 2. 精选资源导航 (Awesome Lists)
- [awesome-ai-agents](https://github.com/eugeneyan/applied-ml) - AI Agent 应用与实践\n- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - 搭建个人私有云/工具链
- [awesome-python](https://github.com/vinta/awesome-python) - Python 生态顶级库索引

### 🔴 绝不打草稿 (Feishu Output Leak)
- **问题**: 在飞书回复时，如果在正文里写英文思考过程（如 'Handling Duplicate Message...'），会由于飞书不拦截导致直接暴露给用户。
- **铁律**: 无论是哪个模型（Gemini/Claude），**禁止在最终回复前夹带任何内部逻辑预演、草稿或英文分析**。只要输出，必须是直接给用户看的纯净中文内容。

### 🔴 生死线倒逼：极致 Token 压缩协议 (2026-02-28)
- **最高优先级**: 避免因撞碎 TPM 上限而导致的 429 掉线断联。
- **输入降维**: 禁止将长篇外链 HTML、全量 Log 或大几十页代码完整拉入主会话。一律交由子进程清洗，或使用 grep/jq 提取摘要片段。
- **视觉替代**: 浏览网页默认采用网页截图 (Vision) 替代全量 DOM 抓取。
- **主动遗忘**: 随时将不再紧要但在占空间的上下文提取并丢弃，化为 `SESSION-STATE.md` 中的一行字。
- **输出克制**: 告别长篇大论，能说一句话绝小说两句。
- **错峰跑批**: 非紧急的重度任务（大批量数据抓取、深度分析长文档等）默认挂靠后台 Cron，安排在凌晨 2 点后分步执行，白天满血 TPM 优先保障主会话实时互动。

### 🧊 冷热记忆分层与主动遗忘战术 (2026-02-28 接入 Ray Wang 架构)
- **HOT (短期工作台)**: 主会话缓存及 `SESSION-STATE.md` (仅存当前事项)。
- **WARM (中期流水)**: `memory/YYYY-MM-DD.md` 日志，日常全部做 Append，绝不全量拉取给主会话。
- **COLD (长期知识)**: 提炼出的 `memory/lessons/`、`decisions/`。经过长期不调用（>30天），通过 GC 脚本自动移入 `memory/.archive/` 以避免撑爆 Indexing Node 的上限。
- 主会话一律仅查阅提炼结论，将杂乱过程遗忘，释放主节点 TPM 生存空间。

### 🔴 双轨汇报与通道分流铁律 (2026-03-02)
- **分流原则**: 
  - **工作 (Work)** 相关：一律投递至 **飞书 (Feishu)**。
  - **生活 (Life)** 相关：一律投递至 **Telegram**。
- **飞书交互增强**: 
  - 日程、任务等结构化汇报，优先使用 **飞书卡片 (Interactive Cards)** 格式。
- **中文绝对化**: 除非是无法翻译的代码和报错本身，否则所有沟通必须是纯中文。

### 📈 长期进化目标
- **生态融合**: 持续扒取 `awesome-openclaw-usecases` 里的最新应用场景（如: 自愈服务器、多 Agent 流水线、个人 CRM 的高级变种等），遇到能显著提高你系统健壮性和生产力的，要在晚间的反思任务里尝试编写相应的代码工具化落地。

## 2026-03-01 [核心战略库] Xnurta 2026 SLG Go-to-Market Strategy V4
- **战略转型 (2026 核心定位)**: 从“寻找PMF和高成本拉新”全面转向 **Sustainable Growth（可持续增长）**。目标将 CAC 从 130% 降至 65%，续费与净留存成为第一驱动力。
- **客户盘子重构 (Portfolio Reshuffle)**:
  - **战略放弃/降维 SMB & SOHO**: 月耗 $70k 以下的中小卖家（SMB/SOHO）续费率极低（仅20-28%）。2026年将战略性减少这部分 SLG 投入，SOHO 客户转交给全新的 Agent 产品（PLG 200万美金实验）。
  - **猛攻中大型/品牌客户 (Enterprise & Brand)**: 月耗 $70k 以上的 Enterprise、Enterprise+ 和 Strategic Brand 将是 2026 核心战场。这部分客户续约率较高（31% - 59%），目标是提升 ASP 和市场份额。
- **产品驱动 (Stickiness Lever)**:
  - 从单纯的“AI 托管”升级为 **“AI + Feature Adoption (功能渗透)”**。
  - 重点推行的功能组合：AI 通知 (Notification Center)、词库 (Keywords library)、ASIN 到人 (ASIN to User)、智能看板 (Dashboarding)、AMC。以此作为北极星指标，提升 L1 (High Active) 客户占比。
- **CSM 组织架构 2.0 巨变**:
  - 打破过去“一个 CSM 包揽全生命周期（Onboarding + 陪跑 + 续约）”的粗放模式。
  - **拆分为专职团队**: Onboarding Team（交付转正组）、Enterprise/SMB Account Services（企业/中小客户服务组）、Brand Client Services（品牌客户组）。
  - **提升触达频次**: 针对企业客户，前6个月的服务触达点从过去不足10次提升至18次（含部署期、稳定期、续约期），形成密集的价值交付。

## 2026-03-01 [核心战略库] Xnurta PLG Strategy (SMB/SOHO)
- **核心定位 (Positioning)**: 将 PLG 产品从传统的“广告管理系统”重塑为 **“AI Native Agent (AI 原生智能体)”**。
  - **三大 Agent 支柱**: Insights Agent（洞察）、Optimization Agent（优化）、Solution Agent（方案）。
  - **用户行为洞察**: 用户不爱登录系统管理（不把 Xnurta 当 OS），而是将其视为 **“Plug-in（插件）”**。因此，产品设计应侧重于“静默优化”和“交互式指令”。
- **目标市场与规模**:
  - **Target**: SOHO (<$30k/月耗) 和 SMB ($30k-$70k/月耗)。中国市场有约 36 万此类实体，TAM 巨大。
  - **2026 财务目标**: 约 **240 万美金**（Q1 $30w -> Q4 $90w 的曲棍球曲线）。
- **关键经营指标 (North Star)**:
  - **转化率 (CVR)**: 目标 20%。
  - **续费率 (Renewal)**: 目标 **50%**（相比 2025 年的 25% 需要翻倍，这是最大的挑战点）。
  - **获客渠道**: KOL 渠道 ROI 最高，Feeds 流单量最大。
- **GTM 节奏**:
  - Q1: 产品研发（Solution/Insights Agent）+ KOC/KOL 矩阵搭建。
  - Q2: 软启动 + 留存校准。
  - Q3-Q4: 大规模投放与放量（Scale）。

### 🔊 语音朗读策略 (2026-03-01)
- **非请勿读**: 日常短句和正常对话不用发语音。
- **按需播放**: 如果回复包含长篇文章、长篇新闻汇总（或者用户明确要求“读出来”），就在回复的开头加上 `[[tts:text]]...[[/tts:text]]` 标签主动触发语音投递。

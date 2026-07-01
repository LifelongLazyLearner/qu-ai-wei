# agentskills.io 对照评审 (v0.8.1)

> 本文档记录把 `qu-ai-wei` 拿去对照 [agentskills.io](https://agentskills.io) 的 skill 创作最佳实践后的结论:哪些是强项、哪些动了、哪些刻意没动以及原因。配套版本 v0.8.1 的两处实质改动(描述触发词优化 + 品牌表去重)见 [`CHANGELOG.md`](../CHANGELOG.md)。

## 评审基准

对照 agentskills.io skill-creation 系列三篇:

- **Best practices** — context economy、progressive disclosure、moderate detail、calibration。
- **Optimizing descriptions** — description 是首要触发信号,要同时写清「做什么」和「什么场景触发」;模型倾向 *under-trigger*,描述要写得偏主动。
- **Evaluating skills** — 输出质量评测 harness(prompt + 期望行为 + 断言,with/without-skill 对照)。

## 强项(刻意不改)

1. **Progressive disclosure** — `SKILL.md`(必加载层)+ `references/*.md`(按需加载)+ `scripts/build-flat.sh`(给不支持 progressive disclosure 的 Cursor / Windsurf / Warp 拍平成单文件)是教科书式做法。每个 reference 文件顶部有「本文件是…」preamble 说明何时读。拍平脚本会剥掉 preamble,避免重复。
2. **具体性 & 示例** — 冲突仲裁顺序配仲裁示例、真人 vs AI 对照表、九语体激活矩阵、每条模式带「原文 / 改后」对。这是 agentskills.io 反复强调的「examples beat rules」,本 skill 已经做到。
3. **Frontmatter 规范** — `name` / `version` / `description` / `license` / `compatibility` / `allowed-tools` 齐全,`name` 匹配目录名,`description` 用 block scalar。

## 唯一实质发现:context economy

`SKILL.md` 当前 **935 行 / 68,118 bytes / 32,540 Unicode codepoints**(CJK 文本 token 数依赖分词器,故只报行 / 字节 / 码点数,不报 token 数)。agentskills.io 的 context-economy 指引是一条「合理的 agent 注意力预算」,不是 skill 必须达到的已发布标准 —— 发现本身成立(必加载层偏大),但不靠某个具体阈值立论。

「偏大」的根子在 **重复**,不是信息密度。本版动了两处:

### 动了:品牌表去重(v0.8.1)

「品牌广告 vs 自媒体营销号:三条识别线」表(3 行表 + 4 个边界场景)**此前在 `SKILL.md` 和 `references/brand-voice.md` 各存一份**。`build-flat.sh` 先原样吐 `SKILL.md` 正文(含这份表),再在附录里拼 `brand-voice.md`(又含一份),flat build 把同一张表发了两遍。

改动:`SKILL.md` 删掉自己的副本,留一行指针,显式说明「在语体识别阶段若拿不准是品牌广告还是自媒体,读 `references/brand-voice.md` 的同名小节」。canonical 副本留在 `brand-voice.md`(已被 `build-flat.sh` 嵌入)。flat build **净减 ~15 行**(少了一份重复),不是「保持不变」。顺带修了一个预存 bug:`SKILL.md` 原本写「**两个**边界场景」却列了 4 条,`brand-voice.md` 正确写「**四个**」—— 去重后 canonical 副本用对的那个。

**load-order 说明:** 这张表是「在还没确定是品牌广告时用来鉴别」的辅助,而 `brand-voice.md` preamble 说「非品牌语体不需要读此文件」。指针措辞因此特意写成「**在语体识别阶段**若拿不准…读 brand-voice.md」,明确把读取时机前移到鉴别阶段;`SKILL.md` 怎么判别语体的三信号(句式密度 / 词汇身份 / 读者对象)仍留在必加载层,初始识别不依赖这张表。Cursor / Windsurf / Warp 的 flat 用户不受影响(表仍在附录里)。

### 刻意没动:51 条模式索引表

`## 51 条 AI 腔模式 · 索引表`(一句话速查索引)看起来是「该挪到 reference 里」的候选,但**不能挪**。两处证据:

- `SKILL.md` 索引表自己写明:「一句话速查索引(决策树:看到关键词 → 查表 → 命中后读对应 reference 核对)」。它是一张**决策树扫描面**,不是详情。
- `scripts/build-flat.sh` 注释里明说:「索引 + 详情并存,不是替换」。

把索引挪到 reference 会**倒置 progressive disclosure**:agent 为了扫一眼就得先加载一个 reference 文件。索引是「扫完才决定要不要加载」的东西,必须留在必加载层。

### 刻意没动:破折号密度基线

`### 破折号的密度基线`(论证为什么破折号在真人中文里基线接近 0)**没有**对应的 `references/punctuation.md` 小节(`punctuation.md` 只有标点频率基线总表)。挪过去会给 `punctuation.md` 新增一个小节、并在 flat build 附录里重排内容顺序。v0.8.1 不动,留作未来可选项。

## 动了:描述触发词优化(v0.8.1)

对照「Optimizing descriptions」:模型倾向 under-trigger,描述要把用户真会打的触发话术写进去。原描述的隐式触发只列了「去 AI 味 / 改得说人话 / humanize 中文」。

改动后描述(4 行,role-labeled):

```
去除简体中文文本里的 AI 写作痕迹,不虚构事实,让终稿干净、精准。
触发:显式 `/qu-ai-wei`,或用户说「去 AI 味 / 改得说人话 / humanize 中文 / 改自然点 / 读着别扭 / 太生硬了」时自动调用。
约束:按「冲突仲裁顺序」六级执行;终稿强制附打磨报告。
范围:只支持简体中文;繁體(台 / 港用字)不自动处理。
```

**新增触发词**(真实高频、原描述未覆盖):

- `读着别扭` —— 抓住「能感到别扭、但不会说『AI 味』」的用户,这是原描述最大的覆盖盲区(原触发词全部明示 AI / 人话)。
- `太生硬了` —— 生硬是 AI 生成 / 翻译腔文本的标准中文描述词,原描述 0% 覆盖。
- `改自然点` —— 跟原「改得说人话」语义相邻,但更接近口语。

**去掉** `这段太 AI 了`(跟 `SKILL.md` 正文已有的「这段中文太 AI 了,改一下」重复)。

**其它措辞调整**(都过中文 authentic 校验,不犯本 skill 自己批评的模式):

- 去掉早期草案里的 `且…任何`(翻译腔 + 过度修正),恢复简洁的 `不虚构事实`。
- `暂未纳入` → `不自动处理`,更如实 —— §2 真人停手门检其实接受繁體输入(停手、只清格式),不是「完全不管」。
- 每行加角色标签(触发 / 约束 / 范围),描述的职责就是触发可靠性,标签用清晰度换暖度,可接受。

## 评测 harness:复用既有 tests/,不另起 evals/

agentskills.io 的「Evaluating skills」建议搭输出质量评测 harness。本仓库**已经有**一套 manifest-based harness(刚在 v0.8.0 并入):`tests/eval-manifest.txt` + `tests/check-runs.sh` + `tests/after/` anchor output,`tests/runs/` 留给未来 captured runs。

v0.8.1 因此**扩展** `tests/`,不另起 `evals/` 目录(避免两套 harness 让人困惑「到底哪套重要」):

- 新增 [`tests/trigger-manifest.txt`](../tests/trigger-manifest.txt) —— ~12 条触发用例(TRIGGER / NO-TRIGGER / BOUNDARY),格式复用 `eval-manifest.txt` 的 `[NN]` + `key=value`。
- 新增 [`tests/check-triggers.sh`](../tests/check-triggers.sh) —— 静态守卫:对每条 TRIGGER 用例,断言它的 `anchor` 在 `SKILL.md` 描述里逐字存在。**这是描述内容守卫,不是行为触发测试** —— 真实触发行为测试需要不确定的模型跑一轮,留给用户在干净会话里逐条手跑(`query` / `expect` 字段为此准备)。

为什么不搭完整的 with/without-skill 对照 benchmark:那是重活,而且 skill 是 prompt、不是代码,with/without 比较只有在 model + version 完全锁定时才有意义。当前深度是「搭好 + 提议」,把可复用的轻量守卫先落地,行为测试留给后续迭代。

## 验证

改动后跑全套既有 gate:

```bash
bash scripts/build-flat.sh          # 重生成 .cursorrules / WARP.md
bash tests/check-version-sync.sh    # 版本号 5 处同步
bash tests/check-snapshot-smoke.sh  # 18 条样本结构烟测
bash tests/check-runs.sh tests/after
bash tests/check-triggers.sh        # 新:触发词锚定守卫
git diff --check
```

**已知盲区(v0.8.2 已补):** `check-version-sync.sh` 只查版本号字符串,不 diff flat build 内容。v0.8.1 评审时这还是个盲区 —— 对当时的 ~15 行去重靠 `build-flat.sh` 重生成 + 手动 `git diff` 复核。v0.8.2 新增 [`tests/check-flat-sync.sh`](../tests/check-flat-sync.sh):重新生成一份 flat build 跟仓库里 commit 的 `.cursorrules` / `WARP.md` 做字节级比对,漂移即 fail。此后「改了 SKILL.md / references/ 忘了重跑 `build-flat.sh`」会被 CI 抓到。

## 评审轮次记录

本评审经三轮 AGENTS.md 对抗评审(CEO / 中文 / 工程),前两轮 plan 被 reject(evals/ 目录跟刚发布的 tests/ harness 撞车;flat-build「不变」的声明被证伪 —— 品牌表本就重复;所有实质改动被「提议但不应用」地推走)。最终 substance-first 重设计获三位评审 approve,verdict 记在 v0.8.1 commit body。

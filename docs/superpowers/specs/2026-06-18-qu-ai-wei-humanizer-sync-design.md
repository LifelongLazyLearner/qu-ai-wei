# qu-ai-wei × humanizer 同步:补 3 条新模式

- **日期:** 2026-06-18
- **状态:** 待 3-reviewer 门审 → 用户复核
- **触发:** 用户要求对照 [humanizer](https://github.com/blader/humanizer)(v2.8.0 / 33 patterns)迭代 qu-ai-wei(v0.7.1 / 51 patterns)

## 背景与判断

qu-ai-wei 已远超 humanizer:51 vs 33 条模式、9 大类、停手门检、9 种语体识别、品牌语体反向锚点(Apple / Nike CN)、打磨报告、过度消毒反制、硬证据规则(#47/#47b)。它是 humanizer 早期版本的中文分叉,之后大幅前进。

逐条比对 humanizer 33 条后,**只有 3 条**是「humanizer 较新增补(#27-33 区块,qu-ai-wei 分叉后才进 humanizer)+ 中文有对应语境 + qu-ai-wei 覆盖不足」的可迁移项。其余要么已被更好地覆盖,要么是英文专属(title case / hyphenated pairs / en-dash / 弯引号默认值)。

**核心约束(来自 [AGENTS.md](../../../AGENTS.md)):** 上下文经济 —— 不新增编号规则,全部折叠进既有规则,沿用 #22a / #47b 子模式惯例。规则总数保持 **51**。

## 三条改动

### 改动 1 — 假坦诚开场(humanizer #33)→ 新子模式 #19b

**问题:** AI(尤其较新模型)爱用 `讲真 / 说实话 / 老实说 / 不瞒你说` 当开场钩子,后接一句自信平铺的套话 —— 假装掏心窝,实则没增信息。结构跟 #19「需要注意的是」同源:#19 是「提示下面来个重要的,然后没下文」,#19b 是「提示下面来个真心话,然后是套话」。

**家:** [references/patterns.md](../../../references/patterns.md) #19 节下,编为 **#19b**(不单独计数,同 #22a / #47b)。索引表里作 #19 下的缩进子项,同 #22a 在 #22 下的写法。

**触发(三条全中才算 AI 腔):**
1. **位置** —— 句首 / 段首开场,不是句中插入
2. **后接** —— 自信 / 平铺 / 概括 / 推销式断言
3. **密度** —— 多段反复拿 `讲真 / 说实话 / 老实说 / 不瞒你说` 当钩子

**不触发(保留为毛边):**
- `说实话` 接 **不确定 / 复杂反应** —— `说实话我也不知道该怎么想`
- 句中单次插入的 `说实话`

判别结构镜像 #48 的「好句识别」例外(落点抽象=AI vs 落点具体/坦白=好句)。

**互锁防误杀(关键,Eng reviewer 命中「非对称加载」后强化):** qu-ai-wei 现在把 `说实话我也不知道` 当**正面毛边样本**写在两处 —— [SKILL.md](../../../SKILL.md) §个性与灵魂、§过度消毒反制·个人化表达。#19b 的**检测**住在按需加载的 patterns.md,而毛边**保护**住在每次必加载的 SKILL.md;若只补一个「见 #19b」指针,轻量 pass 会永远保护 `说实话`、永远不触发 #19b → 偏向漏检 AI 假坦诚。因此 SKILL.md §过度消毒反制·个人化表达 加的那一行必须**自带判别式本体**,不是纯指针:

> 边界:`讲真 / 说实话` 当**开场钩子 + 后接套话** = #19b 改;接**不确定 / 复杂反应**(`说实话我也不知道`)= 毛边保留。

这样每次必加载的那层就能独立执行判别,不依赖 patterns.md 是否被加载。

**第三处 `说实话`(独立对抗复审 B1 命中 —— 原「两处不留缝」声明错误):** `说实话` 还出现在 [references/whitelists.md](../../../references/whitelists.md) 第 40 行 —— 作为 `TBH` 的**错译示例**(❌ 列:"不要把 TBH 翻成 说实话,保留 TBH")。于是同一个 `说实话` 在三个文件里有三种价:whitelists=AI 错译产物(负),毛边=真诚反应保护(正),#19b=开场钩子删(负)。这是字符层歧义,冷启动 agent 做串匹配时可能误推。**处理:** whitelists.md:40 那行的 `TBH` 错译示例**删掉 `说实话` 这一个 gloss**(该行本就是「一组速记 → 一组错译」非一一对应,留下 `太长不看 / 顺便说一下 / 仅供参考` 已足够演示「别过度翻译速记」的点)。删掉即消除三向歧义,教学意义零损失。删后 #19b ↔ 毛边 两处显式互指,whitelists 不再插一脚。

### 改动 2 — 格言公式(humanizer #32)→ #37 公众号伪深度子模板

**问题:** humanizer #32「X is the Y of Z / X becomes a trap」的中文自媒体对应:`XX 是成年人的 YY` / `XX 是当代人的 ZZ` / `XX 本质上是一场 YY` —— 把论点包装成可转发金句,显深刻实空洞。

**家:** [references/platform-patterns.md](../../../references/platform-patterns.md) #37 节(自媒体伪深度)下,作命名子模板。原生栖息地是自媒体 / 公众号标题与正文,#37 是正确归属。

**触发:** 密度敏感 —— 短段内反复用「X 是 Y 的 Z」格言模板;换主语仍成立;落点是抽象拔高而非具体事实。

**不触发(独立对抗复审 M3 命中 —— 原缺具体例):** 单次、且 Y/Z 是具体去光环的真相(跟 #48 例外同口径)。`XX 是成年人的 YY` 本身是真人常用结构,必须给落地例,别让 agent 自己 backfill:
- ❌ AI 腔:`断舍离是成年人的精神修行` —— Y 是抽象拔高
- ✅ 好句(保留):`降薪是成年人的体面` —— Y 是去光环的具体真相

交叉引用 #48(否定对举堂兄弟)+ #22(排比段)。

### 改动 3 — 权威洞察腔(humanizer #27)→ 扩 #19 关键词表

**问题:** humanizer #27「at its core / what really matters / the real question」中文版:`真正的问题是 / 核心在于 / 说到底 / 归根结底` —— 假装切中要害的空枢纽。

**家:** 扩 [references/patterns.md](../../../references/patterns.md) #19 的关键词清单。`本质上` 已在打磨 filler 删除清单([SKILL.md](../../../SKILL.md) §主动打磨动作 3),不重复。纯清单扩充,不新增条目。

**关键约束(日常中文 reviewer 命中「过度修正风险」后加):** `说到底 / 归根结底 / 核心在于` **本身是地道口语话语标记**,不是纯 AI 腔 —— `说到底还是钱的问题` 是真人常说的话。若把它们当 #19 那种「见词即删」的硬关键词,这个 skill 自己就犯了 §避免过度修正。所以 #3 的新词**必须继承 #19 的密度判定**(短段反复出现才疑),并补一条**不触发**:口语里单次、且后面真有落地内容的 `说到底 / 归根结底`,保留。判别同 #48 落点法 —— 后接抽象拔高=改,后接具体事实=留。

**加载策略说明(独立对抗复审 m1):** #3 的新关键词**只入 patterns.md(按需层)**,不入 SKILL.md always-loaded 层。理由跟 #19b 相反:#19b 不进 always-loaded 会**漏检**(危险方向),所以把判别式提上去;#3 若漏触发只是**少改一处口语 marker(under-fire,安全方向)**,且往 §过度消毒反制 塞 4 个口语词会 bloat 必加载层。故 #3 不做 #19b 那种上提,只留 patterns.md 内的密度+落点门。

## 受影响文件(同一改动内全部同步,遵 CLAUDE.md「文档与代码同步」)

| 文件 | 改动 |
|------|------|
| [references/patterns.md](../../../references/patterns.md) | #19 加 #19b 子模式 + 扩 #19 关键词表(改动 1、3) |
| [references/platform-patterns.md](../../../references/platform-patterns.md) | #37 加格言公式子模板(改动 2) |
| [references/whitelists.md](../../../references/whitelists.md) | **第 40 行删 `说实话` gloss**(B1,消除三向歧义) |
| [SKILL.md](../../../SKILL.md) | §过度消毒反制·个人化表达 加 #19b 判别式一行(自带本体,非纯指针);§51 条索引表 #19 行下加 #19b 缩进子项(同 #22a);frontmatter `version: 0.7.1 → 0.8.0` |
| [README.md](../../../README.md) | 版本号全量 bump(见下「版本同步触点」);humanizer 陈旧计数 3 处软化(见下,不硬改 29→33) |
| [CHANGELOG.md](../../../CHANGELOG.md) | 加 `### v0.8.0（2026-06-18）` 节;`Unreleased` 内容(离线 harness)并入 v0.8.0(见下 m3) |
| `.cursorrules` / `WARP.md` | **不手改** —— 跑 [scripts/build-flat.sh](../../../scripts/build-flat.sh) 重新生成(已含 patterns.md + platform-patterns.md 源,版本提示从 frontmatter 取) |
| git tag | `v0.8.0` 在 ship 时打 + push(遵记忆 feedback_tag_on_version_bump) |

**版本同步触点(独立对抗复审 M2 —— `tests/check-version-sync.sh` 断言 6 串,只改 frontmatter 会挂):**
1. [SKILL.md](../../../SKILL.md) frontmatter `version:`
2. [README.md](../../../README.md):3 badge `version-0.7.1-blue.svg` → `0.8.0`
3. [README.md](../../../README.md) `当前 v0.7.1` / `（v0.7.1）` 全部出现处(第 10、24、56、203 行)→ `v0.8.0`
4. [README.md](../../../README.md) §版本记录 最近更新列表加 `- **v0.8.0（2026-06-18）...`
5. [CHANGELOG.md](../../../CHANGELOG.md) `### v0.8.0（` 节
6. `.cursorrules` / `WARP.md` `版本 0.8.0 开发版`(build-flat 自动)

改完跑 `bash tests/check-version-sync.sh` 一次过。

**附带数准修正(CEO reviewer「陈旧磁铁」+ 独立对抗复审 M1「漏一处」后改方案):** [README.md](../../../README.md) 把 humanizer 记作「29 条规则」共 **3 处:第 62、206、411 行**(原 spec 只列 206/411,漏了 62)。实际 humanizer 现为 v2.8.0 / 33 条。**但不硬改 29→33** —— 钉死一个 humanizer 的精确条数,每次 humanizer 发版都会重新过时,是自找的维护负债。3 处统一**去掉精确数 / 软化为「30 余条」**,不再追踪 humanizer 的版本计数。不动「约一半 / 约 17 条」(那是 qu-ai-wei 借用量,非 humanizer 总数)。

## 版本

0.7.1 → **0.8.0**(minor)。理由:#19b 是真正的新检测行为,会改变输出;改动 2/3 是既有规则细化。计数仍 51。ship 时确认并打 tag。

**CHANGELOG Unreleased 处置(独立对抗复审 m3):** [CHANGELOG.md](../../../CHANGELOG.md) 现有 `### Unreleased` 块(离线 real-run 回归 harness,来自前一 commit)。它本就要随下一版发布 —— 即 v0.8.0。故 v0.8.0 节**收纳两部分**:(1) Unreleased 的离线 harness 条目上滚进来;(2) 本次 3 条新模式。不另留 Unreleased 块。

## YAGNI / 不做

- 不加英文专属模式(title case / hyphenated pairs / en-dash / 弯引号默认)
- 不新增编号规则,不动 51 总数
- 不重写 humanizer 已被更好覆盖的条目
- 不做与本同步无关的重构

## 验证

- 跑 [tests/check-version-sync.sh](../../../tests/check-version-sync.sh) 确认 6 个版本串跨文件一致
- 跑 [tests/check-snapshot-smoke.sh](../../../tests/check-snapshot-smoke.sh) 确认 build-flat 输出无破损
- **回归断言(独立对抗复审 m2 —— 新规则要有 guard,别成 silent regression):** 仿 #48/#47b 在 [tests/check-snapshot-smoke.sh](../../../tests/check-snapshot-smoke.sh) 加 `rg -q` 断言,覆盖 #19b 假坦诚开场 + #37 格言公式;并加对应 fixture(一段「讲真/说实话」开场套话 + 一段「XX 是成年人的 YY」自媒体文)。同时验证真诚 `说实话我也不知道` 不被误杀。
- 跑 [scripts/build-flat.sh](../../../scripts/build-flat.sh) 后 grep `.cursorrules` / `WARP.md` 确认 #19b + 格言子模板 + whitelists 删改已同步

## Reviewer 门审(最终轮)

第一轮三位 roster reviewer 各命中 needs-changes(CEO:README 计数陈旧磁铁;日常中文:#3 口语 marker 过度修正风险;Eng:#19b 非对称加载 + 索引粒度)。全部修订后,独立对抗冷复审又命中 1 blocker + 3 major + 3 minor(B1 whitelists.md 三向歧义;M1 漏 README:62;M2 版本同步 6 触点;M3 格言缺不触发例;m1/m2/m3)。全部已在本 spec 落实。最终轮:

- **CEO / holistic:** ✅ sign off —— 价值集中在 #19b(补真实盲点),折叠不膨胀,计数不再追 humanizer 版本。
- **日常中文表达(adversarial):** ✅ sign off —— 新触发词均地道;#3/#19b/#37 全部密度+落点门 + 不触发例,不犯 §避免过度修正。
- **Eng(skill effectiveness):** ✅ sign off —— 判别式提进 always-loaded 层、#19b 仿 #22a 嵌套、whitelists 歧义清除、无新 ref 文件(loadability 稳)、加了回归断言。
- **独立对抗冷复审(CLAUDE.md 自动接力):** ✅ 原判 NEEDS CHANGES,B1+M1-M3+minors 全部 resolved,现 clear。

# qu-ai-wei × humanizer 同步实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 humanizer (v2.8.0) 的 3 条可迁移模式折叠进 qu-ai-wei,作为子模式 / 关键词扩展(规则总数保持 51),并完成 0.7.1 → 0.8.0 全量版本同步。

**Architecture:** 纯 markdown 内容编辑 + 回归测试。新检测逻辑住在按需加载的 `references/`;判别式(防误杀真诚 `说实话`)提进每次必加载的 `SKILL.md`。无代码改动,验证靠现有 bash 测试(`check-version-sync.sh` / `check-snapshot-smoke.sh`)+ build-flat 同步检查。

**Tech Stack:** Markdown、bash、ripgrep(`rg`)、`scripts/build-flat.sh`。

**Spec:** [docs/superpowers/specs/2026-06-18-qu-ai-wei-humanizer-sync-design.md](../specs/2026-06-18-qu-ai-wei-humanizer-sync-design.md)(已过 3-reviewer + 冷复审门审)

---

## 文件清单

| 文件 | 责任 | 改动类型 |
|------|------|---------|
| `references/patterns.md` | 核心 A-G/I 规则 | 改:#19 加 #19b 子模式 + 扩 #19 关键词(改动 1、3) |
| `references/platform-patterns.md` | H 组平台 / 文体规则 | 改:#37 加格言公式子模板(改动 2) |
| `references/whitelists.md` | 四类白名单 | 改:第 40 行删 `说实话` gloss(B1) |
| `SKILL.md` | 技能核心(必加载) | 改:§过度消毒反制 加判别式;索引表 #19 下嵌 #19b;frontmatter 版本 |
| `README.md` | 公开文档 | 改:版本号 6 触点;humanizer 计数 3 处软化;版本记录加条目 |
| `CHANGELOG.md` | 版本历史 | 改:加 v0.8.0 节(收纳 Unreleased + 3 模式) |
| `tests/fixtures/18-fake-candor-aphorism.md` | 回归输入 | 建 |
| `tests/after/18-output.md` | 回归 anchor 输出 | 建 |
| `tests/check-snapshot-smoke.sh` | 语义断言 | 改:加 18 block + loop list |
| `tests/eval-manifest.txt` | 断言 manifest | 改:加 [18] block |
| `.cursorrules` / `WARP.md` | 拍平版(不手改) | build-flat 自动生成 |

---

## Task 1: patterns.md — 加 #19b + 扩 #19 关键词(改动 1、3)

**Files:**
- Modify: `references/patterns.md`(#19 节,约 298-307 行)

- [ ] **Step 1: 在 #19 的「问题」段后插入伪洞察枢纽关键词 + 落点门(改动 3)**

定位 `references/patterns.md` 的这一段:

```markdown
### 19. "需要注意的是 / 要知道的是 / 值得思考的是"

**问题：** 空枢纽句，不承载信息，只是在提示"下面来个重要的",然后后面也没啥重要的。
```

改成(在「问题」段后追加两段):

```markdown
### 19. "需要注意的是 / 要知道的是 / 值得思考的是"

**问题：** 空枢纽句，不承载信息，只是在提示"下面来个重要的",然后后面也没啥重要的。

**也覆盖伪洞察枢纽（humanizer #27 中文版）：** `真正的问题是 / 核心在于 / 说到底 / 归根结底` —— 假装切中要害、其实没下文的空枢纽。

**⚠ 密度 + 落点门（别误杀口语）：** `说到底 / 归根结底 / 核心在于` 本身是地道口语话语标记，不是见词即删。继承本条密度判定（短段反复出现才疑），再看落点（同 #48）：
- ❌ AI 腔：`说到底，这是认知的问题；归根结底，还是底层逻辑。` —— 反复 + 落点抽象
- ✅ 口语（保留）：`说到底还是钱的问题` —— 单次 + 落点具体
```

- [ ] **Step 2: 在 #19 节末尾(`### 20.` 之前)插入 #19b 子模式(改动 1)**

定位 #19 的「改后」块到 `### 20.` 之间:

```markdown
**改后：**
> 这个问题涉及三个层面：A、B、C。

### 20. "这里有几个要点"式列表预告
```

改成(在两者之间插入 #19b):

```markdown
**改后：**
> 这个问题涉及三个层面：A、B、C。

#### 19b. 变体：假坦诚开场（讲真 / 说实话当钩子）

**覆盖形式：** `讲真 / 说实话 / 老实说 / 不瞒你说 / 说真的` 放句首 / 段首当开场钩子，后接一句自信平铺的断言。

**问题：** 跟 #19 同骨架 —— #19 是「提示下面来个重要的，然后没下文」，本条是「提示下面来个真心话，然后是套话」。AI（尤其较新模型）用它假装掏心窝、制造亲近感，实际后面不增任何信息。

**判定（三条全中才按 AI 腔）：**
- **位置** —— 句首 / 段首开场，不是句中插入
- **后接** —— 自信 / 平铺 / 概括 / 推销式断言，不是不确定或复杂反应
- **密度** —— 多段反复拿 `讲真 / 说实话 / 老实说` 当钩子

**⚠ 不触发（保留为毛边，别误杀）：** 跟 #48 落点法同口径 —— `说实话` 接**不确定 / 复杂反应**是真人毛边，保留。
- ❌ AI 腔：`讲真，这个功能真的非常强大。说实话，它会改变你的工作方式。` —— 开场钩子 + 平铺推销 + 多段堆叠
- ✅ 毛边（保留）：`说实话我也不知道该怎么想` —— 接不确定反应
- ✅ 毛边（保留）：句中单次 `这事说实话挺难评的` —— 句中插入 + 复杂反应

**与 SKILL.md 互锁：** SKILL.md §过度消毒反制·个人化表达 把 `说实话我也不知道` 列为正面毛边。两处显式互指:开场钩子 + 套话 = 本条改;接不确定反应 = 毛边保留。本条同 #22a / #47b,不单独计数(总数仍 51)。

### 20. "这里有几个要点"式列表预告
```

- [ ] **Step 3: 验证插入无破损**

Run: `rg -n "19b. 变体：假坦诚开场|也覆盖伪洞察枢纽|说到底还是钱的问题" references/patterns.md`
Expected: 3 行命中,分别在 #19b 标题、伪洞察枢纽段、落点门口语例。

- [ ] **Step 4: 确认 51 计数口径未被破坏**

Run: `rg -n "总数仍 51|不单独计数" references/patterns.md | head`
Expected: 命中 #19b 那句「不单独计数(总数仍 51)」,与 #22a/#47b 口径一致。

- [ ] **Step 5: Commit**

```bash
git add references/patterns.md
git commit -m "feat(patterns): add #19b fake-candor opener + extend #19 authority tropes"
```

---

## Task 2: platform-patterns.md — #37 加格言公式子模板(改动 2)

**Files:**
- Modify: `references/platform-patterns.md`(#37 公众号节末尾,`**B. 小红书：**` 之前,约 26 行)

- [ ] **Step 1: 在公众号「伪深度咨询腔」块末尾、`**B. 小红书：**` 之前插入格言公式子模板**

定位:

```markdown
- **判断法：** 随手挑一段，替换术语成同义空泛词（"逻辑闭环" → "想明白"），看看有没有掉信息。没掉 —— 就是伪深度。

**B. 小红书：**
```

改成(在两者之间插入):

```markdown
- **判断法：** 随手挑一段，替换术语成同义空泛词（"逻辑闭环" → "想明白"），看看有没有掉信息。没掉 —— 就是伪深度。

**格言公式（humanizer #32 中文版）：** 把论点包装成可转发金句 —— `XX 是成年人的 YY` / `XX 是当代人的 ZZ` / `XX 本质上是一场 YY` / `XX 是另一种 YY`。显深刻、实空洞。
- **判定：** 密度敏感 —— 短段反复套「X 是 Y 的 Z」格言模板；换主语仍成立；落点是抽象拔高。跟 #48（否定对举）、#22（排比段）联动。
- **⚠ 不触发（同 #48 落点法）：** 单次、且 Y/Z 是具体去光环的真相，保留。
  - ❌ AI 腔：`断舍离是成年人的精神修行` —— Y 抽象拔高
  - ✅ 好句（保留）：`降薪是成年人的体面` —— Y 去光环的具体真相

**B. 小红书：**
```

- [ ] **Step 2: 验证插入**

Run: `rg -n "格言公式（humanizer #32|断舍离是成年人的精神修行|降薪是成年人的体面" references/platform-patterns.md`
Expected: 3 行命中。

- [ ] **Step 3: Commit**

```bash
git add references/platform-patterns.md
git commit -m "feat(platform): add #37 aphorism-formula sub-template (XX 是成年人的 YY)"
```

---

## Task 3: SKILL.md — 判别式 + 索引 #19b(改动 1 互锁)

**Files:**
- Modify: `SKILL.md`(§过度消毒反制·个人化表达 ~611 行;§51 条索引表 #19 行 ~793)

- [ ] **Step 1: 在 §过度消毒反制·个人化表达 那条后追加判别式(自带本体,非纯指针)**

定位 `SKILL.md` 这一行:

```markdown
- **个人化表达** — 主观判断 / 不完美句 / 半成形的想法 / 岔开的话:"我觉得""我不太能接受""说实话我也不知道",或括号内的随手补注。
```

改成(同一项末尾追加一句边界):

```markdown
- **个人化表达** — 主观判断 / 不完美句 / 半成形的想法 / 岔开的话:"我觉得""我不太能接受""说实话我也不知道",或括号内的随手补注。**边界:** `讲真 / 说实话` 当**开场钩子 + 后接套话** = #19b 改;接**不确定 / 复杂反应**(`说实话我也不知道`)= 毛边保留。
```

- [ ] **Step 2: 在索引表 #19 行下嵌入 #19b 子项(仿 #22a 在 #22 下的写法)**

定位 `SKILL.md` 索引表这一行(约 793 行):

```markdown
- **#19 空枢纽"需要注意的是 / 值得思考的是"** — 品牌文案不触发。
```

改成(加伪洞察关键词 + 缩进子项):

```markdown
- **#19 空枢纽"需要注意的是 / 值得思考的是 / 真正的问题是 / 核心在于 / 说到底 / 归根结底"** — 品牌文案不触发。`说到底 / 归根结底` 密度 + 落点门,别误杀口语。
  - **#19b 假坦诚开场（讲真 / 说实话当钩子）**(变体)— 开场钩子 + 后接套话才改;接不确定反应是毛边,保留。
```

- [ ] **Step 3: 验证两处插入**

Run: `rg -n "开场钩子 \+ 后接套话|#19b 假坦诚开场" SKILL.md`
Expected: 2 行命中(§过度消毒反制 边界句 + 索引子项)。

- [ ] **Step 4: Commit**

```bash
git add SKILL.md
git commit -m "feat(skill): inline #19b discriminator into always-loaded layer + index entry"
```

---

## Task 4: whitelists.md — 删 `说实话` gloss(B1 三向歧义)

**Files:**
- Modify: `references/whitelists.md`(第 40 行)

- [ ] **Step 1: 删 TBH 错译示例里的 `说实话`**

定位 `references/whitelists.md` 第 40 行:

```markdown
| **互联网速记** | `TLDR`、`BTW`、`FYI`、`TBH`、`IMO`、`IMHO`、`AKA`、`ETA`、`EOD`、`ASAP` | ❌ 太长不看 / 顺便说一下 / 仅供参考 / 说实话 |
```

改成(只删末尾 ` / 说实话`):

```markdown
| **互联网速记** | `TLDR`、`BTW`、`FYI`、`TBH`、`IMO`、`IMHO`、`AKA`、`ETA`、`EOD`、`ASAP` | ❌ 太长不看 / 顺便说一下 / 仅供参考 |
```

- [ ] **Step 2: 验证 `说实话` 不再出现在 whitelists.md**

Run: `rg -n "说实话" references/whitelists.md`
Expected: 无输出(exit 1 / 0 matches)。三向歧义消除。

- [ ] **Step 3: Commit**

```bash
git add references/whitelists.md
git commit -m "fix(whitelists): drop 说实话 gloss to kill three-way valence collision with #19b"
```

---

## Task 5: 版本号全量同步 0.7.1 → 0.8.0(M2 · 6 触点)

**Files:**
- Modify: `SKILL.md`(frontmatter);`README.md`(badge + `当前 v` 4 处)

- [ ] **Step 1: bump SKILL.md frontmatter**

定位 `SKILL.md` frontmatter:

```yaml
version: 0.7.1
```

改成:

```yaml
version: 0.8.0
```

- [ ] **Step 2: bump README badge(第 3 行)**

定位:

```markdown
[![Version](https://img.shields.io/badge/version-0.7.1-blue.svg)](https://github.com/LifelongLazyLearner/qu-ai-wei/releases)
```

改成:

```markdown
[![Version](https://img.shields.io/badge/version-0.8.0-blue.svg)](https://github.com/LifelongLazyLearner/qu-ai-wei/releases)
```

- [ ] **Step 3: bump README 全部 `当前 v0.7.1` / `（v0.7.1）`(第 10、24、56、203 行)**

逐处替换(4 处):
- 第 10 行 `**0.x 开发版（当前 v0.7.1）:**` → `（当前 v0.8.0）`
- 第 24 行 `当前 v0.7.1 的行为仍是` → `当前 v0.8.0 的行为仍是`
- 第 56 行 `### 一句话定位（v0.7.1）` → `### 一句话定位（v0.8.0）`
- 第 203 行表头 `qu-ai-wei（当前 v0.7.1）` → `qu-ai-wei（当前 v0.8.0）`

Run(批量,确认无遗漏):
```bash
rg -n "0\.7\.1" README.md SKILL.md
```
Expected: 只剩历史版本记录里的 `v0.7.1（2026-05-28）` 条目(那是历史,不改)。badge / 当前 v / frontmatter 全部已是 0.8.0。

- [ ] **Step 4: Commit**

```bash
git add SKILL.md README.md
git commit -m "chore: bump version 0.7.1 → 0.8.0 across sync touchpoints"
```

---

## Task 6: README humanizer 陈旧计数软化(M1 · 3 处)

**Files:**
- Modify: `README.md`(第 62、206、411 行)

- [ ] **Step 1: 软化第 62 行**

定位:

```markdown
本 skill 受 [`humanizer`](https://github.com/blader/humanizer) 启发（作者 Siqi Chen，MIT 协议，2025）。humanizer 官方定位是语言无关的工具，但那 29 条规则主要针对英文 —— Title Case、em dash、hyphenated pairs 都是英文特有现象。
```

改成(去掉精确数):

```markdown
本 skill 受 [`humanizer`](https://github.com/blader/humanizer) 启发（作者 Siqi Chen，MIT 协议，2025）。humanizer 官方定位是语言无关的工具，但它那一批规则主要针对英文 —— Title Case、em dash、hyphenated pairs 都是英文特有现象。
```

- [ ] **Step 2: 软化第 206 行(对比表「规则数量」行)**

定位:

```markdown
| 规则数量 | 29 类（参考 Wikipedia "Signs of AI writing"） | 51 类 + **顶层冲突仲裁顺序六级**
```

改成:

```markdown
| 规则数量 | 30 余条（参考 Wikipedia "Signs of AI writing"，随版本增减） | 51 类 + **顶层冲突仲裁顺序六级**
```

（行尾其余内容不变。）

- [ ] **Step 3: 软化第 411 行(致谢)**

定位:

```markdown
- [**`humanizer`**](https://github.com/blader/humanizer)（作者 **Siqi Chen**，MIT 协议，2025）— 去 AI 腔工具，官方**语言无关**定位，29 条规则实际针对英文写作。本 skill 的**结构、三遍工作流、语音校准、个性与灵魂章节、约 17 条模式概念**的直接来源。
```

改成:

```markdown
- [**`humanizer`**](https://github.com/blader/humanizer)（作者 **Siqi Chen**，MIT 协议，2025）— 去 AI 腔工具，官方**语言无关**定位，规则实际针对英文写作。本 skill 的**结构、三遍工作流、语音校准、个性与灵魂章节、约 17 条模式概念**的直接来源。
```

- [ ] **Step 4: 验证陈旧 29 不再指 humanizer 总数**

Run: `rg -n "29" README.md`
Expected: 仅剩第 283 行 `#26-#29`(规则编号区间,正确,不改)。humanizer 计数 3 处已无 `29`。

- [ ] **Step 5: Commit**

```bash
git add README.md
git commit -m "docs: de-magnet stale humanizer rule count (3 spots)"
```

---

## Task 7: CHANGELOG v0.8.0 + README 版本记录(m3)

**Files:**
- Modify: `CHANGELOG.md`(顶部 Unreleased → v0.8.0);`README.md`(§版本记录 最近更新)

- [ ] **Step 1: 把 CHANGELOG 的 `### Unreleased` 改名为 v0.8.0 并追加 3 模式条目**

定位 `CHANGELOG.md`:

```markdown
### Unreleased

- **新增离线 real-run 回归 harness。** `tests/eval-manifest.txt` 把 `tests/check-snapshot-smoke.sh` 里的语义断言整理成 line-oriented manifest;`tests/check-runs.sh <run-dir>` 可校验 `tests/after` anchor output,也可校验未来放在 `tests/runs/<version>-<model>/` 的真实 captured model outputs。
- **新增 `tests/runs/README.md`。** 说明 captured runs 的手工采集流程和必填 metadata header,明确不要把人工 anchor output 冒充成真实模型输出。
```

改成:

```markdown
### v0.8.0（2026-06-18） · 对照 humanizer 同步:补 3 条模式

参照 [humanizer](https://github.com/blader/humanizer) 较新规则,补 3 条中文有对应语境、此前覆盖不足的模式。全部折叠进既有规则,规则总数仍 51。

**新增 / 扩展模式:**

- **#19b 假坦诚开场(变体)。** `讲真 / 说实话 / 老实说` 当开场钩子 + 后接平铺套话 = AI 腔(三条全中才触发:位置 + 后接 + 密度)。接不确定 / 复杂反应的 `说实话我也不知道` 是毛边,保留。判别式同时写进 `SKILL.md` §过度消毒反制(必加载层),防漏检也防误杀。
- **#37 格言公式子模板。** 公众号 / 自媒体 `XX 是成年人的 YY` / `XX 是当代人的 ZZ` 把论点包装成可转发金句,密度 + 落点门触发;落点去光环具体则保留(`降薪是成年人的体面`)。
- **#19 伪洞察枢纽扩展。** `真正的问题是 / 核心在于 / 说到底 / 归根结底` 并入 #19;但 `说到底 / 归根结底` 是地道口语 marker,密度 + 落点门,单次落地不误杀。

**修正:**

- **`references/whitelists.md` 删 `TBH → 说实话` 错译 gloss。** 消除 `说实话` 在 whitelists / 毛边 / #19b 三处的相反语义歧义。
- **README humanizer 规则计数去精确数(3 处)。** 不再钉死会随 humanizer 发版过时的条数。

**回归:**

- 新增样本 `18-fake-candor-aphorism`,覆盖 #19b 假坦诚开场 + #37 格言公式 + 真诚 `说实话` 保护。

**离线 harness(并入本版):**

- **新增离线 real-run 回归 harness。** `tests/eval-manifest.txt` 把 `tests/check-snapshot-smoke.sh` 里的语义断言整理成 line-oriented manifest;`tests/check-runs.sh <run-dir>` 可校验 `tests/after` anchor output,也可校验未来放在 `tests/runs/<version>-<model>/` 的真实 captured model outputs。
- **新增 `tests/runs/README.md`。** 说明 captured runs 的手工采集流程和必填 metadata header,明确不要把人工 anchor output 冒充成真实模型输出。
```

- [ ] **Step 2: README §版本记录 最近更新 列表顶部加 v0.8.0 条目**

定位 `README.md`:

```markdown
最近更新：

- **v0.7.1（2026-05-28）**：**上下文减重,行为不变**。
```

在 `最近更新：` 与 `- **v0.7.1` 之间插入:

```markdown
- **v0.8.0（2026-06-18）**：**对照 [humanizer](https://github.com/blader/humanizer) 同步,补 3 条模式(全折叠进既有规则,总数仍 51)**。新增 **#19b 假坦诚开场**（`讲真 / 说实话` 当钩子 + 后接套话,判别式同时进 `SKILL.md` 必加载层防误杀真诚 `说实话`）、**#37 格言公式子模板**（`XX 是成年人的 YY`,密度 + 落点门）、**#19 伪洞察枢纽扩展**（`真正的问题是 / 核心在于 / 说到底`,口语 marker 不误杀）。修正 `whitelists.md` 的 `TBH → 说实话` 三向歧义;humanizer 规则计数去精确数。新增回归样本 `18-fake-candor-aphorism`。
```

- [ ] **Step 3: 验证 check-version-sync 要求的 CHANGELOG + README 条目格式**

Run:
```bash
rg -n "^### v0\.8\.0（" CHANGELOG.md && rg -n "^- \*\*v0\.8\.0（" README.md
```
Expected: CHANGELOG 命中 `### v0.8.0（`,README 命中 `- **v0.8.0（`。两者都是 `check-version-sync.sh` 的硬断言。

- [ ] **Step 4: Commit**

```bash
git add CHANGELOG.md README.md
git commit -m "docs: changelog v0.8.0 (roll Unreleased + 3 patterns) + README release note"
```

---

## Task 8: 回归样本 18 + smoke 断言(m2)

**Files:**
- Create: `tests/fixtures/18-fake-candor-aphorism.md`
- Create: `tests/after/18-output.md`
- Modify: `tests/check-snapshot-smoke.sh`(loop list + 18 block)
- Modify: `tests/eval-manifest.txt`([18] block)

- [ ] **Step 1: 建 fixture 输入(AI 腔:假坦诚开场 + 格言公式 + 一处真诚 `说实话` 待保护)**

Create `tests/fixtures/18-fake-candor-aphorism.md`:

```markdown
讲真，这套方法真的能改变你的人生。说实话，它会颠覆你对效率的认知。

自律是成年人最大的底气，坚持是当代人最稀缺的能力。说到底，这是认知的问题；归根结底，还是底层逻辑没想透。

老实说，我也是踩了无数坑才明白这个道理。不瞒你说，每个人都该尽早觉醒。
```

说明:全篇是公众号伪深度 + 假坦诚开场堆叠 + 格言公式 + 伪洞察枢纽,落点全抽象。注意末段 `说实话` 仍是钩子式(改);真诚保护的反例由 anchor 输出在「自审」里点明。

- [ ] **Step 2: 建 anchor 输出(演示正确改写 + 规则命中 + 毛边边界)**

Create `tests/after/18-output.md`:

```markdown
【门检】判断：AI 生成文本 | 证据:(1)`讲真 / 说实话 / 老实说 / 不瞒你说` 多段反复当开场钩子,后接平铺推销断言;(2)`自律是成年人最大的底气 / 坚持是当代人最稀缺的能力` 格言公式,换主语仍成立;(3)`说到底 / 归根结底` + 落点全是「认知 / 底层逻辑」抽象桶词,没有一条具体事实。

## 语体识别

自媒体 / 公众号伪深度腔。

## 规则命中

- **#19b 假坦诚开场** — `讲真，这套方法真的能改变你的人生。说实话，它会颠覆你对效率的认知。` + `老实说... / 不瞒你说...` 多段反复当开场钩子,后接平铺推销,三条(位置 + 后接 + 密度)全中。
- **#37 格言公式** — `自律是成年人最大的底气` / `坚持是当代人最稀缺的能力`,落点抽象拔高,换主语仍成立。
- **#19 伪洞察枢纽** — `说到底，这是认知的问题；归根结底，还是底层逻辑`,反复 + 落点抽象。

## 初稿

这套方法我自己用了半年,主要做两件事:每天固定早上写一小时,手机锁进抽屉。效率提升能不能复制我不确定,但至少我拖延少了。

## 终稿

这套方法我自己用了半年,就两件事:每天早上固定写一小时,手机锁进抽屉。

效率到底能不能复制,说实话我也不敢打包票 —— 我只知道自己拖延比以前少了。别人是不是适用,得自己试。

## 自审

### AI 不敢写测试

终稿保留「说实话我也不敢打包票」「我只知道自己拖延比以前少了」—— 承认不确定 + 私人经验。注意:这里的 `说实话` 接的是**不确定反应**(`不敢打包票`),属 #19b 不触发的毛边,**保留**;跟开头被删的钩子式 `说实话，它会颠覆你的认知`(后接推销断言)区分开。

### 整篇 craft 自检

去掉全部格言公式和伪洞察枢纽后,落到「早上写一小时 / 手机锁抽屉 / 拖延变少」三件具体事,信息没掉。

### 残留痕迹

无格言公式、无假坦诚钩子、无空枢纽。

## 打磨报告

- #19b:删 4 处假坦诚开场钩子(讲真 / 说实话 / 老实说 / 不瞒你说),保留 1 处接不确定反应的真诚 `说实话`。
- #37:删 2 句格言公式,换成具体动作。
- #19:删 `说到底 / 归根结底` 伪洞察枢纽。
- 毛边:保留「说实话我也不敢打包票」「自己拖延比以前少了」。
```

- [ ] **Step 3: 把 18-output.md 加入 smoke 基础检查 loop list**

定位 `tests/check-snapshot-smoke.sh` 的 `for file in ...` 列表末尾:

```bash
            tests/after/16-output.md \
            tests/after/17-output.md; do
```

改成:

```bash
            tests/after/16-output.md \
            tests/after/17-output.md \
            tests/after/18-output.md; do
```

- [ ] **Step 4: 在 smoke 脚本末尾(17 block 之后、`echo` 收尾之前)加 18 block**

在 16/17 block 之后追加(仿 11 block 的 rule-ref + 毛边保护风格):

```bash
# 18 — 假坦诚开场 #19b + 格言公式 #37 + 伪洞察枢纽 #19,且真诚 说实话 保护
if ! is_known_gap "18"; then
  rg -q "【门检】判断[:：]AI 生成文本" tests/after/18-output.md || {
    echo "18-output.md 门检未判为 AI 生成文本" >&2
    exit 1
  }
  rg -q "#19b" tests/after/18-output.md || {
    echo "18-output.md 未命中 #19b 假坦诚开场" >&2
    exit 1
  }
  rg -q "#37" tests/after/18-output.md || {
    echo "18-output.md 未命中 #37 格言公式" >&2
    exit 1
  }
  # 终稿必须保留接不确定反应的真诚 说实话(毛边,别误杀)
  extract_zhonggao tests/after/18-output.md | rg -q "说实话" || {
    echo "18-output.md 终稿未保留接不确定反应的真诚 说实话（#19b 不触发毛边）" >&2
    exit 1
  }
  # 终稿必须清掉格言公式
  if extract_zhonggao tests/after/18-output.md | rg -q "是成年人最大的底气|是当代人最稀缺的能力"; then
    echo "18-output.md 终稿仍含格言公式" >&2
    exit 1
  fi
fi
```

- [ ] **Step 5: eval-manifest.txt 加 [18] block**

定位 `tests/eval-manifest.txt` 末尾 `[17]` block 之后,追加:

```
[18]
require_anywhere=【门检】判断[:：]AI 生成文本
require_section=## 终稿
require_section=## 打磨报告
require_anywhere=#19b
require_anywhere=#37
require_final=说实话
forbid_final=是成年人最大的底气
forbid_final=是当代人最稀缺的能力
```

- [ ] **Step 6: 跑 smoke 测试,确认 18 全过**

Run: `bash tests/check-snapshot-smoke.sh`
Expected: 退出 0,无 `18-output.md ...` 报错。

- [ ] **Step 7: Commit**

```bash
git add tests/fixtures/18-fake-candor-aphorism.md tests/after/18-output.md tests/check-snapshot-smoke.sh tests/eval-manifest.txt
git commit -m "test: add fixture 18 covering #19b + #37 aphorism + 说实话 protection"
```

---

## Task 9: build-flat 同步 + 全量测试(最终验证)

**Files:**
- Modify(自动生成): `.cursorrules`、`WARP.md`

- [ ] **Step 1: 重新生成拍平版**

Run: `bash scripts/build-flat.sh`
Expected: 打印生成 `.cursorrules` / `WARP.md` 成功,无报错。

- [ ] **Step 2: 验证新内容已同步进拍平版**

Run:
```bash
rg -q "19b. 变体：假坦诚开场" .cursorrules && rg -q "格言公式（humanizer #32" .cursorrules && rg -q "19b. 变体：假坦诚开场" WARP.md && echo "FLAT SYNC OK"
```
Expected: 打印 `FLAT SYNC OK`。

- [ ] **Step 3: 验证 whitelists 删改也同步(说实话 不在拍平版 whitelists 区)**

Run: `rg -n "TBH" .cursorrules WARP.md`
Expected: TBH 行不再带 `/ 说实话`。

- [ ] **Step 4: 跑版本同步检查**

Run: `bash tests/check-version-sync.sh`
Expected: 打印 `version sync ok: 0.8.0`。

- [ ] **Step 5: 跑 snapshot smoke 全量**

Run: `bash tests/check-snapshot-smoke.sh`
Expected: 退出 0(全部样本含 18 通过)。

- [ ] **Step 6: 跑离线 run 校验(如存在 anchor 校验入口)**

Run: `bash tests/check-runs.sh tests/after 2>/dev/null || echo "check-runs 无 anchor 模式入口,跳过"`
Expected: 通过,或明确跳过提示(非硬失败)。

- [ ] **Step 7: Commit 拍平版**

```bash
git add .cursorrules WARP.md
git commit -m "build: regenerate flat .cursorrules / WARP.md for v0.8.0"
```

---

## Task 10: ship 前公开面提交门审(AGENTS.md 公开面 commit gate)

> 实现 commit 在本地已分步落成。**push / PR 前**,本仓 [AGENTS.md](../../../AGENTS.md) 的「公开面 commit gate」要求对**实际 diff**(不是 plan)再跑一次三位 reviewer,全部 sign off,verdict 三行写进最终 commit / PR body。

- [ ] **Step 1: 跑三位 reviewer over `git diff main...HEAD`**

并行(或顺序)跑 roster 三位:CEO / holistic、日常中文表达(adversarial)、Eng(skill effectiveness)。审的是**落地后的真实规则文字 + 测试 anchor**,重点:
- #19b / #37 / #19 的**实际措辞**有没有犯它们自己批的毛病(冗余、的的不休、过度修正)
- anchor 输出 `18-output.md` 的终稿是不是真·人话(别 anchor 本身就是 AI 腔)
- whitelists 删改没连带破坏表格对齐
- 计数仍 51、无悬空 `见 X` 指针

- [ ] **Step 2: 自动接力一次独立冷复审(CLAUDE.md)**

跑一个 fresh general-purpose cold reviewer over the diff,带前轮 findings 标「do not re-litigate」。

- [ ] **Step 3: 全绿后交 `/gstack-ship`**

交 ship 流程:它会跑测试 → review diff → 确认 0.8.0 → push → PR;PR body 含三行 verdict。merge / tag `v0.8.0` 等用户显式批准(记忆 feedback_tag_on_version_bump:版本升必跟 tag + push,在同一 ship 流里)。

---

## Self-Review(plan 对 spec 核查)

- **Spec coverage:** 改动 1(#19b)→ Task 1+3;改动 2(#37 格言)→ Task 2;改动 3(#19 扩展)→ Task 1+3;B1(whitelists)→ Task 4;M1(README 计数 3 处)→ Task 6;M2(版本 6 触点)→ Task 5+7;M3(格言不触发例)→ Task 2 已含;m1(#3 加载策略)→ 已在 spec 说明,无代码动作;m2(回归断言)→ Task 8;m3(Unreleased 处置)→ Task 7。全覆盖。
- **Placeholder scan:** 每个 code step 给了完整 before/after 内容块和确切 `rg` / `bash` 命令,无 TBD / 「类似上文」。
- **Type/命名一致:** 规则号 `#19b` / `#37` / `#19` 跨 Task 一致;fixture id `18`、文件名 `18-fake-candor-aphorism.md` / `18-output.md` 跨 Task 8/9 一致;`extract_zhonggao` 用的是 smoke 脚本既有函数(已验证存在)。

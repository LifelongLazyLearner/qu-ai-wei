# 去 AI 味（qu-ai-wei）

[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](https://github.com/LifelongLazyLearner/qu-ai-wei/releases/tag/v0.9.0)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skill-multilingual-red.svg)](./SKILL.md)
[![GitHub stars](https://img.shields.io/github/stars/LifelongLazyLearner/qu-ai-wei?style=social)](https://github.com/LifelongLazyLearner/qu-ai-wei/stargazers)

**按原语言重写现有文字，保留事实、逻辑、语体和作者声口。**

qu-ai-wei 在原文语言里重写现有文字。句子、段落、标题和长文顺序都可以动；事实、数字、引语、证据强度、格式和作者声口要留下。

简体中文和英语有各自的细查规则。繁體中文、西班牙语、日语等语言先走共同编辑内核，再按该语言、使用场景和作者样本校准。默认保持原语言。

[English](./readmes/README.en.md) · [日本語](./readmes/README.ja.md) · [한국어](./readmes/README.ko.md) · [Español](./readmes/README.es.md)

![qu-ai-wei 把套话较多的中文改成保留事实的自然表达](./assets/demo.gif)

## 安装

电脑上已有 Node.js 和 npm 时，运行：

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

安装后新建会话，或按所用工具的方式重新加载 skills。

## 直接用

```text
帮我去 AI 味，只输出终稿：

[粘贴文字]
```

英语也用同一个 skill：

```text
Use qu-ai-wei to humanize this in English. Keep every fact and return only the final text:

[paste text]
```

它默认按原语言改写。若任务还包含翻译，先完成翻译，再让 qu-ai-wei 处理译文。

## 示例

中文原文：

> 在快速变化的时代背景下，值得一提的是，本季度团队发布了 3 个版本，修复了 17 个线上问题，进一步赋能了组织协同。

终稿：

> 团队本季度发布了 3 个版本，修复了 17 个线上问题。

英语原文：

> It is important to note that the migration of 14 services was successfully completed by the platform team—ultimately resulting in two incidents being resolved.

终稿：

> The platform team migrated 14 services and resolved two incidents.

两处改写都让动作承担主干，数字和责任主体照旧。技术文、合同和学术文字继续使用各自的正式语体。

## 编辑顺序

处理时先记录事实、论证关系、说话人和受保护片段，再判断每段承担的职责。结构调整完成后，才处理连接词、抽象词、副词、被动和标点。

陈述句会写清必要的行动者、动作、对象和条件，及物动作保留宾语。目标语言允许省略主语时，指代仍需明确。技术文本进一步使用标准术语、中性表头和直接机制描述。

共同规则放在 [`cross-language-core.md`](./references/cross-language-core.md)。简体中文看 [`pattern-catalog.md`](./references/pattern-catalog.md)，英语看 [`english-patterns.md`](./references/english-patterns.md)。故事另查 [`narrative-patterns.md`](./references/narrative-patterns.md)；发布说明、PR、复盘和工单另查 [`professional-venues.md`](./references/professional-venues.md)；模型、数据、工程和实验文本另查 [`technical-writing.md`](./references/technical-writing.md)。

英文里的 `-ing` 尾部结构、冠词和 em dash 只在英语里判断，中文翻译腔留在中文层。各语言共同检查信息密度、无证据拔高、篇章复述、说话人漂移、引用错位和场域失配。

## 严格清理

用户要求彻底清理，或文本本身是 humanizer 的 README、SKILL.md、介绍页时，skill 会逐个检查副词、被动、破折号和表演性节奏。

保留项需要承担明确作用，例如时间、程度、证据、责任、语法或作者节奏。数量服从内容和语法。详见 [`strict-pass.md`](./references/strict-pass.md)。

## 交付方式

普通模式给出终稿和一份很短的打磨报告。把它嵌进其他流程时，可以要求“只输出终稿”。明确指定文件后，它也能直接修改文件里的 prose，并保留代码块、frontmatter、命令、路径、链接目标和机器可读数据。

文本已经自然时，原文就是终稿。作者只贴出一段真人文字而没有编辑指令时，skill 会先等授权。

## 职责

qu-ai-wei 负责已有文字的同语言改写。翻译、从零写作、纯校对、作者鉴定和模型识别各有自己的任务。终稿使用原文或用户授权材料中的事实、观点、经历和专业判断。

凭证请先替换为 `[REDACTED]`。涉及学校、期刊、平台或机构的 AI 使用规则时，以其披露和合规要求为准。

## 方法与许可

共同内核参考 [Wikipedia 的描述性目录](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)、[Humanizer](https://github.com/blader/humanizer)、[Humanizer-zh](https://github.com/op7418/Humanizer-zh)、[Sepia](https://github.com/Nanako0129/sepia)、[stop-slop](https://github.com/hardikpandya/stop-slop) 和 [claudish-to-english](https://github.com/gvzdv/claudish-to-english)。每条规则都要回到当前文本里验证；来源中的绝对禁令和单语言词表只作为候选信号。

项目采用 [MIT License](./LICENSE)。完整执行规则见 [`SKILL.md`](./SKILL.md)。

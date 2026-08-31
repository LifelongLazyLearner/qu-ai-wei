# 去 AI 味（qu-ai-wei）

[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](https://github.com/LifelongLazyLearner/qu-ai-wei/releases/tag/v0.9.0)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skill-multilingual-red.svg)](./SKILL.md)
[![GitHub stars](https://img.shields.io/github/stars/LifelongLazyLearner/qu-ai-wei?style=social)](https://github.com/LifelongLazyLearner/qu-ai-wei/stargazers)

qu-ai-wei 按原语言重写已有文字。它可以调整句子、段落、标题和长文顺序，同时保留事实、数字、引语、证据强度、格式和作者声口。

简体中文和英语有各自的细查规则。繁體中文、西班牙语、日语等语言使用共同编辑内核，再按该语言、使用场景和作者样本校准。

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

如果任务还包括翻译，请先完成翻译，再用 qu-ai-wei 处理译文。

## 示例

中文原文：

> 在快速变化的时代背景下，值得一提的是，本季度团队发布了 3 个版本，修复了 17 个线上问题，进一步赋能了组织协同。

终稿：

> 团队本季度发布了 3 个版本，修复了 17 个线上问题。

英语原文：

> It is important to note that the migration of 14 services was successfully completed by the platform team—ultimately resulting in two incidents being resolved.

终稿：

> The platform team migrated 14 services and resolved two incidents.

中文终稿保留季度、版本数和问题数。英文终稿保留服务数量、事故数量和平台团队的责任。技术文、合同和学术文字沿用各自的正式语体。

## 编辑顺序

qu-ai-wei 先记录事实、论证关系、说话人和受保护片段，再确认每段承担的职责。确定结构后，它才处理连接词、抽象词、副词、被动和标点。

qu-ai-wei 会在陈述句中写清必要的行动者、动作、对象和条件，并为及物动词保留宾语。目标语言允许省略主语时，指代仍需明确。技术文本进一步使用标准术语、中性表头和直接机制描述。

[`cross-language-core.md`](./references/cross-language-core.md) 收录共同规则。简体中文文本同时使用 [`pattern-catalog.md`](./references/pattern-catalog.md)，英语文本同时使用 [`english-patterns.md`](./references/english-patterns.md)。故事使用 [`narrative-patterns.md`](./references/narrative-patterns.md)。发布说明、PR、复盘和工单使用 [`professional-venues.md`](./references/professional-venues.md)。模型、数据、工程和实验文本使用 [`technical-writing.md`](./references/technical-writing.md)。

语言专层处理各自的语法习惯。英语层检查 `-ing` 尾部结构、冠词和 em dash，中文规则处理翻译腔。各语言共同检查信息密度、无证据拔高、篇章复述、说话人漂移、引用错位和场域失配。

## 严格清理

用户要求彻底清理，或文本本身是 humanizer 的 README、SKILL.md、介绍页时，qu-ai-wei 会逐个检查副词、被动、破折号和表演性节奏。

保留项需要承担明确作用，例如时间、程度、证据、责任、语法或作者节奏。内容和语法决定保留数量。[`strict-pass.md`](./references/strict-pass.md) 说明具体检查方法。

## 交付方式

普通模式返回终稿和简短打磨报告。用户可以在内嵌流程中要求“只输出终稿”。文件模式修改用户指定的 prose，并保留代码块、frontmatter、命令、路径、链接目标和机器可读数据。

文本已经自然时，原文就是终稿。用户只提供正文时，qu-ai-wei 会保留原文并询问是否改写。

## 职责

qu-ai-wei 负责已有文字的同语言改写。翻译、从零写作、纯校对、作者鉴定和模型识别属于独立任务。终稿使用原文或用户授权材料中的事实、观点、经历和专业判断。

用户分享文本前，应把凭证替换为 `[REDACTED]`。学校、期刊、平台和机构各自的披露与合规要求决定适用规则。

## 方法与许可

共同内核参考 [Wikipedia 的描述性目录](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)、[Humanizer](https://github.com/blader/humanizer)、[Humanizer-zh](https://github.com/op7418/Humanizer-zh)、[Sepia](https://github.com/Nanako0129/sepia)、[stop-slop](https://github.com/hardikpandya/stop-slop) 和 [claudish-to-english](https://github.com/gvzdv/claudish-to-english)。qu-ai-wei 会在当前文本中核对每条规则的证据。来源中的绝对禁令和单语言词表提供候选信号。

项目采用 [MIT License](./LICENSE)。[`SKILL.md`](./SKILL.md) 收录完整执行规则。

# 去 AI 味（qu-ai-wei）

[![Version](https://img.shields.io/github/v/release/LifelongLazyLearner/qu-ai-wei?label=version)](https://github.com/LifelongLazyLearner/qu-ai-wei/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Language](https://img.shields.io/badge/lang-简体中文-red.svg)](#)
[![GitHub stars](https://img.shields.io/github/stars/LifelongLazyLearner/qu-ai-wei?style=social)](https://github.com/LifelongLazyLearner/qu-ai-wei/stargazers)

语言：简体中文 | [English](./readmes/README.en.md) | [日本語](./readmes/README.ja.md) | [한국어](./readmes/README.ko.md) | [Español](./readmes/README.es.md)

> ⚠️ **0.x 开发版：** qu-ai-wei 仍在迭代，规则、分类、调用方式和输出格式都可能变动。最新发布版本见 [Releases](https://github.com/LifelongLazyLearner/qu-ai-wei/releases)；欢迎提 [issue](https://github.com/LifelongLazyLearner/qu-ai-wei/issues)、[discussion](https://github.com/LifelongLazyLearner/qu-ai-wei/discussions) 或 PR 反馈。

qu-ai-wei 用来修改 AI 生成的简体中文初稿，让文字读起来更自然，同时保留原来的事实、意思、正式程度和说话方式。

它会清理套话、机械结构、翻译腔和过度工整的表达，但不会：

- 替你翻译或从零写一篇文章。
- 补写原文没有的观点、经历和细节。
- 处理繁體中文。
- 帮你绕过学校、期刊或公司的 AI 使用规定。

## 看效果

![qu-ai-wei 把套话较多的简体中文改成保留事实的自然表达](./assets/demo.gif)

**原文：** 在快速变化的时代背景下，团队围绕提质增效开展了系统化实践。值得一提的是，本季度发布了 3 个版本，修复了 17 个线上问题，进一步赋能了组织协同。

**终稿：** 本季度，团队发布了 3 个版本，修复了 17 个线上问题。

这里删掉了没有增加信息的背景、强调和口号，没有补写原文未说明的措施或效果。更多边界案例见 [`references/examples.md`](./references/examples.md)。

## 安装

电脑上已有 Node.js 和 npm 时，运行：

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

`skills` 会自动检测本机支持的 AI 编程工具。

## 支持的工具

qu-ai-wei 使用开放的 Agent Skills 格式。Codex、Claude Code、Kimi Code CLI、Cursor 和 OpenCode 等工具可以直接加载同一份 `SKILL.md` 和 `references/`；`agents/openai.yaml` 只为 Codex / ChatGPT 提供展示名称、简介和默认提示词。

需要明确安装目标时，可以运行：

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei -a codex -a claude-code -a kimi-code-cli
```

## 使用

安装后，新建会话或按工具要求重新加载 skills，再直接说：

```text
帮我去 AI 味：

[粘贴简体中文]
```

qu-ai-wei 会先判断这段文字是否该改，然后给出初稿、自审、终稿和打磨报告。如果原文已经是自然的真人文本，它会停手；如果事实不清，或它无法判断这段文字该用在什么场合、该有多正式，它会先提问。

不要粘贴密码、API key 或其他凭证；检测到疑似凭证时，qu-ai-wei 会停止并要求先脱敏。

## 只要终稿

如果 qu-ai-wei 只是工作流中的一步，可以这样说：

```text
用 qu-ai-wei 改写下面的 PR 描述，只输出终稿正文：

[粘贴简体中文]
```

它仍会核对事实，并判断原文是否该改、该有多正式。能安全改写时，它只返回终稿；遇到真人文本或信息不足，仍会停手或提问。它不会因此获得写文件、commit、发布或发送内容的权限。

完整执行规则见 [`SKILL.md`](./SKILL.md)。方法受 [humanizer](https://github.com/blader/humanizer) 启发，中文翻译腔规则参考 [yage.ai](https://yage.ai/share/ai-chinese-translationese-20260418.html)。本项目采用 [MIT License](./LICENSE)。

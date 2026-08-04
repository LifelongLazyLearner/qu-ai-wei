# 去 AI 味（qu-ai-wei）

把已有的简体中文初稿改得更自然、准确，同时保留事实、原意、语体和原文声口。

它适合清理套话、机械结构、翻译腔和过度工整的 AI 表达；不负责翻译、新写文章、补观点和细节、改繁體中文，也不用于规避 AI 政策。

## 安装

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

`skills` 会自动检测本机支持的 agent。

## 使用

```text
帮我去 AI 味：

[粘贴简体中文]
```

普通模式会返回门检、初稿、自审、终稿和打磨报告。输入本来就是自然的真人文本时，它会停手；事实或语体边界不清时，它会先提问。

把它嵌入其他工作流、只需要终稿时：

```text
用 qu-ai-wei 改写下面的 PR 描述，只输出终稿正文：

[粘贴简体中文]
```

内嵌模式只改变输出形式，不放宽事实、语体和真人停手边界，也不增加写文件、commit、发布或发送权限。

完整执行规则见 [`SKILL.md`](./SKILL.md)。方法受 [humanizer](https://github.com/blader/humanizer) 启发，中文翻译腔规则参考 [yage.ai](https://yage.ai/share/ai-chinese-translationese-20260418.html)。本项目采用 [MIT License](./LICENSE)。

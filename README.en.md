# qu-ai-wei

[简体中文](./README.md) | English | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md)

qu-ai-wei is an agent skill for cleaning up AI-sounding writing in **Simplified Chinese**. It helps turn a Simplified Chinese draft from "obviously AI-written" into cleaner, more natural Chinese, while preserving facts and the original intent.

The canonical documentation is the [Simplified Chinese README](./README.md). This file is only a compact orientation for English readers.

## What It Is For

- Cleaning visible AI-writing traces in Simplified Chinese drafts, such as generic slogans, mechanical structure, over-polished phrasing, and translation-like Chinese.
- Lightly polishing wording, rhythm, and concrete expression when the source text already contains the needed information.
- Helping writers, editors, operators, product managers, students, and developers make everyday Simplified Chinese writing read less like a first AI draft.

## Hard Boundary

qu-ai-wei **only supports Simplified Chinese**.

It does not humanize English, Japanese, Korean, Spanish, Traditional Chinese, or mixed-language drafts. Traditional Chinese has different AI-writing patterns, word choices, and typography rules, so it needs a separate rule set.

It is also not a cheating or AI-detection bypass tool. Use it to improve writing you are responsible for, not to misrepresent authorship.

## What It Can and Cannot Do

It can:

- Remove obvious AI-sounding Chinese patterns.
- Keep the text's facts, intent, and broad register.
- Refuse or pause when the input looks like already-human writing, Traditional Chinese, legal/public-sector writing, or another case where rewriting would be risky.

It cannot:

- Invent original insight, interviews, details, or a stronger point of view.
- Turn weak source material into magazine-grade writing.
- Rewrite non-Simplified-Chinese text.

## Install

The same install script supports Cursor, Claude Code, OpenAI Codex CLI, OpenCode, Kiro, Factory Droid, Slate, and Hermes.

```bash
git clone https://github.com/LifelongLazyLearner/qu-ai-wei.git ~/qu-ai-wei
cd ~/qu-ai-wei

# Install for one agent
bash scripts/install-skill.sh --platform codex

# Or install for every supported agent
bash scripts/install-skill.sh --platform all
```

## Use

For non-Chinese-speaking users, the safest path is to call the skill explicitly and paste Simplified Chinese text:

```text
/qu-ai-wei

[paste Simplified Chinese text here]
```

You can also paste the body of [SKILL.md](./SKILL.md) into an AI model's custom instructions or system prompt. Skip the YAML frontmatter at the top.

## More

- Full docs: [README.md](./README.md)
- Skill rules: [SKILL.md](./SKILL.md)
- Supporting references: [references/](./references/)
- Changes: [CHANGELOG.md](./CHANGELOG.md)
- License: [MIT](./LICENSE)

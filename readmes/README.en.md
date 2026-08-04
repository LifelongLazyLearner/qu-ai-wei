# qu-ai-wei

[简体中文](../README.md) | English | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md)

> ⚠️ **0.x development release:** Rules, categories, and interfaces may still change. Feedback is welcome through [issues](https://github.com/LifelongLazyLearner/qu-ai-wei/issues), [discussions](https://github.com/LifelongLazyLearner/qu-ai-wei/discussions), or pull requests.

qu-ai-wei edits AI-generated drafts written in **Simplified Chinese** so they read more naturally while preserving facts, meaning, formality, and the source voice.

This README is available in several languages, but the skill itself edits prose whose primary language is Simplified Chinese. Necessary product names, technical terms, abbreviations, and other embedded terms are preserved.

## See It Work

![qu-ai-wei removes boilerplate while preserving the facts in a Simplified Chinese draft](../assets/demo.gif)

The example removes a generic opening, an unnecessary emphasis cue, and a slogan while preserving the two stated facts. See [`references/examples.md`](../references/examples.md) for the editing boundaries behind the example.

## Install

With Node.js and npm installed, run:

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

The external `skills` CLI detects supported AI coding tools installed on your computer.

## Use

After installation, start a new session or reload skills as required by your tool, then ask:

```text
/qu-ai-wei

[paste Simplified Chinese text]
```

By default, qu-ai-wei checks whether the text should be edited, produces a draft, reviews it, and returns a final version with a polishing report. It stops on already-human writing and asks when the intended context or level of formality is unclear.

## Final Text Only

When qu-ai-wei is one step inside a larger workflow, request embedded mode:

```text
Use qu-ai-wei to revise the following PR description. Return only the final text:

[paste Simplified Chinese text]
```

Embedded mode runs the same checks. When a safe revision is possible, it exposes only the final text; when the input is already human writing or lacks necessary context, it returns the source unchanged, asks a question, or reports the block. It does not grant permission to write files, commit, publish, or send anything.

## Boundaries

qu-ai-wei does not translate or write from scratch, invent missing opinions or details, rewrite a person's established voice, or help bypass AI-use policies.

See [SKILL.md](../SKILL.md) for the complete execution rules. The method was inspired by [humanizer](https://github.com/blader/humanizer), with Chinese translationese guidance informed by [yage.ai](https://yage.ai/share/ai-chinese-translationese-20260418.html). Licensed under the [MIT License](../LICENSE).

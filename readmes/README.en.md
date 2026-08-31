# qu-ai-wei

[简体中文](../README.md) · English · [日本語](./README.ja.md) · [한국어](./README.ko.md) · [Español](./README.es.md)

**Revise existing prose in the same language while preserving facts, logic, register, and voice.**

qu-ai-wei rewrites existing prose in the same language. It can reshape sentences, paragraphs, headings, and long-form structure while keeping the facts, numbers, quotations, strength of evidence, formatting, and the writer's voice.

Simplified Chinese and English have dedicated editing layers. Traditional Chinese, Spanish, Japanese, and other languages use a shared cross-language core, then follow the grammar, venue, and writer samples available for that language.

![qu-ai-wei removes boilerplate from Chinese prose while keeping the stated facts](../assets/demo.gif)

## Install

With Node.js and npm installed, run:

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

Start a new session after installation, or reload skills as required by your tool.

## Use it

```text
Use qu-ai-wei to humanize this in English. Keep every fact and return only the final text:

[paste text]
```

The source language stays in place by default. For a translated piece, translate first and run qu-ai-wei on the translation.

## What it pays attention to

The skill first records the facts, claims, speaker roles, quotations, code, paths, links, and machine-readable text that the revision must preserve. It then identifies the purpose of each paragraph. Surface edits come last.

The shared rules live in [`cross-language-core.md`](../references/cross-language-core.md). English adds its own checks for inflated verb phrases, trailing participles, hidden actors, nominalization, vocabulary clusters, hedging, and typography in [`english-patterns.md`](../references/english-patterns.md). Narrative and professional writing use separate venue guides.

This separation keeps English habits in English. An `-ing` phrase, article, passive construction, or em dash does not become a universal rule for every language.

## Strict pass

When the request calls for aggressive cleanup, or the text is a humanizer README or skill document, qu-ai-wei audits every adverb, passive construction, dash, and performative beat. The final text retains constructions that contribute time, degree, evidence, responsibility, grammar, rhythm, or the writer's voice.

## Output and scope

Normal mode returns the revised text with a short editing note. Embedded mode returns only the final text. File mode edits authorized prose while preserving code blocks, frontmatter, commands, identifiers, paths, link targets, and data.

qu-ai-wei handles same-language revision of existing prose. Translation, writing from scratch, typo-only proofreading, authorship claims, and model identification are separate jobs. Facts, opinions, experiences, and professional judgments in the result come from the source or material the user has authorized.

Replace credentials with `[REDACTED]` before sharing text. For school, journal, platform, or workplace AI rules, follow the applicable disclosure and compliance policy.

## Method and license

The editing core draws on [Wikipedia's descriptive catalogue](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [Humanizer](https://github.com/blader/humanizer), [Humanizer-zh](https://github.com/op7418/Humanizer-zh), [Sepia](https://github.com/Nanako0129/sepia), [stop-slop](https://github.com/hardikpandya/stop-slop), and [claudish-to-english](https://github.com/gvzdv/claudish-to-english). A rule applies when the current text contains matching evidence.

See [SKILL.md](../SKILL.md) for the execution rules. Licensed under the [MIT License](../LICENSE).

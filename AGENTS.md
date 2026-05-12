# Project rules for AI agents

> Conventions any AI coding agent working on this repo should follow.
> Format: [AGENTS.md](https://agents.md) — agent-agnostic, recognized by Claude Code, OpenAI Codex, Cursor, Aider, Windsurf, and others.

## Review gates

Before pushing any commit or posting any external reply (PR comment, discussion comment, issue comment) that affects the public face of this repository, run two adversarial reviewers **in parallel** using whatever sub-agent / sub-task / spawn-agent capability the harness exposes:

1. **CEO / holistic reviewer** — judges product, user, and reputation impact; flags scope problems and anything that would embarrass the project strategically.
2. **日常中文表达 expert (adversarial)** — judges Chinese authenticity, tone, and whether the change itself commits the patterns `SKILL.md` criticizes (冗余, 过度修正, 的的不休, 性 / 化堆叠, 翻译腔, etc.).

Do not commit, push, or post until **both** reviewers explicitly sign off. Address every "reject" or "needs changes" before retrying. Record both verdicts (one line each, final round) in the commit message body.

If the harness does not support spawning sub-agents, do this in two sequential passes within the main thread — but keep the personas, criteria, and sign-off requirement.

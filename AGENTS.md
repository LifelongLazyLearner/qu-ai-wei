# Project rules for AI agents

> Conventions any AI coding agent working on this repo should follow.
> Format: [AGENTS.md](https://agents.md) — agent-agnostic, recognized by Claude Code, OpenAI Codex, Cursor, Aider, Windsurf, and others.

## Review gates

### Adversarial reviewer roster

Use these three reviewers for every gate in this section:

1. **CEO / holistic reviewer** — judges product, user, and reputation impact; flags scope problems and anything that would embarrass the project strategically.
2. **日常中文表达 expert (adversarial)** — judges Chinese authenticity, tone, and whether the change itself commits the patterns `SKILL.md` criticizes (冗余, 过度修正, 的的不休, 性 / 化堆叠, 翻译腔, etc.).
3. **Engineering reviewer (skill effectiveness)** — judges the change as a piece of *agent-executable instruction*, not as prose. Specifically:
   - **Context economy** — does the change bloat `SKILL.md` or auto-loaded references beyond what an agent can hold attention to? Could each new sentence have been moved behind a `references/` pointer? Token-count the delta.
   - **Effectiveness** — would a real agent, reading the changed file cold, actually execute the rule? Do edge cases / examples cover the most common failure modes, or just add words?
   - **Hallucination risk** — does the change add rule numbers, file paths, brand anchors, or "see X" pointers that don't exist or don't load reliably? Could phrasing be over-interpreted by the agent (e.g., "always" / "never" / "must" applied to fuzzy categories)? Are examples concrete enough that the agent doesn't backfill imaginary ones?
   - **Loadability** — if the change adds a new `references/*.md`, verify it's picked up by `scripts/build-flat.sh` so the flat `.cursorrules` / `WARP.md` stay in sync. Stale references = silent regressions.

### Plan finalization gate

Before presenting any final implementation plan, `<proposed_plan>` block, design spec, execution checklist, or saved plan as ready, run all three reviewers from the roster in parallel using whatever sub-agent / sub-task / spawn-agent capability the harness exposes.

Do not finalize the plan, present it as approved, save it as approved, or hand it off for implementation until **all three** reviewers explicitly sign off. Address every "reject" or "needs changes" verdict before retrying, then rerun the reviewers until all three sign off.

When presenting the finalized plan, include the final three reviewer verdict lines. If the plan is saved outside chat, include those verdict lines in the saved plan or link/name the saved review artifact.

### Public-face commit and reply gate

Before pushing any commit or posting any external reply (PR comment, discussion comment, issue comment) that affects the public face of this repository, run all three reviewers from the roster in parallel using whatever sub-agent / sub-task / spawn-agent capability the harness exposes.

Do not commit, push, or post until **all three** reviewers explicitly sign off. Address every "reject" or "needs changes" before retrying. Record all three verdicts (one line each, final round) in the commit message body.

If the harness does not support spawning sub-agents, do this in three sequential passes within the main thread — but keep the personas, criteria, and sign-off requirement.

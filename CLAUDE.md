# Project rules for Claude

## Review gates

Before pushing any commit or posting any external reply (PR comment, discussion comment, issue comment) that affects the public face of this repository, run two adversarial reviewers in parallel via the `Agent` tool:

1. **CEO / holistic reviewer** — judges product, user, and reputation impact; flags scope problems and anything that would embarrass the project strategically.
2. **日常中文表达 expert (adversarial)** — judges Chinese authenticity, tone, and whether the change itself commits the patterns SKILL.md criticizes (冗余, 过度修正, 的的不休, 性/化堆叠, 翻译腔, etc.).

Do not commit, push, or post until **both** reviewers explicitly sign off. Address every "reject" or "needs changes" before retrying. Record both verdicts (one line each, final round) in the commit message body.

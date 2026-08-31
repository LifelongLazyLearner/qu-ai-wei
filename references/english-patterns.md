# English editing patterns

Read this file when the prose being edited is primarily English. It adds English grammar, vocabulary, and typography checks to the cross-language core. Treat every pattern as an editing clue tied to the current passage; authorship claims and universal bans sit outside this layer.

## Use order

1. Preserve every claim, qualifier, name, number, date, quotation, citation, identifier, and speaker role.
2. Fix content and paragraph structure with `cross-language-core.md` before touching surface wording.
3. Check the English-specific groups below one at a time.
4. Read the result aloud, then compare it with the source ledger. A smoother sentence that changes a claim is a failed edit.

## 1. Inflated verb phrases instead of simple verbs

Watch for clusters of `serves as`, `stands as`, `represents`, `boasts`, `features`, and `offers` where `is`, `has`, or a direct action would say the same thing.

- Keep the longer verb when it carries a real distinction: a room can *serve as* a clinic without being one permanently.
- Preserve the distinction between a temporary function and a permanent identity.
- Prefer the plain verb only when the meaning is genuinely equivalent.

## 2. Trailing participial pseudo-analysis

An English sentence may state a fact, then attach an `-ing` phrase that merely declares significance: `highlighting`, `underscoring`, `showcasing`, `reflecting`, `ensuring`, `fostering`.

- Delete the tail when it repeats or inflates the main clause.
- Turn it into a finite clause when it states a separate, supported action or consequence. A shared subject can govern several complete predicates.
- Keep an ordinary participial clause when simultaneity or manner matters and the construction matches the writer's voice. Separate actions normally use finite clauses.

## 3. Hidden actors and false agency

Passive voice and abstract subjects can hide responsibility, but English also uses them legitimately.

- Name the actor when the source identifies one and the reader needs it.
- Keep the passive when the actor is unknown, irrelevant, deliberately withheld, or the object is the established topic.
- A new actor requires source support. Recast `the decision emerged`, `the data suggests`, or `the market changed` only when the source supplies a more precise actor or interpretation.
- Protect conventional technical phrases, scientific register, legal drafting, and incident-report blamelessness.

## 4. Abstract wrappers and nominalization stacks

Watch for repeated shapes such as `a sense of`, `the weight of`, `a mix of X and Y`, and sentences whose subjects are long chains of `-tion`, `-ment`, or `-ness` nouns.

- Restore a direct verb or concrete object when the wrapper adds no distinction.
- Keep established technical terms and real paired concepts.
- Sensory detail belongs in the revision only when it already exists in the source or authorized material.

## 5. Template contrasts and completeness rituals

English AI-like prose often clusters around:

- `not only X but also Y`, `it is not X; it is Y`, `more than X`, or clipped endings such as `no guessing`;
- forced groups of three;
- `from X to Y` when X and Y do not form a real range;
- staged candor such as `Honestly?`, `Here's the thing`, or `Let's be real`;
- announced insight such as `Let's dive in`, `Here's what you need to know`, or `At its core`;
- fake objections and disposable alternatives that no one raised;
- rows of dramatic fragments that all try to be the final line.

Rewrite the function behind the watched phrase. When X is only a vague foil for Y, state Y directly. This applies whether the foil comes first or last: `This was not merely procedural; it clarified our roles` and `It clarified our roles; it wasn't just procedural` both become `It clarified our roles`. Keep real correction, contrast, scope exclusion, design alternatives, deliberate rhythm, and quotations. Let the content determine the number of list items.

## 6. Vocabulary clusters

Potential cluster words include `delve`, `underscore`, `tapestry`, `testament`, `landscape` used abstractly, `pivotal`, `vibrant`, `seamless`, `robust`, `transformative`, `multifaceted`, `navigate`, `foster`, `harness`, and `resonate`.

- A finding requires a cluster or a clear loss of concrete action; a single word stays a candidate.
- Keep correct technical uses such as a robust estimator, feature gating, a network landscape, or a quoted slogan.
- Replace the sentence's structure and claim; thesaurus swaps alone leave the pattern intact.

## 7. Hedging, adverbs, and conversational particles

- Collapse stacked qualifiers that express the same uncertainty; keep the one that matches the evidence.
- In the default path, keep adverbs that carry time, degree, stance, or manner. In the strict pass, inspect every adverb and remove each one that only intensifies, softens, or performs sincerity.
- Remove `successfully` when the completed verb already states the result and the adverb adds no separate fact.
- Contractions, discourse particles, first person, slang, profanity, and rhetorical questions come from the author sample or venue.
- Repeated `seems to`, `appears to`, or `could potentially` can be simplified when the source supports a stronger statement; otherwise the uncertainty stays.

## 8. English typography and formatting

- Em dashes are common human punctuation. The default path changes them only when they cluster with a repeated sales-like rhythm, violate the target style guide, or conflict with the writer sample. The strict pass makes every dash justify its function and removes the rest.
- Curly and straight quotation marks follow formatting convention and the target publication.
- Title Case, sentence case, serial commas, and heading depth follow the venue's style guide.
- Bold mini-headings, emoji, and vertical lists are problems only when they add decoration without navigation or comparison value.
- Hyphenate compounds according to grammar and house style. Valid pre-nominal hyphens remain intact even when several appear.

## 9. English fluency check

Read each changed sentence as English rather than as a transformation rule:

- Does the subject arrive early enough to follow?
- Does a pronoun still point to the same person or thing?
- Did a rewrite change tense, modality, article meaning, countability, or scope?
- Is a plain word more precise, or merely less formal?
- Does the sentence fit the publication and the writer rather than a generic casual voice?

If the answer is uncertain, keep the source wording or make a narrower edit.

## Sources and limits

This layer adapts the current [Humanizer](https://github.com/blader/humanizer) pattern set, the Chinese translation project [Humanizer-zh](https://github.com/op7418/Humanizer-zh), the high-recall structural checks in [stop-slop](https://github.com/hardikpandya/stop-slop), and the same-language preservation contract in [claudish-to-english](https://github.com/gvzdv/claudish-to-english). It also uses English style findings summarized by [Sepia](https://github.com/Nanako0129/sepia). Stop-slop's absolute rules are retained as an optional high-recall audit in `strict-pass.md`; the protection check still decides whether each occurrence changes.

---
name: oiticica-style-qualities
description: Audit a single English passage or compare parallel drafts using Oiticica's six essential style qualities and their component skills.
---

# Oiticica Style Qualities

Audit every supplied passage. When the user supplies parallel drafts, audit each independently before comparing them.

Source concept: Style has six essential qualities: correctness, concision, clarity, harmony, originality, and vigor.

## Component Skills

Load and apply all six component skills for every audit. These `$` handles are explicit skill invocations, not labels:

- `$oiticica-correctness`
- `$oiticica-concision`
- `$oiticica-clarity`
- `$oiticica-harmony`
- `$oiticica-originality`
- `$oiticica-vigor`

Use each component skill's rules and objective rubric. Do not substitute an unaided general definition of the quality. If the runtime cannot resolve nested skill invocations, use the decision boundaries below rather than omitting a quality.

## Router Mode

When the general `oiticica-style` router invokes this skill as a pipeline stage, apply all six component skills but defer final response shape, total length, and revision decisions to the router. Return the six evidenced decisions to the router; do not emit this skill's standalone audit format.

## Decisions

Give every quality a final `Pass` or `Fail` decision with quoted or otherwise concrete evidence.

- **Correctness**: grammar, spelling, usage, idiom, and punctuation fit the intended English register.
- **Concision**: no word, clause, or example can be removed, and no circumlocution can be replaced by a shorter direct noun or verb, without harming another quality.
- **Clarity**: actor, action, object, attachment, order, and consequence permit one intended reading.
- **Harmony**: sound and cadence support meaning without an accidental collision or stumble.
- **Originality**: exact observation and relation, rather than stock phrasing or borrowed effect, carry the passage.
- **Vigor**: concision and clarity pass, and the strongest actor, force, and main verb remain visible without inflation.

Judge all six; do not let one excuse failure in another. Correctness is the floor, not the finish. Shortness alone does not establish concision, novelty does not establish originality, and an active voice alone does not establish vigor.

Keep the decisions specific. Preserve historically accepted punctuation and usage in a sourced historical quotation; do not fail correctness merely because current convention differs. A grammatical construction does not fail correctness merely because it is awkward; judge its sound under harmony. For concision, require deletion or a shorter direct substitution to preserve logic, tense, necessary emphasis, and voice. When Concision fails, state the exact deletion or substitution and the resulting local phrase. A light verb plus an action noun fails concision when the direct cognate verb preserves the relation: for example, `make preparations` becomes `prepare`. The same construction fails vigor when it moves the main action out of the verb. A modifier that only repeats meaning already entailed by its governing verb fails concision unless the passage supplies evidence of deliberate emphasis. Vigor must `Fail` whenever Concision or Clarity fails, even when the actors and verbs are otherwise strong.

## Response

Keep each audit under 220 words. For each passage or draft, use exactly one line per quality in this form: `Name — Pass/Fail: evidence.` List Correctness, Concision, Clarity, Harmony, Originality, and Vigor in that order. State the final decision directly; do not narrate deliberation or retract a decision.

For one passage, give a one-sentence quality-based `Verdict`. For parallel drafts, complete the same six-quality audit for each draft, then recommend the stronger draft with at least one explicit paired difference: name the corresponding construction or relation in both drafts and explain the changed effect. Do not present a rewrite unless asked.

If revision was not requested, write `Revision: Not requested.` If the prompt says `revise only if needed` and all six qualities pass, write `Revision: No revision needed.`

Source boundaries and quotation locations are recorded in `references/notes.md`.

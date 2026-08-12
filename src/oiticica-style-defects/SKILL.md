---
name: oiticica-style-defects
description: Audit a single English passage or compare parallel drafts using Oiticica's six essential style defects, with fixed grades and evidence.
---

# Oiticica Style Defects

Audit every supplied passage. When the user supplies parallel drafts, audit each independently before comparing them.

Source concept: Style has six essential defects corresponding to its six qualities: impurity, prolixity, obscurity, disharmony, banality, and weakness.

## Decisions

Apply all six. A matching test requires at least `Minor`, even when the prose remains intelligible.

- **Impurity**: a form violates its grammatical role or governing usage. Exempt historically attested spelling, capitalization, and punctuation, deliberate dialect, and editorial notation.
- **Prolixity**: words can be deleted, without substitution, while preserving logic, tense, necessary emphasis, and voice. A shorter rewording is not evidence. An emphatic auxiliary is `None` when deleting it weakens declared emphasis, solemnity, or performative force.
- **Obscurity**: two contextually coherent referents, attachments, or comparison terms survive the whole supplied passage and materially change the relation asserted, or a deictic's discourse role is unclear. Name the readings. Ordinary contextual deixis such as `this place`, `now`, or `before` is `None` when its role is clear even if the quotation does not name the real-world place or time. A choice between a discourse span and that span's named subject is also `None` when it leaves the asserted relation unchanged. A fleeting syntactic possibility that the passage resolves, a semantically implausible referent, or a bare dictionary sense is `None`.
- **Disharmony**: immediately neighboring identical word tokens, or another accidental phonetic collision that distracts when read aloud, even if the construction is grammatical. A repeated word or phrase later in the passage is not adjacent. Repeated content words, parallel coordination, and a deliberate semantic echo are `None` unless they independently create a separate phonetic collision; describe that sound rather than calling the repetition adjacent.
- **Banality**: stock phrasing, generic praise, or borrowed imagery supplies the main effect. A conventional transition, idiom, or functional connective is `None` when it merely carries the logic, even if it is familiar or dispensable; familiarity alone does not satisfy the main-effect test.
- **Weakness**: passive construction, nominalization, abstraction, or inflation buries the main actor, movement, or force. Quote the grammatical construction and name what it buries. A finite `be` auxiliary plus a past participle can supply passive evidence when its subject receives an action, especially in an expression of movement; an absent actor strengthens but is not required for that diagnosis. A passive is `None` when attention properly belongs on its receiver and the actor is visible or immaterial. `Be` plus an `-ing` present participle is progressive, not passive. An active infinitive remains active when its agent is implicit or its recipient is explicit. A copular scene-setting frame such as `It was ...` is stative and therefore `None` when it buries no actor, action, or movement. Gentle tone, an unnamed semantic instigator alone, or the mere possibility of a stronger recast is also `None`. Do not double-count an absent actor as obscurity unless the missing identity is necessary to understand the relation or permits competing readings.

Grade `None` for no evidence, `Minor` for a local defect, and `Major` for a repeated or controlling defect. Quote the evidence and explain why it matches the decision. Assign one textual cause to one primary defect. Do not use prolixity as a fallback: deleting an unclear essential relation is obscurity, repairing sound is disharmony, and making passive action active is weakness. Do not grade a conventional functional transition as banality unless it supplies the passage's main effect.

Do not presume sourced, famous, literary, civic, sacred, quoted, grammatical, or intelligible prose is defect-free. Judge literal translations as English unless source-language structure is explicitly required. Preserve quotations; do not rewrite unless asked.

Source boundaries and quotation locations are recorded in `references/notes.md`.

## Response

Keep each audit under 220 words. For each passage or draft, use exactly one line per defect in this form: `Name — Grade: evidence.` List Impurity, Prolixity, Obscurity, Disharmony, Banality, and Weakness in that order. State the final grade directly; do not narrate deliberation or retract a grade. Then give a one-sentence defect-based `Verdict`, up to three brief evidenced `Follow-up` handles, and `Revision`. A minimal local contrast may prove a diagnosis; do not present a revised passage unless asked.

Map the six defects respectively to `oiticica-correctness`, `oiticica-concision`, `oiticica-ambiguity` or `oiticica-clarity`, `oiticica-harmony`, `oiticica-originality`, and `oiticica-vigor`. Do not run them unless asked.

If revision was not requested, write `Revision: Not requested.` If the prompt says `revise only if needed` and all grades are `None`, write `Revision: No revision needed.`

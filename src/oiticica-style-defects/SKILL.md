---
name: oiticica-style-defects
description: Audit or compare English drafts using Oiticica's six essential style defects, with fixed severity grades, concrete evidence, and narrow follow-up handles.
---

# Oiticica Style Defects

Use one fixed audit for a single passage or for parallel drafts. Diagnose defects; do not replace the adaptive routing performed by `oiticica-style`.

Source concept: Style has six essential defects corresponding to its six qualities: impurity, prolixity, obscurity, disharmony, banality, and weakness.

## Six Defects

- **Impurity** damages correctness through unintended faults in grammar, spelling, idiom, punctuation, or word form. Preserve deliberate dialect and historical quotation.
- **Prolixity** damages concision through removable words, clauses, repetition, circumlocution, or avoidable subordination.
- **Obscurity** damages clarity by hiding the actor, action, attachment, order, condition, or consequence, or by permitting unintended readings.
- **Disharmony** damages readable sound or cadence through a demonstrable collision, distracting repetition, or monotonous rhythm.
- **Banality** damages originality when stock phrasing, generic praise, or borrowed imagery carries the main effect.
- **Weakness** damages vigor when passive construction, nominalization, abstraction, or inflation buries the main actor or force.

## Audit Rules

- Inspect all six defects for every passage or draft, using the same evidence threshold when comparing parallel work.
- Report only defects supported by a quoted word, phrase, sentence relation, or audible pattern.
- Grade each defect as None, Minor, or Major according to its effect and recurrence.
- Do not treat a possible shorter wording as prolixity unless the original repeats meaning or can lose words without losing logic, emphasis, or voice.
- When a pronoun, modifier, attachment, or scope permits more than one plausible reading, name the competing readings, grade obscurity above None, and use oiticica-ambiguity rather than generic clarity as the follow-up.
- Recommend a narrower Oiticica skill only when it would add a specific diagnosis or repair.

Use these grades:

- `None`: no concrete evidence of the defect.
- `Minor`: a local defect that can be repaired without changing the passage's structure or meaning.
- `Major`: a repeated or controlling defect that impedes meaning, force, or comparison.

Do not infer a defect from personal preference, sentence length alone, or a feature deliberately required by the genre or voice.

## Output Shape

For each passage or draft, use:

```markdown
<passage or draft label>:
- Impurity — <None|Minor|Major>: <evidence or "No concrete evidence.">
- Prolixity — <None|Minor|Major>: <evidence or "No concrete evidence.">
- Obscurity — <None|Minor|Major>: <evidence or "No concrete evidence.">
- Disharmony — <None|Minor|Major>: <evidence or "No concrete evidence.">
- Banality — <None|Minor|Major>: <evidence or "No concrete evidence.">
- Weakness — <None|Minor|Major>: <evidence or "No concrete evidence.">

Verdict:
<strongest draft or overall diagnosis, justified by defect severity>

Follow-up:
- <zero to three narrower oiticica-* skills, each tied to an evidenced defect>

Revision:
<revision only when requested, otherwise "Not requested.">
```

When the prompt says `revise only if needed` and every grade is `None`, write `Revision: No revision needed.`

## Objective Rubric

- All six defects receive an explicit grade.
- Every non-None grade cites concrete textual evidence.
- The comparison applies one standard to every draft and explains the verdict.
- No rewrite appears unless the user requests one.

Pass only when every applicable check passes. Correctness and intelligibility defects outweigh decorative polish in the verdict.

## Follow-up Boundary

- Route impurity to `oiticica-correctness` or the precise grammar, spelling, word-form, or foreignism skill.
- Route prolixity to `oiticica-concision` or `oiticica-accumulation`.
- Route competing referents, attachments, or scopes to `oiticica-ambiguity`; route other obscurity to `oiticica-clarity`, `oiticica-anacoluthon`, `oiticica-brachylogy`, `oiticica-precision`, `oiticica-comma`, or `oiticica-semicolon`.
- Route disharmony to `oiticica-harmony`, `oiticica-cacophony`, `oiticica-assonance`, `oiticica-alliteration`, `oiticica-hiatus`, `oiticica-meter`, or `oiticica-prose-rhythm`.
- Route banality to `oiticica-originality`, `oiticica-description`, `oiticica-precision`, or `oiticica-image`.
- Route weakness to `oiticica-vigor`, `oiticica-concision`, `oiticica-clarity`, `oiticica-inversion`, or `oiticica-antithesis`.

Recommend only the smallest useful set. Do not run the narrower skills unless the user requests deeper diagnosis or repair.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. Preserve supplied source-model text exactly unless the user asks for a revision.

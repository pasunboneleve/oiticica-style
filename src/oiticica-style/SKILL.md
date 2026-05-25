---
name: oiticica-style
description: Orchestrate Oiticica principle skills for English prose by diagnosing genre, fixing defects, and applying qualities.
---

# Oiticica Style

Use this skill when the user asks for general Oiticica-style review or revision and has not named a narrower Oiticica skill.

This skill is a router. It chooses the relevant existing principle skills and applies only the ones the passage needs. Do not copy every principle into the answer.

## Pipeline

Work in this order:

1. Identify genre.
2. Eliminate defects.
3. Apply qualities.

Stop early when the passage needs only a narrow correction.

## Identify genre

Choose one genre only when it clearly controls the passage:

- Use `oiticica-description` when the passage presents aspects of an object, place, person, scene, or state.
- Use `oiticica-narration` when the passage presents facts, events, or episodes in time.
- Use `oiticica-dissertation` when the passage presents opinions, claims, reasons, or conclusions.

If no genre clearly controls the passage, write `Genre: None` and continue with the concrete fault.

## Eliminate defects

Correctness and intelligibility come before polish:

- Use `oiticica-correctness`, `oiticica-spelling`, `oiticica-solecism`, `oiticica-word-formation`, or `oiticica-confused-words` when grammar, spelling, syntax, word form, or word choice blocks the sentence.
- Use `oiticica-foreignism`, `oiticica-latinism`, `oiticica-gallicism`, `oiticica-archaism`, or `oiticica-neologism` only when register, imported construction, or word novelty is the fault.
- Use `oiticica-ambiguity`, `oiticica-anacoluthon`, `oiticica-accumulation`, `oiticica-brachylogy`, `oiticica-precision`, `oiticica-comma`, or `oiticica-semicolon` when structure, reference, punctuation, or exactness prevents one clear reading.

Do not polish sound, imagery, or force before these faults are fixed.

## Apply qualities

After meaning is stable, use the smallest set of quality skills:

- Use `oiticica-style-qualities` for a broad six-quality check.
- Use `oiticica-concision` when words, clauses, or examples can be removed without loss.
- Use `oiticica-clarity` when subject, action, object, condition, or consequence is not visible.
- Use `oiticica-harmony` or `oiticica-prose-rhythm` when cadence or sentence movement matters.
- Use `oiticica-originality` when the passage depends on stock phrases, borrowed images, or generic observation.
- Use `oiticica-vigor` when the actor, force, or main verb is buried.

Use sound and figure skills only when the text demands them:

- `oiticica-cacophony`, `oiticica-assonance`, `oiticica-alliteration`, `oiticica-hiatus`, or `oiticica-meter` for audible local problems or deliberate prosody.
- `oiticica-image`, `oiticica-inversion`, or `oiticica-antithesis` for imagery, word order, or contrast.

## Selection rules

- Select one to four skills unless the user asks for a full audit.
- If the user names a specific Oiticica skill, use that skill and add only necessary correctness fixes.
- If the passage is already strong, preserve it and name the checks it passes.
- Do not invent faults in clear, correct, specific prose.
- Do not treat sentence complexity as a fault by itself. A complex sentence passes when its actor, action, order, and consequence are explicit.
- Do not use speculative polish phrases such as `could be clearer`, `could be made more explicit`, or `for improved clarity` unless you name the exact missing actor, ambiguous attachment, wrong order, or broken relation.
- Do not route to sound, meter, image, inversion, or antithesis unless that feature is present and relevant.
- Do not turn a practical rewrite request into a long taxonomy.
- For generic description with words such as `nice`, `impressive`, `beautiful`, `great`, `pleasant`, or `atmosphere`, select `oiticica-description` plus `oiticica-precision` or `oiticica-originality`.
- For event sequence, causal order, condition before effect, or consequence before cause, select `oiticica-narration` plus `oiticica-clarity`; do not label the sequence issue as correctness unless grammar is actually wrong.
- For ambiguous attachment, select `oiticica-ambiguity` even when clarity or narration also applies. Name both possible readings, and if the user gives no intended reading, choose one plausible reading in the revision and make the choice explicit. In the revision, repeat the intended actor or object by name when a pronoun would preserve the ambiguity.
- When the user says `revise only if needed`, revise only when a selected check fails. If selected checks pass, write `Revision: No revision needed.` A passing `oiticica-clarity`, `oiticica-concision`, or `oiticica-vigor` check is evidence to preserve, not permission to paraphrase.
- For `revise only if needed`, do not treat smoother flow, streamlining, or a possible shorter wording as a need. Name the passing relation and stop unless there is a concrete defect in correctness, ambiguity, precision, order, force, or concision.
- Treat compact causal prose as already strong when the actor, action order, and consequence are explicit. Do not replace a shorter causal link with a longer paraphrase unless it fixes a concrete fault in correctness, clarity, or force.

## Output shape

For general review and rewrite, use:

```markdown
Genre:
<selected genre skill or None>

Selected skills:
- <skill>: <why this skill applies>

Diagnosis:
- <skill>: <specific fault or passing relation>

Revision:
<revised passage, or "No revision needed.">

Checks:
- <skill check>: Pass/Fail
```

For a requested audit, add more selected skills but keep each diagnosis concrete.

For a requested single-skill review, use that skill's own review shape.

## Finish

Before answering, verify that:

- every selected skill is named exactly;
- every selected skill has evidence in the passage;
- all blocking defects are handled before qualities;
- the revision preserves the original meaning, facts, and intended register.

Source notes live in `references/notes.md`.

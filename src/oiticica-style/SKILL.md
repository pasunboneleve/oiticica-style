---
name: oiticica-style
description: Orchestrate Oiticica aggregate audits for English prose by identifying genre, eliminating defects, then applying qualities.
---

# Oiticica Style

Use this router for a general Oiticica review or revision. It owns the final response and composes the aggregate audits; do not copy their standalone response shapes.

## Narrow Requests

If the user explicitly names a narrower Oiticica skill, use that skill and add only necessary correctness fixes. Do not run the three aggregate stages unless the user also requests a general or full audit.

## Pipeline

For every general review, work in this order:

1. Identify one controlling genre when present.
2. Invoke `$oiticica-style-defects` on the supplied passage.
3. Invoke `$oiticica-clarity-faults` on the supplied passage to identify the specific cause of any clarity failure.
4. When revision is requested, repair every evidenced defect and clarity fault before polishing. Invoke every required narrower follow-up skill by its `$oiticica-*` handle before drafting the revision; naming a handle in the response is not an invocation. Component skills already loaded by `$oiticica-clarity-faults` satisfy this requirement.
5. Invoke `$oiticica-style-qualities` after the meaning is stable. For a revision, judge the repaired passage; for an audit without revision, judge the supplied passage.
6. Preserve the passage when all broad defects and clarity faults are `None` and all qualities pass.

Do not skip the quality stage merely because the defect stage found no defect. Do not let quality polish conceal an unresolved defect.

## Genre

Choose one genre only when it clearly controls the passage:

- `oiticica-description` for aspects of an object, place, person, scene, or state;
- `oiticica-narration` for facts, events, or episodes in time;
- `oiticica-dissertation` for opinions, claims, reasons, or conclusions.

Invoke only the selected genre skill, prefixing its exact name with `$` at invocation time. If none controls the passage, write `Genre: None`.

## Selection Rules

- For a general review, select all three aggregate skills, plus at most one genre skill and only evidenced follow-up skills.
- Do not list the six quality component skills as separate top-level selections; `$oiticica-style-qualities` owns that composition.
- Do not list the seven clarity-fault component skills as separate top-level selections; `$oiticica-clarity-faults` owns that composition.
- If the passage is already strong, preserve it and name the relations it passes.
- Do not invent faults in clear, correct, specific prose or treat complexity as a fault by itself.
- Preserve historically accepted punctuation and usage in a sourced quotation; current convention alone is not a defect. This preservation rule governs audits and unrequested modernization, not an explicitly requested interpretive revision of a diagnosed defect. Label the interpretive choice instead of presenting it as source wording.
- Make the smallest local change that repairs an evidenced defect or failed quality. Preserve every undiagnosed word, tense, relation, and punctuation choice in a sourced quotation.
- Name the exact missing actor, ambiguous attachment, wrong order, broken relation, removable wording, sound collision, stock effect, or buried action. Do not offer speculative polish.
- Do not route to sound, meter, image, inversion, or antithesis unless the feature is present and relevant.
- Do not turn a practical rewrite into a long taxonomy.
- In generic description, replace controlling praise with observable properties, actions, spatial relations, or sensory facts.
- After diagnosing generic evaluation, delete every diagnosed evaluative adjective. Replacing it with another praise synonym or retaining it elsewhere does not repair the passage.
- When a stock scene-setting phrase supplies the main effect and revision is requested, replace it with concrete details already supplied by the passage. Preserve factual time, place, weather, actor, and action information even when it appears inside the stock phrase; remove the stock expression, not its facts. A famous source does not exempt a phrase from the defect rubric.
- In event sequences, preserve each actor, action, object, causal relation, and explicit `before` or `after` relation. Repair a misattached causal phrase with an idiomatic construction, but do not force cause before effect when either order is clear.
- Grade a bare demonstrative comparison term such as `more than these` as obscurity when the supplied passage does not name its referent and more than one contextual class, such as people or objects, remains plausible. Do not excuse it by assuming omitted source context.
- When the broad defect stage grades obscurity or the clarity-fault stage grades Ambiguity and revision is requested, apply `$oiticica-ambiguity` before drafting the revision. This is an execution requirement, not merely a response label. Name the viable readings, choose one plausible reading when the user gives no intention, and expose that choice in the revision. Replace the ambiguous word or attachment with a concrete noun phrase; adding words around the same expression or substituting a demonstrative plus generic `others`, `people`, or `things` does not name the referent. Do not retain the ambiguity merely because it may be deliberate in the source unless the user asks to preserve it.
- Grade Comma above `None` when a participial phrase interrupts the subject-predicate frame but has only a closing comma. Insert the matching opening comma after the subject when revision is requested; historical provenance does not preserve a mark that creates the false grouping under review.
- When the user says `revise only if needed`, revise only for an evidenced broad defect, clarity fault, or failed quality. Smoother flow or a possible paraphrase is not enough.
- Unless the user authorizes deletion, preserve every explicit fact in revision: time, place, actors, actions, objects, quantities, comparisons, and causal relations. Replacing a stock phrase does not authorize dropping the fact it expressed.

## Output

For a general review, use:

```markdown
Genre:
<selected genre skill or None>

Selected skills:
- oiticica-style-defects: <why the defect stage applies>
- oiticica-clarity-faults: <why the clarity-fault stage applies>
- oiticica-style-qualities: <why the quality stage applies>
- <optional genre or follow-up skill>: <evidence>

Diagnosis:
- <specific defect, quality failure, or passing relation>

Revision:
<revised passage, "Not requested.", or "No revision needed.">

Checks:
- Defects (before revision): Impurity <grade>; Prolixity <grade>; Obscurity <grade>; Disharmony <grade>; Banality <grade>; Weakness <grade>
- Clarity faults (before revision): Ambiguity <grade>; Anacoluthon <grade>; Accumulation <grade>; Brachylogy <grade>; Imprecision <grade>; Semicolon <grade>; Comma <grade>
- Qualities (final): Correctness <decision>; Concision <decision>; Clarity <decision>; Harmony <decision>; Originality <decision>; Vigor <decision>
```

Use only `None`, `Minor`, or `Major` for defect grades and only `Pass` or `Fail` for quality decisions; do not report `Present` or `Not applicable`. Keep the diagnosis concrete and the checks compact. For a requested single-skill review, use that skill's own response shape.

## Finish

Verify that all three aggregate stages ran in order, every selected skill has evidence, the revision preserves meaning and register, and no blocking defect or clarity fault survives the quality stage.

Source notes live in `references/notes.md`.

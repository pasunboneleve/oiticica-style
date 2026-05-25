---
name: oiticica-style-qualities
description: Apply Oiticica's style qualities concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Style Qualities

Use this skill when reviewing or rewriting English prose where style qualities is the controlling issue.

Source concept: Style has six essential qualities: correctness, concision, clarity, harmony, originality, and vigor.

## Rules

- Judge a passage by all six qualities; do not let one excuse failure in another.
- Treat correctness as the floor, not the finish.
- Treat concision as minimum effort for maximum expression, not mere shortness.
- Treat originality as personal exactness, not novelty for its own sake.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-style-qualities: one sentence naming the concept>

Preserve:
<supplied example text>

Why:
<why the model satisfies the concept>

Rubric:
<at least two objective checks, each marked Pass or Fail>
```

Use the repair shape for weak passages:

```markdown
Principle:
<oiticica-style-qualities: one sentence naming the concept>

Weak:
<small passage or paraphrase>

Fault:
<name the exact broken relation>

Better:
<corrected version>

Why:
<explain how the revision restores the relation>

Rubric:
<at least two objective checks, each marked Pass or Fail>
```

Start `Principle` with the exact skill name `oiticica-style-qualities`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- No grammar, spelling, or usage fault blocks comprehension.
- No removable word, clause, or example remains.
- The thought is easy to grasp on first reading.
- Sound, order, specificity, and energy support the meaning.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.

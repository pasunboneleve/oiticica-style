---
name: oiticica-gallicism
description: Apply Oiticica's gallicism concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Gallicism

Use this skill when reviewing or rewriting English prose where gallicism is the controlling issue.

Source concept: Gallicism is foreignness drawn from French diction or syntax; in English, treat any imported construction by English idiom.

## Rules

- Keep established French loanwords when they are natural English or exact cultural terms.
- Replace French-calqued syntax with idiomatic English order and prepositions.
- Do not condemn a loanword merely because it began outside English.
- Judge by current English use, clarity, and necessity.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-gallicism: one sentence naming the concept>

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
<oiticica-gallicism: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-gallicism`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The foreign source is not the sole objection.
- The sentence follows English idiom after revision.
- Necessary cultural terms remain.
- The correction is shorter or clearer than the calque.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.

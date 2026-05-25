---
name: oiticica-solecism
description: Apply Oiticica's solecism concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Solecism

Use this skill when reviewing or rewriting English prose where solecism is the controlling issue.

Source concept: Solecism is an error of syntax.

## Rules

- Find broken agreement, case, government, comparison, modifier attachment, and clause relation.
- Name the syntactic relation that fails.
- Correct by restoring the relation, not by rewriting the whole passage.
- Keep deliberate character speech when the task asks for dialogue or dialect.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-solecism: one sentence naming the concept>

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
<oiticica-solecism: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-solecism`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The review identifies the exact syntactic fault.
- The repair changes only the words needed to restore syntax.
- The actor and object remain the same.
- The result reads as current standard English.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.

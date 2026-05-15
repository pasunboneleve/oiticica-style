---
name: oiticica-concision
description: Apply Oiticica's concision concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Concision

Use this skill when reviewing or rewriting English prose where concision is the controlling issue.

Source concept: Concision expresses aspects, facts, or opinions with the fewest words compatible with the other qualities.

## Rules

- Remove superfluous aspects, episodes, opinions, adjectives, periphrases, redundant clauses, and avoidable subordination.
- Do not cut words that carry correctness, clarity, harmony, originality, or vigor.
- Prefer the direct noun or verb over a circumlocution.
- Keep only details that affect the total impression, action, or argument.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-concision: one sentence naming the concept>

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
<oiticica-concision: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-concision`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- Every retained word changes meaning, rhythm, emphasis, or relation.
- No stock adjective repeats what the noun already implies.
- Long subordinate clauses are reduced or coordinated when clarity improves.
- The shorter version preserves all necessary facts.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.

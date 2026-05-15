---
name: oiticica-brachylogy
description: Apply Oiticica's brachylogy concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Brachylogy

Use this skill when reviewing or rewriting English prose where brachylogy is the controlling issue.

Source concept: Brachylogy is the opposite vice of accumulation: too many short, disconnected phrases with forced pauses.

## Rules

- Join short fragments when they belong to one movement or relation.
- Keep short sentences for shock, turn, or emphasis, not as a default texture.
- Restore conjunctions or subordination when relation is otherwise unclear.
- Do not sacrifice grammar for brevity.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-brachylogy: one sentence naming the concept>

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
<oiticica-brachylogy: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-brachylogy`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- Short units have a reason.
- Related actions are connected.
- The rhythm varies.
- No fragment hides a needed subject, verb, or relation.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.

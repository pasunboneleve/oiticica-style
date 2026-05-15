---
name: oiticica-image
description: Apply Oiticica's image concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Image

Use this skill when reviewing or rewriting English prose where image is the controlling issue.

Source concept: An image is an aesthetic relation between objects, phenomena, or actions.

## Rules

- Name both sides of the relation and the shared quality.
- Reject images whose relation is stale, false, or merely decorative.
- Prefer a precise image drawn from the subject's world.
- Do not mix incompatible images in one sentence.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-image: one sentence naming the concept>

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
<oiticica-image: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-image`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The image has two clear terms.
- The shared relation is concrete.
- The image clarifies or intensifies the subject.
- No dead metaphor carries the main force.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.

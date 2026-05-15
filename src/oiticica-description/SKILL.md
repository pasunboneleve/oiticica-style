---
name: oiticica-description
description: Apply Oiticica's description concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Description

Use this skill when reviewing or rewriting English prose where description is the controlling issue.

Source concept: Description is a sequence of aspects.

## Rules

- Choose aspects that let the reader see this object, place, or person rather than a generic member of its class.
- Separate interior, landscape, type, still-life, and scene work by the kind of aspect being selected.
- Omit inventory items that do not distinguish the subject.
- Prefer concrete nouns, visible actions, local names, and sensory facts over mood labels.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-description: one sentence naming the concept>

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
<oiticica-description: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-description`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- Every sentence adds a visible or audible aspect.
- At least one detail distinguishes this subject from a stock example.
- Generic labels such as beautiful, gloomy, splendid, or picturesque are supported by particulars.
- The order lets the reader locate the parts without rereading.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.

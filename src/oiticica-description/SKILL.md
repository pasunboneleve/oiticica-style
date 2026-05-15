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

Use a concrete contrast:

```markdown
Principle:
<one sentence naming the concept>

Weak:
<small passage or paraphrase>

Fault:
<name the exact broken relation>

Better:
<corrected version>

Why:
<explain how the revision restores the relation>

Rubric:
<pass/fail against the objective checks>
```

## Objective Rubric

- Every sentence adds a visible or audible aspect.
- At least one detail distinguishes this subject from a stock example.
- Generic labels such as beautiful, gloomy, splendid, or picturesque are supported by particulars.
- The order lets the reader locate the parts without rereading.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A Dickens street passage that names shop signs, fog, mud, and lamps so the reader can place the scene.
- Negative model: A sunset described only as golden, majestic, beautiful, and beyond words.
- Required labels should be concrete, such as `choose, separate, omit` or a more exact local relation.

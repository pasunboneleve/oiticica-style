---
name: oiticica-meter
description: Apply Oiticica's meter concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Meter

Use this skill when reviewing or rewriting English prose where meter is the controlling issue.

Source concept: Meter is measured language; Oiticica uses scansion to train the ear for rhythm.

## Rules

- Use English metrical terms when analyzing English: stress, foot, iamb, trochee, anapest, dactyl, line, caesura.
- Do not translate Portuguese syllable-count rules directly into English stress verse.
- Scan only when rhythm is relevant to the task.
- Use meter as evidence for harmony, not as decoration.

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

- The analysis uses English prosody.
- Stressed and unstressed beats are marked or described accurately.
- The metrical observation explains an effect.
- The review does not impose meter on prose without need.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A Shakespeare pentameter line scanned by stress to explain emphasis.
- Negative model: Judging an English line only by Portuguese-style syllable count.
- Required labels should be concrete, such as `use, do, scan` or a more exact local relation.

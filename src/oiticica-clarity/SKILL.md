---
name: oiticica-clarity
description: Apply Oiticica's clarity concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Clarity

Use this skill when reviewing or rewriting English prose where clarity is the controlling issue.

Source concept: Clarity transmits thought in the form most easily understood.

## Rules

- Make subject, action, object, condition, and consequence visible.
- Separate crowded aspects, facts, or opinions into readable units.
- Put conditions before effects when the condition governs the effect.
- Repair ambiguity and anacoluthon before polishing sound.

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

- A reader can paraphrase the sentence once, correctly.
- Pronouns have single antecedents.
- Modifiers attach to the intended words.
- Cause, condition, concession, and result are in logical order.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: Orwell's expository prose where actors and consequences are plain.
- Negative model: After reviewing the file, the error was obvious and it was fixed.
- Required labels should be concrete, such as `make, separate, put` or a more exact local relation.

---
name: oiticica-anacoluthon
description: Apply Oiticica's anacoluthon concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Anacoluthon

Use this skill when reviewing or rewriting English prose where anacoluthon is the controlling issue.

Source concept: Anacoluthon is a break in logical order, usually by changing the expected subject or construction.

## Rules

- Track the sentence's announced subject or construction to its grammatical completion.
- Flag a break when the sentence starts one structure and finishes another by accident.
- Repair by restoring the promised subject, adding the missing link, or splitting the sentence.
- Keep deliberate anacoluthon in dramatic speech when it expresses interruption or emotion.

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

- The announced construction is identified.
- The point of break is identified.
- The repair completes one coherent construction.
- Deliberate speech effects are not overcorrected.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A Dickens character's broken speech kept because panic causes the break.
- Negative model: The report, when the auditors finished reading it, they rejected the figures.
- Required labels should be concrete, such as `track, flag, repair` or a more exact local relation.

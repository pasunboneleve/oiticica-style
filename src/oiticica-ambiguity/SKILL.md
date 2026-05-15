---
name: oiticica-ambiguity
description: Apply Oiticica's ambiguity concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Ambiguity

Use this skill when reviewing or rewriting English prose where ambiguity is the controlling issue.

Source concept: Ambiguity is a structure that allows more than one meaning when only one is intended.

## Rules

- Find the word, pronoun, modifier, punctuation mark, or clause relation that permits two readings.
- State both possible readings.
- Revise so only the intended reading remains.
- Keep useful literary ambiguity only when the task asks for it.

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

- At least two readings are named.
- The intended reading is selected.
- The fix removes the unintended reading.
- The revision does not flatten deliberate irony or double meaning.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A Henry James ambiguity preserved when the uncertainty is the point of view.
- Negative model: She saw the man with the telescope and waved.
- Required labels should be concrete, such as `find, state, revise` or a more exact local relation.

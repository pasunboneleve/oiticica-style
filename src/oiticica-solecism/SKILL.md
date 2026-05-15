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

- The review identifies the exact syntactic fault.
- The repair changes only the words needed to restore syntax.
- The actor and object remain the same.
- The result reads as current standard English.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: Austen dialogue that uses standard syntax while preserving social tone.
- Negative model: Him and me was going to the market when the letters arrived.
- Required labels should be concrete, such as `find, name, correct` or a more exact local relation.

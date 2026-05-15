---
name: oiticica-semicolon
description: Apply Oiticica's semicolon concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Semicolon

Use this skill when reviewing or rewriting English prose where semicolon is the controlling issue.

Source concept: The semicolon separates related clauses where a comma is too weak and a period too final.

## Rules

- Use semicolons for successive conditions before a conclusion, strong adversative turns, parallel clauses with omitted words, and list items that contain internal commas.
- Do not use a semicolon between unrelated sentences.
- Do not use a comma splice where a semicolon or period is required.
- Prefer a comma when the clauses are short and lightly joined.

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

- Both sides of the semicolon are grammatically compatible.
- The relation is contrast, parallelism, sequence, or complex listing.
- A comma would be ambiguous or too weak.
- A period would break a useful relation.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A Gibbon sentence whose semicolons keep balanced historical clauses in relation.
- Negative model: The moon rose; the soup was cold; sincerity is rare.
- Required labels should be concrete, such as `use, do, do` or a more exact local relation.

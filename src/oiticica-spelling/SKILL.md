---
name: oiticica-spelling
description: Apply Oiticica's spelling concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Spelling

Use this skill when reviewing or rewriting English prose where spelling is the controlling issue.

Source concept: Cacography is an error of writing; in English practice, treat it as spelling and orthographic error.

## Rules

- Use the spelling system requested by the user: American, British, or project-local.
- Correct misspellings, malformed compounds, capitalization, and apostrophes.
- Do not modernize proper names or quoted editions unless asked.
- Separate spelling faults from word-choice faults.

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

- The chosen English spelling convention is explicit when relevant.
- Every changed word has an orthographic reason.
- No proper noun is normalized accidentally.
- The correction does not mask a grammar or meaning issue.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A Bronte passage quoted with edition spelling preserved and surrounding analysis in modern spelling.
- Negative model: The goverment recieved seperate accomodations for it's officers.
- Required labels should be concrete, such as `use, correct, do` or a more exact local relation.

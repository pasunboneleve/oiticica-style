---
name: oiticica-foreignism
description: Apply Oiticica's foreignism concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Foreignism

Use this skill when reviewing or rewriting English prose where foreignism is the controlling issue.

Source concept: Barbarism is abusive use of foreign words or constructions.

## Rules

- Keep necessary foreign terms when English lacks an exact equivalent or the domain owns the term.
- Naturalize or translate needless foreign words that only display learning.
- Reject foreign syntax that makes English stiff or unclear.
- Do not purge useful loanwords that are established English.

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

- Each foreign term has necessity, domain value, or quotation value.
- English idiom governs the sentence.
- The review distinguishes loanword from needless display.
- The correction improves clarity without narrowing meaning.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A Conrad sentence that keeps nautical loanwords because they name exact things.
- Negative model: We made a rendezvous for the personnel to assist at the conference.
- Required labels should be concrete, such as `keep, naturalize, reject` or a more exact local relation.

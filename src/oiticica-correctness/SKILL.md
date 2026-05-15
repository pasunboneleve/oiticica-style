---
name: oiticica-correctness
description: Apply Oiticica's correctness concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Correctness

Use this skill when reviewing or rewriting English prose where correctness is the controlling issue.

Source concept: Correctness observes the grammatical tradition of the language being used.

## Rules

- Apply modern standard English grammar, spelling, idiom, and punctuation unless the task requires dialect or historical form.
- Preserve quoted historical language as quotation; modernize only the surrounding instruction.
- Fix correctness faults before judging elegance.
- Do not import Portuguese grammar rules into English.

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

- Subject, verb, pronoun, modifier, and punctuation choices conform to the intended English register.
- Dialect, archaism, or nonstandard form is marked by character, quotation, or purpose.
- No correction changes the facts or voice without reason.
- The revised sentence remains idiomatic English.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A George Eliot sentence whose long structure still keeps agreement and reference intact.
- Negative model: Between you and I, the committee were unable to decide who they should appoint.
- Required labels should be concrete, such as `apply, preserve, fix` or a more exact local relation.

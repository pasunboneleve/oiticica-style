---
name: oiticica-dissertation
description: Apply Oiticica's dissertation concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Dissertation

Use this skill when reviewing or rewriting English prose where dissertation is the controlling issue.

Source concept: Dissertation is a sequence of opinions.

## Rules

- State the opinion before decorating it.
- Give each paragraph one claim and the reason or example that tests it.
- Distinguish personal judgment from borrowed authority.
- Move from premise to contrast to conclusion, not from conclusion to afterthought.

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

- The main claim is explicit.
- Each supporting opinion has evidence or an example.
- Transitions name the relation: cause, contrast, concession, or result.
- The conclusion follows from the stated sequence.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A Johnson essay paragraph that states a moral claim, tests it with example, then turns the consequence.
- Negative model: An essay that stacks admirable nouns about liberty without saying what should be done.
- Required labels should be concrete, such as `state, give, distinguish` or a more exact local relation.

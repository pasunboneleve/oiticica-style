---
name: oiticica-inversion
description: Apply Oiticica's inversion concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Inversion

Use this skill when reviewing or rewriting English prose where inversion is the controlling issue.

Source concept: Inversion alters logical word order to give relief, rhythm, or emphasis.

## Rules

- Use inversion only when it improves emphasis, rhythm, or image placement.
- Keep modern English syntax intelligible.
- Reject violent or archaic inversion that calls attention to itself.
- Compare the inverted order with the direct order before recommending it.

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

- The word moved gains useful emphasis.
- The sentence remains idiomatic English.
- The inversion does not obscure subject and verb.
- The direct order is worse for a named reason.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: A poetic inversion in Wordsworth that places the landscape word under stress.
- Negative model: Brightly the quarterly report did the manager submit.
- Required labels should be concrete, such as `use, keep, reject` or a more exact local relation.

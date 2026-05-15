---
name: oiticica-concision
description: Apply Oiticica's concision concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Concision

Use this skill when reviewing or rewriting English prose where concision is the controlling issue.

Source concept: Concision expresses aspects, facts, or opinions with the fewest words compatible with the other qualities.

## Rules

- Remove superfluous aspects, episodes, opinions, adjectives, periphrases, redundant clauses, and avoidable subordination.
- Do not cut words that carry correctness, clarity, harmony, originality, or vigor.
- Prefer the direct noun or verb over a circumlocution.
- Keep only details that affect the total impression, action, or argument.

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

- Every retained word changes meaning, rhythm, emphasis, or relation.
- No stock adjective repeats what the noun already implies.
- Long subordinate clauses are reduced or coordinated when clarity improves.
- The shorter version preserves all necessary facts.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: Hemingway's early story prose where selected details carry the scene without explanation.
- Negative model: The celestial orb of daytime commenced its ascent above the eastern horizon.
- Required labels should be concrete, such as `remove, do, prefer` or a more exact local relation.

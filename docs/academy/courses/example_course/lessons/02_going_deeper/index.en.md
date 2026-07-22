---
title: "Quantifiers, Groups & Anchors"
description: Repeat, capture, and pin patterns to positions to match real-world data.
tags:
  - corner:academy
  - type:tutorial
  - topic:computer-science
  - difficulty:beginner
  - status:budding
entry_type: LearningResource
aliases: []
---

# Quantifiers, Groups & Anchors

!!! abstract "Lesson 2 of 2 · [Regular Expressions from Scratch](../../index.en.md)"
    With characters under your belt, you'll now say *how many* to match, *group* parts together,
    and *pin* patterns to positions — enough to validate a real input.

## Objectives

By the end of this lesson you will be able to:

- Use quantifiers to match repetition.
- Group sub-patterns and capture what they match.
- Anchor a pattern to the start or end of the input.

## Quantifiers

A quantifier says how many times the preceding element may repeat:

- `*` — zero or more; `+` — one or more; `?` — zero or one (optional).
- `{n}` — exactly *n*; `{n,}` — *n* or more; `{n,m}` — between *n* and *m*.

So `\d+` matches one or more digits, and `colou?r` matches both "color" and "colour".

## Groups

Parentheses group a sub-pattern so a quantifier applies to the whole thing, and **capture** what
it matched for later use: `(ab)+` matches "ababab", and in `(\d{4})-(\d{2})` the year and month are
captured separately. Use `|` for alternation: `(cat|dog)` matches either word.

## Anchors

Anchors match a *position*, not a character:

- `^` matches the start of the input; `$` matches the end.
- Anchoring both ends forces the pattern to describe the *whole* string, not just a substring.

## Capstone: validate an email

Putting it together — a deliberately simple email check:

```text
^[\w.+-]+@[\w-]+\.[a-z]{2,}$
```

It reads: start, one-or-more word/`.`/`+`/`-` characters, an `@`, a domain label, a literal dot,
then a 2+ letter suffix, end.

!!! warning "Regex has limits"
    A *fully* correct email validator is famously hard. This pattern is good enough for a form
    hint — knowing *when a regex is the wrong tool* is part of mastering them.

## Recap

- Quantifiers (`* + ? {n,m}`) express repetition; groups `(...)` capture and scope it.
- `|` alternates between options; `^` and `$` anchor to the start and end of the input.
- Real validation combines all three — and knows its own limits.

## Classwork

1. Write a pattern matching a US ZIP code: five digits, optionally followed by `-` and four more.
2. Write a pattern that matches a whole string of only lowercase letters.

??? example "Solutions"
    1. `^\d{5}(-\d{4})?$`
    2. `^[a-z]+$`

## Key terms

- **[Key Terms — Quantifiers, Groups & Anchors](./keywords.en.md)**

## Next

- ← Previous: [Literal text & character classes](../01_getting_started/index.en.md)
- 🎓 You've finished the course — back to the [overview](../../index.en.md) to review the roadmap.

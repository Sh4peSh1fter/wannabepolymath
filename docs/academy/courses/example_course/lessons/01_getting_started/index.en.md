---
title: "Literal Text & Character Classes"
description: Match exact text and sets of characters — the foundation of every regular expression.
tags:
  - corner:academy
  - type:tutorial
  - topic:computer-science
  - difficulty:beginner
  - status:budding
entry_type: LearningResource
aliases: []
---

# Literal Text & Character Classes

!!! abstract "Lesson 1 of 2 · [Regular Expressions from Scratch](../../index.en.md)"
    Every regex starts with matching characters. Here you'll match literal text, then widen the
    net with character classes.

## Objectives

By the end of this lesson you will be able to:

- Match literal text and understand why some characters must be escaped.
- Use a character class to match any one of a set of characters.
- Use ranges and negation inside a character class.

## Prerequisites

- An [online regex tester](https://regex101.com/) open in another tab. Nothing else.

## Matching literal text

The simplest pattern is just the text you want to find. The pattern `cat` matches the letters
`c`, `a`, `t` in sequence — it finds "cat" inside "concatenate".

Some characters are **metacharacters** (`. ^ $ * + ? ( ) [ ] { } | \`) — they have special meaning.
To match one literally, escape it with a backslash: `3\.14` matches the text "3.14" (an unescaped
`.` would match *any* character).

## Character classes

A character class, written in square brackets, matches **any one** character from the set:

- `[aeiou]` matches a single vowel.
- `[0-9]` uses a **range** to match any single digit; `[a-z]` matches any lowercase letter.
- `[^0-9]` — a leading `^` **negates** the class: match any single character that is *not* a digit.

!!! tip "Shorthand classes"
    Common classes have shorthands: `\d` = `[0-9]`, `\w` = `[A-Za-z0-9_]`, `\s` = whitespace.
    Their uppercase forms negate: `\D` is "not a digit".

## Recap

- A bare pattern matches literal text; escape metacharacters with `\` to match them literally.
- `[...]` matches one character from a set; ranges (`a-z`) and negation (`^`) extend it.
- `\d`, `\w`, `\s` are handy shorthands for the most common classes.

## Classwork

1. Write a pattern that matches a single hexadecimal digit (`0-9` or `a-f`).
2. Write a pattern that matches the literal string "a+b".

??? example "Solutions"
    1. `[0-9a-f]`
    2. `a\+b` — the `+` is a metacharacter, so it must be escaped.

## Key terms

- **[Key Terms — Literal Text & Character Classes](./keywords.en.md)**

## Next

- ← Back to: [Course overview](../../index.en.md)
- → Next: [Quantifiers, groups & anchors](../02_going_deeper/index.en.md)

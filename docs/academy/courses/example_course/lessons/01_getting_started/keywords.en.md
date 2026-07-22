---
title: "Key Terms — Literal Text & Character Classes"
description: Key terms introduced in the first lesson of Regular Expressions from Scratch.
tags:
  - corner:academy
  - type:reference
  - topic:computer-science
  - status:budding
entry_type: DefinedTermSet
aliases: []
---

# Key Terms — Literal Text & Character Classes

The vocabulary introduced in this lesson. Hover a term to reveal its definition.

## Patterns & Matching

<div class="annotate" markdown>

- Regular expression (1)
- Match (2)
- Metacharacter (3)
- Escaping (4)

</div>

1.  A string that describes a search pattern over text. **Aliases:** regex, regexp. **See also:** [Wikipedia](https://en.wikipedia.org/wiki/Regular_expression).
2.  The portion of input text that a pattern successfully describes.
3.  A character with special meaning in a pattern (such as `.`, `*`, or `[`) rather than its literal value.
4.  Prefixing a metacharacter with a backslash (`\`) so it is matched as a literal character.

## Character Classes

<div class="annotate" markdown>

- Character class (1)
- Range (2)
- Negation (3)
- Shorthand class (4)

</div>

1.  A set in square brackets (`[...]`) that matches any single character from the set. **Scope:** here we cover positive, ranged, and negated classes.
2.  A hyphenated span inside a class (e.g. `a-z`) that stands for every character between the endpoints.
3.  A leading `^` inside a class (`[^...]`) that inverts it, matching any character *not* listed.
4.  A backslash escape standing for a common class: `\d` (digit), `\w` (word character), `\s` (whitespace).

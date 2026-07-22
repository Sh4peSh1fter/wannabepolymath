---
title: "Key Terms — Quantifiers, Groups & Anchors"
description: Key terms introduced in the second lesson of Regular Expressions from Scratch.
tags:
  - corner:academy
  - type:reference
  - topic:computer-science
  - status:budding
entry_type: DefinedTermSet
aliases: []
---

# Key Terms — Quantifiers, Groups & Anchors

The vocabulary introduced in this lesson. Hover a term to reveal its definition.

## Repetition

<div class="annotate" markdown>

- Quantifier (1)
- Greedy matching (2)

</div>

1.  A symbol specifying how many times the preceding element may repeat: `*` (0+), `+` (1+), `?` (0 or 1), `{n,m}` (a range). **See also:** [Wikipedia](https://en.wikipedia.org/wiki/Regular_expression#Quantification).
2.  The default behaviour where a quantifier matches as much text as possible; appending `?` makes it *lazy* (as little as possible).

## Grouping & Alternation

<div class="annotate" markdown>

- Group (1)
- Capture group (2)
- Alternation (3)

</div>

1.  A sub-pattern enclosed in parentheses `(...)` so a quantifier applies to it as a unit.
2.  A group whose matched text is remembered for back-references or extraction.
3.  The `|` operator, matching the pattern on either side (e.g. `cat|dog`).

## Positions

<div class="annotate" markdown>

- Anchor (1)

</div>

1.  A token that matches a position rather than a character: `^` (start of input) and `$` (end of input). **Aliases:** boundary matcher.

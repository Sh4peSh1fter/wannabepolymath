---
title: "Create Your First Mermaid Diagram"
description: Render a flowchart from plain text inside a Markdown page — in about five minutes.
tags:
  - corner:academy
  - type:tutorial
  - topic:computer-science
  - difficulty:beginner
  - status:budding
entry_type: LearningResource
aliases: []
---

# Create Your First Mermaid Diagram

!!! note "Example tutorial"
    A worked demonstrator of the Academy tutorial pattern. Author real tutorials from
    `_templates/tutorial_template.en.md`.

[Mermaid](https://mermaid.js.org/) lets you describe diagrams in plain text and have them rendered
as pictures — perfect for a knowledge base, because the "source" stays diff-able and searchable.
This site already has Mermaid enabled, so you can start immediately.

## What you'll build

A simple flowchart, written as four lines of text, that renders as boxes and arrows on the page.

## Prerequisites

- Any Markdown page in this project (or an [online live editor](https://mermaid.live/)).

## Steps

1. **Open a fenced code block and label it `mermaid`.** The label tells the renderer to treat the
   contents as a diagram rather than code.

2. **Declare a diagram type and add nodes.** `flowchart LR` means "left to right"; each `-->` draws
   an arrow between two nodes:

    ````text
    ```mermaid
    flowchart LR
        A[Idea] --> B[Draft]
        B --> C[Publish]
    ```
    ````

3. **Preview the page.** Run `poetry run mkdocs serve` and open the page — the block renders as a
   diagram. This is exactly what produces the roadmap in the
   [example course](../courses/example_course/index.en.md).

## Result

The block above renders like this:

```mermaid
flowchart LR
    A[Idea] --> B[Draft]
    B --> C[Publish]
```

## Next steps

- Try `flowchart TD` (top-down), or branch with `A --> B` and `A --> C`.
- See the roadmap in [Regular Expressions from Scratch](../courses/example_course/index.en.md) for
  a real-world use of a Mermaid flowchart.

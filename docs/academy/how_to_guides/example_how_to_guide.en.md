---
title: "How to Add a New Observatory Field"
description: Scaffold a new Observatory field from the template and wire it into the site.
tags:
  - corner:academy
  - type:guide
  - topic:computer-science
  - status:budding
entry_type: HowTo
aliases: []
---

# How to Add a New Observatory Field

!!! note "Example guide"
    A worked demonstrator of the Academy how-to pattern. Author real guides from
    `_templates/how_to_guide_template.en.md`.

You want to add a new field (e.g. a new science) to the Observatory, following the established
four-file pattern. This guide assumes you already know the repo layout and can run the site locally.

## Prerequisites

- A local checkout with dependencies installed (`poetry install`).
- Decided the field's **science category** (`formal_sciences`, `natural_sciences`, …) and its
  lowercase-underscore folder name.

## Steps

1. **Copy the template folder** into the right category:

    ```bash
    cp -r docs/observatory/_templates/field_template \
          docs/observatory/<category>/<new_field>
    ```

2. **Fill in each of the four files** (`index`, `keywords`, `entities`, `sources`). Set a Title-Case
   `title` (same casing across all four), a `topic:<field>` tag, the correct `entry_type`, and start
   at `status:seedling`. Mirror `formal_sciences/mathematics/` — the reference exemplar.

3. **Wire it into `mkdocs.yml` `nav:`** under its category, with the standard four child entries
   (Overview, Key Terms & Concepts, Key Entities, Sources & Further Reading). Reference the
   `.en.md` files as the sibling fields do.

4. **Remove the field from `exclude_docs:`** if you scaffolded it there as a draft first.

## Verify

```bash
poetry run mkdocs build --strict
```

A zero-warning build confirms the nav paths resolve and no links are broken. Then
`poetry run mkdocs serve` and click through the new field's four pages.

## Related

- **[Create your first Mermaid diagram](../tutorials/example_tutorial.en.md)** — if your field's
  index needs a diagram.
- The Observatory conventions live in the project's `CLAUDE.md` (the "Observatory field pattern").

---
title: "mkdocs build --strict Fails on an Unrecognized Relative Link"
description: A strict build breaks on a link that renders fine locally — cause and fix.
tags:
  - corner:academy
  - type:troubleshooting
  - topic:computer-science
  - status:budding
aliases: []
entry_type: TechArticle
---

# `mkdocs build --strict` Fails on an Unrecognized Relative Link

!!! note "Example journal"
    A worked demonstrator of the Academy troubleshooting pattern. Author real journals from
    `_templates/troubleshooting_journal_template.en.md`.

## Problem

`poetry run mkdocs build --strict` exits non-zero (failing CI), even though the page renders fine
under `mkdocs serve`.

## Environment

- MkDocs + Material, `mkdocs-static-i18n` with `docs_structure: suffix`.
- A new page added under a corner, linking to a sibling page.

## Symptoms

```text
WARNING - Doc file 'academy/courses/example_course/index.en.md' contains a link
          '../tutorial.md', but the target is not found among documentation files.
Aborted with 1 warnings in strict mode!
```

## Investigation

1. Opened the page under `mkdocs serve` → the link *worked*. So it's strict-mode-only. → rules out
   a totally missing file.
2. Checked the target existed on disk → it did, as `example_tutorial.en.md`. → the *name* is wrong
   in the link, not the file.
3. Re-read the CLAUDE.md i18n note → relative links between content pages must point at the actual
   `.en.md` file; a bare `.md` or a wrong slug isn't resolved as a doc and only "works" in serve
   because of lenient fallback.

## Root cause

The link used a stale/short filename (`../tutorial.md`) instead of the real suffixed path
(`../tutorials/example_tutorial.en.md`). `--strict` treats any unresolved internal link as a hard
error; `serve` is lenient, which is why it hid the bug.

## Resolution

Point the link at the real file, with its `.en.md` suffix and correct relative depth:

```text
[Create your first Mermaid diagram](../tutorials/example_tutorial.en.md)
```

Re-run to confirm:

```bash
poetry run mkdocs build --strict   # 0 warnings
```

## Prevention / takeaways

- Always run `--strict` locally before committing — `serve` will not catch broken internal links.
- When you rename or move a page, grep the repo for the old slug and update every link.

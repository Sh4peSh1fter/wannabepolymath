---
title: Project Standards
description: The authoritative conventions for writing, naming, structuring, and maintaining content in the Wannabe Polymath knowledge base.
icon: material/ruler-square
tags:
  - about
  - standards
  - conventions
---

# Project Standards

This is the **single source of truth** for how content in this knowledge base is written,
named, structured, and maintained. It describes the conventions as they are actually
enforced (the site builds under `mkdocs build --strict`, so drift is caught automatically).
When a convention here conflicts with an older page, this document wins — fix the page.

## File and folder naming

- **Use `lowercase_with_underscores`** for every file and folder
  (e.g. `formal_sciences`, `round_table`, `oral_health`, `beef_stew.en.md`).
- **No** spaces, capital letters, or hyphens in names; **no** double underscores.
- Names should be short, descriptive, and stable — renaming a published page changes its
  URL, so add a redirect (see [Maintenance](#maintenance)) whenever you must rename one.
- Assets live in an `_assets/` folder next to the content that uses them.

## Language suffixes (i18n)

Every content page carries a language suffix so the `mkdocs-static-i18n` plugin can serve
it in the right language:

- `page.en.md` — English (the default language).
- `page.he.md` — Hebrew (rendered right-to-left automatically).

Never commit a bare `page.md` content file. If a page has no translation yet, the English
version is served as the fallback.

## Frontmatter schema

Every content page **must** begin with a YAML frontmatter block. Required and optional keys:

```yaml
---
title: Human-Readable Page Title      # required
description: One sentence on the page. # required — feeds SEO meta + social cards + JSON-LD
tags:                                  # required — see the tag taxonomy below
  - topic:economics
  - type:reference
  - status:published
date: 2026-07-11                       # optional — creation date (YYYY-MM-DD)
icon: material/telescope               # optional — section landing pages only
hide:                                  # optional — section landing pages only
  - navigation
  - toc
---
```

- `title` and `description` are mandatory on every page. `description` is reused for the
  page's `<meta>` description, its social card, and its structured data — keep it to one
  clear sentence.
- "Last updated" timestamps are generated automatically from git history; do **not** hand-maintain
  a `last_updated` field. Use `date` only for the original creation/publication date.

### Tag taxonomy

Tags use prefixes so they can be filtered and aggregated. Apply at minimum a `topic:` and a
`type:` tag to every page.

| Prefix | Purpose | Examples |
| --- | --- | --- |
| `topic:` | Subject/discipline | `topic:economics`, `topic:devops`, `topic:philosophy` |
| `type:` | Content format (see below) | `type:tutorial`, `type:reference`, `type:explanation`, `type:item-review` |
| `status:` | Lifecycle | `status:draft`, `status:published`, `status:needs-update` |
| `skill-level:` | Optional, educational content | `skill-level:beginner`, `skill-level:advanced` |

Reuse existing tags before inventing new ones; keep them lowercase and hyphen-separated
*within* a tag value (e.g. `topic:computer-science`).

## Content types (Diátaxis)

Teaching content follows the [Diátaxis](https://diataxis.fr/) framework, which separates
documentation by the reader's need. **Do not mix modes on one page** — a tutorial that
drifts into background theory confuses the learner.

| Mode | Reader need | Where it lives | `type:` tag |
| --- | --- | --- | --- |
| **Tutorial** | "Teach me, step by step" | Academy | `type:tutorial` |
| **How-to guide** | "Help me accomplish a task" | Academy | `type:how-to` |
| **Reference** | "Tell me the facts" | Observatory, Academy | `type:reference` |
| **Explanation** | "Help me understand why" | Academy, Round Table | `type:explanation` |

The **Observatory** is the reference layer — its per-field `keywords`, `entities`, and
`sources` pages are dry, accurate reference material, not tutorials.

## Writing style

- Clear, concise, active voice. Short paragraphs (3–4 sentences).
- Start each page with an `#` H1 that matches the frontmatter `title`, then a short intro.
- Maintain heading hierarchy (`#` → `##` → `###`); never skip levels.
- Prefer the platform's built-in features over raw HTML: admonitions (`!!! note`),
  content tabs, annotations, and grid cards. See the [Formatting Guide](./formatting_guide/index.md).
- **Favor visuals.** The most common reader feedback is that pages are text-heavy — use
  diagrams (Mermaid), images, and tables to break up prose.

## Media

- Preferred formats: **WebP** for photos, **PNG** for graphics/screenshots, **SVG** for
  icons/diagrams. Keep individual images well under ~500 KB; optimize before committing.
- Always provide descriptive alt text.
- Store images in the nearest `_assets/` folder and reference them with relative paths.

## The Observatory field pattern

Each Observatory field is a folder containing exactly four files. Copy the template at
`observatory/_templates/field_template/` when adding a field:

- `index.en.md` — field overview and links to the other three.
- `keywords.en.md` — key terms and concepts (uses the Material annotation pattern).
- `entities.en.md` — influential figures and organizations.
- `sources.en.md` — further reading.

## Navigation

- The `nav:` tree in `mkdocs.yml` is maintained by hand; it does **not** auto-discover
  pages. Add every new page to `nav:` or it won't appear in the site navigation.
- In `nav:`, reference the **base** filename (`observatory/index.md`), not the suffixed one
  (`observatory/index.en.md`) — the i18n plugin resolves the suffix.
- Keep navigation shallow (avoid more than three levels).

## Drafts and unpublished content

Work-in-progress that isn't ready to publish is **quarantined**: it stays in the repository
(version-controlled) but is excluded from the built site.

- Tag it `status:draft`.
- Add its path to the `exclude_docs:` list in `mkdocs.yml` so it is not built or linked.
- When it's ready, remove it from `exclude_docs`, add it to `nav:`, and set
  `status:published`.

## Maintenance

- **Renames/moves:** add a `redirect_maps` entry (via the `redirects` plugin) from the old
  URL to the new one so existing links don't break.
- **Quality gates:** the CI pipeline runs `mkdocs build --strict` (fails on any broken link
  or config warning), `markdownlint`, and a link check on every pull request. Content that
  breaks these gates is not merged.
- **Reviews:** periodically audit for broken links, stale content (`status:needs-update`),
  and oversized images.

---

*These standards evolve with the project. Propose changes via a pull request.*

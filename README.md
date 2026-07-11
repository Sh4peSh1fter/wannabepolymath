# Wannabe Polymath

My personal knowledge base, blog, and portfolio — a place to document what I learn on the
way to becoming a polymath, and to share that knowledge with others.

Built with [MkDocs](https://www.mkdocs.org/) and
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), and deployed to GitHub
Pages. Huge thanks to MkDocs, Material, and everyone and everything that inspired this project.

🔗 **Live site:** <https://Sh4peSh1fter.github.io/wannabepolymath/>

## Getting started

Requires Python 3.12+ and [Poetry](https://python-poetry.org/).

```bash
python -m venv .venv
source .venv/bin/activate         # macOS / Linux
# .\.venv\Scripts\Activate.ps1    # Windows

pip install poetry
poetry install                    # install dependencies from pyproject.toml / poetry.lock

poetry run mkdocs serve           # live preview at http://127.0.0.1:8000
poetry run mkdocs build --strict  # production build; fails on broken links / warnings
```

## Project layout

```
mkdocs.yml        # Site configuration and navigation.
includes/         # Shared Markdown snippets (e.g. the abbreviations glossary).
overrides/        # Material theme template overrides.
docs/             # All knowledge-base content, organized into "Corners".
    index.en.md   # Homepage.
    about/        # The project's vision, standards, and authoring guides.
    observatory/  # Key terms, concepts, figures, and sources across fields.
    academy/      # Tutorials, how-to guides, and explanations (Diátaxis-based).
    ...           # Round Table, Incubator, Bazaar, Hall of Fame, Other Corners.
```

Content is bilingual-ready via `mkdocs-static-i18n`: pages use language suffixes
(`*.en.md`, `*.he.md`), with English as the default.

## License

This repository is **dual-licensed** to separate the software from the knowledge it hosts:

- **Code, configuration, and snippets** — [MIT License](LICENSE).
- **Content under `docs/`** (prose, notes, images) —
  [Creative Commons BY-NC-SA 4.0](LICENSE-CONTENT).

In short: you're welcome to take inspiration from and share the content **with attribution,
for non-commercial purposes**, and any derivatives must stay under the same license. Please
don't repackage or sell it. When reusing content, credit it as:

> "Wannabe Polymath" by Kivsean (<https://Sh4peSh1fter.github.io/wannabepolymath/>),
> licensed under CC BY-NC-SA 4.0.

## Contributing

Feedback and contributions are welcome — open an issue or a pull request on
[GitHub](https://github.com/Sh4peSh1fter/wannabepolymath). See the
[About section](https://Sh4peSh1fter.github.io/wannabepolymath/about/) for the project's
vision, standards, and authoring guides.

## Roadmap / ideas

1. A script to title-case all page titles consistently.
2. Parameterize Academy questions (difficulty, tags) so a reader can generate a custom exam
   by tag and difficulty.
3. Reduce text density — lean on images, diagrams, and visual explanations (the most common
   feedback received).

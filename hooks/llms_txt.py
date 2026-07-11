"""MkDocs hook that generates /llms.txt and /llms-full.txt for the DEFAULT (English)
locale only.

This replaces the mkdocs-llmstxt plugin, which is incompatible with mkdocs-static-i18n
here (it captured the Hebrew build pass and emitted wrong /he/.../index.md URLs). By
collecting pages during the build and filtering out the Hebrew (`he/`) variants, we emit
clean English URLs.

- /llms.txt       — a curated, sectioned index (title + link + description per page).
- /llms-full.txt  — every English page's Markdown concatenated, for large-context agents.

See: https://llmstxt.org/
"""

from __future__ import annotations

import os

# Section title -> list of top-level path prefixes (relative to docs/, without language
# suffix in the built URL). Order defines the order in llms.txt.
_SECTIONS: list[tuple[str, tuple[str, ...]]] = [
    ("Observatory (reference)", ("observatory/",)),
    ("Academy (learning)", ("academy/",)),
    ("Round Table (analysis)", ("round_table/",)),
    ("Incubator (projects)", ("incubator/",)),
    ("Bazaar (recommendations)", ("bazaar/",)),
    ("Hall of Fame", ("hall_of_fame/",)),
    ("Other Corners", ("other_corners/",)),
    ("About", ("about/",)),
]

_DESCRIPTION = (
    "Wannabe Polymath is a personal knowledge base documenting one learner's journey "
    "across many disciplines, organized into themed \"Corners\": the Observatory "
    "(reference), the Academy (tutorials, how-to guides, explanations), the Round Table "
    "(problem analyses), the Incubator (projects), the Bazaar (researched recommendations), "
    "the Hall of Fame (inspiring figures), and Other Corners."
)

# Collected across on_page_content calls, keyed by clean URL -> (title, markdown).
_pages: dict[str, tuple[str, str]] = {}


def on_page_content(html, page, config, files):
    """Collect each English page's source Markdown (skip Hebrew /he/ variants)."""
    url = (page.url or "").lstrip("/")
    if url.startswith("he/"):
        return html  # skip the Hebrew build pass
    title = page.title or url
    markdown = page.markdown or ""
    _pages[url] = (str(title), markdown)
    return html


def _abs_url(site_url: str, url: str) -> str:
    return site_url.rstrip("/") + "/" + url


def _first_paragraph(markdown: str) -> str:
    for line in markdown.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("---") or s.startswith("<"):
            continue
        return s
    return ""


def on_post_build(config):
    site_dir = config["site_dir"]
    site_url = config.get("site_url") or ""
    site_name = config.get("site_name", "Documentation")

    # --- llms.txt: curated, sectioned index ---
    lines = [f"# {site_name}", "", f"> {config.get('site_description', '').strip()}", "", _DESCRIPTION, ""]
    used: set[str] = set()
    for section_title, prefixes in _SECTIONS:
        entries = sorted(
            (url, title)
            for url, (title, _md) in _pages.items()
            if url not in used and any(url.startswith(p) for p in prefixes)
        )
        if not entries:
            continue
        lines.append(f"## {section_title}")
        lines.append("")
        for url, title in entries:
            used.add(url)
            lines.append(f"- [{title}]({_abs_url(site_url, url)})")
        lines.append("")

    with open(os.path.join(site_dir, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # --- llms-full.txt: full Markdown concatenation ---
    full = [f"# {site_name}", "", _DESCRIPTION, ""]
    for url in sorted(_pages):
        title, markdown = _pages[url]
        full.append(f"## {title}")
        full.append(f"<!-- {_abs_url(site_url, url)} -->")
        full.append("")
        full.append(markdown.strip())
        full.append("")
    with open(os.path.join(site_dir, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(full))

---
title: Tagging Guide
description: Guidelines and predefined tags for content organization.
tags:
  - tagging
  - standards
  - organization
  - metadata
---

# Tagging Guide

Effective tagging is crucial for content discoverability, organization, and for enabling features like topic aggregation and faceted search. This guide outlines the types of tags we use and provides lists of predefined tags within categories.

**Guiding Principles for Tagging:**

*   **Clarity:** Tags should be unambiguous and easy to understand.
*   **Consistency:** Use predefined tags whenever possible. If a new concept requires a new tag, consider if it fits an existing category or if a new category is needed (and update this guide).
*   **Relevance:** Only use tags that are directly relevant to the content.
*   **Specificity:** Prefer specific tags over overly broad ones, but avoid excessive granularity.
*   **Case:** Use lowercase for all tags.
*   **Spaces:** Use hyphens (`-`) instead of spaces for multi-word tags (e.g., `artificial-intelligence`).

## Tag Categories and Prefixes

We use prefixes to categorize tags. This helps in understanding the role of a tag at a glance and can be used for advanced filtering.

### 1. `topic:` - Subject Matter

These tags identify the primary subject(s) or discipline(s) the content relates to. They are fundamental for organizing knowledge within the **Observatory** and across all **Corners**.

*   **Purpose:** To group all content related to a specific academic field, area of study, or distinct subject.
*   **Examples:**
    *   `topic:artificial-intelligence`
    *   `topic:neuroscience`
    *   `topic:philosophy-of-mind`
    *   `topic:quantum-physics`
    *   `topic:devops`
    *   `topic:project-management`
    *   *(Please expand this list with your primary topics)*

### 2. `corner:` - Thematic Section

These tags indicate which primary thematic "Corner" the content belongs to or is most closely associated with. While content lives in a Corner's folder, this tag can reinforce association, especially if content is aggregated or displayed out of its original context.

*   **Purpose:** To identify the primary thematic area of the content.
*   **Predefined Tags:**
    *   `corner:round-table`
    *   `corner:incubator`
    *   `corner:academy`
    *   `corner:observatory`
    *   `corner:bazaar`
    *   *(Add `corner:forge` if it becomes active)*

### 3. `type:` - Content Format/Nature

These tags describe the format or nature of the content itself.

*   **Purpose:** To allow users to find specific kinds of information (e.g., only tutorials, only project pages).
*   **Examples:**
    *   `type:article`
    *   `type:blog-post`
    *   `type:guide`
    *   `type:tutorial`
    *   `type:project-showcase`
    *   `type:idea-pitch`
    *   `type:problem-analysis`
    *   `type:solution-proposal`
    *   `type:keyword-definition`
    *   `type:concept-map`
    *   `type:random-fact`
    *   `type:tool-review`
    *   `type:methodology`
    *   *(Please refine and expand this list based on your content types)*

### 4. `status:` - Content Lifecycle (Optional)

These tags can indicate the current state of a piece of content, especially for dynamic items like projects or articles under development.

*   **Purpose:** To track progress and manage content workflow.
*   **Examples:**
    *   `status:idea`
    *   `status:in-progress`
    *   `status:published`
    *   `status:needs-review`
    *   `status:archived`
    *   `status:experimental`
    *   *(Consider if these are needed and expand)*

### 5. `difficulty:` - Content Complexity (Optional, for Academy/Tutorials)

For educational content, these tags can help users find material appropriate to their current understanding.

*   **Purpose:** To guide learners to suitable content.
*   **Examples:**
    *   `difficulty:beginner`
    *   `difficulty:intermediate`
    *   `difficulty:advanced`
    *   *(Consider if these are needed)*

### 6. General Keywords (No Prefix)

These are specific, non-categorized keywords that further describe the content. They should be more granular than `topic:` tags.

*   **Purpose:** To capture specific concepts, tools, techniques, or names mentioned within the content that aren't broad enough to be a `topic:` but are still useful for search and discovery.
*   **Examples:**
    *   `docker`
    *   `meditation`
    *   `stoicism`
    *   `kanban-method`
    *   `socratic-dialogue`
    *   *(These will be highly content-dependent and will grow organically)*

## How to Use Tags in Frontmatter

Tags should be listed in the frontmatter of your Markdown files:

```yaml
---
title: My Awesome Article
description: An article about something cool.
tags:
  - topic:artificial-intelligence
  - corner:academy
  - type:article
  - status:published
  - machine-learning
  - neural-networks
---
```

## Maintaining This Guide

This guide is a living document. As new types of content emerge or new common themes are identified, please update the tag categories and predefined lists here.

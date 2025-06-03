# Project Standards and Guidelines

## Overview
This document outlines the standards and guidelines for maintaining consistency and quality across the Wanna be Polymath project. These standards cover file organization, naming conventions, documentation, and development practices.

## File Organization

### Naming Conventions

#### File Names
1. **General Rules**
   - Use lowercase letters
   - Replace spaces with underscores
   - Use descriptive names
   - Include version numbers when applicable

2. **File Types**
   - Markdown: `.md`
   - Images: `.png`, `.jpg`, `.webp`
   - Code: `.py`, `.js`, `.css`
   - Configuration: `.yml`, `.json`

3. **Directory Structure**
   - Use lowercase
   - Separate words with underscores
   - Keep names concise
   - Follow logical hierarchy

### Directory Organization

#### Content Structure
1. **Documentation**
   - `/docs`
     - `/About`
     - `/topics`
     - `/corners`
     - `/assets`

2. **Source Code**
   - `/src`
     - `/components`
     - `/styles`
     - `/utils`
     - `/tests`

3. **Assets**
   - `/assets`
     - `/images`
     - `/videos`
     - `/audio`
     - `/fonts`

## Documentation Standards

### Markdown Formatting

#### Headers
1. **Structure**
   - Use ATX-style headers
   - Maintain hierarchy
   - Include table of contents
   - Link to related content

2. **Formatting**
   - H1: `# Title`
   - H2: `## Section`
   - H3: `### Subsection`
   - H4: `#### Detail`

#### Content
1. **Text Formatting**
   - Use emphasis sparingly
   - Maintain consistent style
   - Include code blocks
   - Add proper links

2. **Lists**
   - Use appropriate markers
   - Maintain indentation
   - Keep items concise
   - Use nested lists when needed

### Code Documentation

#### Comments
1. **Style**
   - Clear and concise
   - Purpose-focused
   - Up-to-date
   - Language-appropriate

2. **Format**
   - Function documentation
   - Class documentation
   - Module documentation
   - Inline comments

## Development Standards

### Code Style

#### General Rules
1. **Formatting**
   - Consistent indentation
   - Line length limits
   - Spacing rules
   - Bracket placement

2. **Naming**
   - Descriptive variables
   - Clear function names
   - Consistent casing
   - Meaningful constants

### Version Control

#### Git Practices
1. **Commits**
   - Clear messages
   - Atomic changes
   - Proper branching
   - Regular updates

2. **Branches**
   - Feature branches
   - Development branch
   - Production branch
   - Hotfix branches

## Content Standards

### Writing Style

#### General Guidelines
1. **Tone**
   - Professional
   - Clear
   - Consistent
   - Engaging

2. **Structure**
   - Logical flow
   - Clear headings
   - Proper paragraphs
   - Effective transitions

### Media Standards

#### Images
1. **Format**
   - WebP preferred
   - PNG for graphics
   - JPG for photos
   - SVG for icons

2. **Quality**
   - Appropriate resolution
   - Optimized size
   - Clear focus
   - Proper compression

### Tagging Strategy

A consistent tagging strategy is crucial for content discoverability, organization, and for enabling the hybrid navigation model (Thematic Corners + Topic Hubs). Tags help users find related information easily and allow for powerful filtering and search functionalities.

**Guiding Principles:**
- **Clarity:** Tags should be unambiguous and easy to understand.
- **Consistency:** Use a predefined set of tag prefixes and a consistent style (e.g., lowercase, hyphen-separated for multi-word tags).
- **Comprehensiveness:** Aim to tag content thoroughly but avoid over-tagging with irrelevant terms.
- **Relevance:** Tags should accurately reflect the content's subject matter, purpose, and context within the platform.

**Tag Categories (Prefixes Recommended):**

1.  **`topic:`** Identifies the main subject matter or discipline.
    *   Examples: `topic:devops`, `topic:neuroscience`, `topic:ancient-history`, `topic:python-programming`
    *   Crucial for building Topic Hub pages.

2.  **`corner:`** Indicates the thematic section where the content primarily resides or its main purpose.
    *   Examples: `corner:academy` (for tutorials/guides), `corner:observatory` (for keywords/concepts), `corner:round-table` (for discussions), `corner:incubator` (for projects/ideas), `corner:bazaar` (for random facts/discoveries), `corner:forge` (for self-improvement).

3.  **`type:`** Specifies the format or nature of the content.
    *   Examples: `type:tutorial`, `type:guide`, `type:article`, `type:project-showcase`, `type:problem-analysis`, `type:keyword-map`, `type:quick-fact`, `type:tool-review`, `type:blog-post`.

4.  **`skill-level:`** (Optional, but recommended for educational content)
    *   Examples: `skill-level:beginner`, `skill-level:intermediate`, `skill-level:advanced`.

5.  **`status:`** (Optional, useful for tracking content development)
    *   Examples: `status:draft`, `status:review`, `status:published`, `status:needs-update`.

6.  **General Keywords:** Additional descriptive keywords not covered by prefixes.
    *   Examples: `cicd`, `cognitive-bias`, `stoicism`, `api-design`.

**Application Guidelines:**
-   Every piece of content should have at least one `topic:` tag and one `corner:` tag.
-   Strive to include a `type:` tag for clarity.
-   Use existing tags whenever possible to maintain consistency. If a new, necessary tag is identified, consider if it fits an existing category or if a new category needs discussion.
-   Keep tags relatively concise.
-   The tagging system should be documented and easily accessible to all contributors.
-   Regularly review and refine the tag vocabulary to ensure it remains relevant and manageable.

**Integration with Search:**
The tagging system will be a cornerstone of the search functionality, allowing users to perform faceted searches (e.g., find all `type:tutorial` on `topic:devops` that are `skill-level:beginner`).

## Quality Assurance

### Review Process

#### Content Review
1. **Checklist**
   - Accuracy
   - Completeness
   - Consistency
   - Accessibility

2. **Technical Review**
   - Code quality
   - Performance
   - Security
   - Compatibility

### Testing

#### Types
1. **Automated**
   - Unit tests
   - Integration tests
   - End-to-end tests
   - Performance tests

2. **Manual**
   - User testing
   - Content review
   - Accessibility testing
   - Cross-browser testing

## Maintenance

### Updates

#### Regular Tasks
1. **Content**
   - Regular reviews
   - Version updates
   - Link checking
   - Image optimization

2. **Technical**
   - Dependency updates
   - Security patches
   - Performance optimization
   - Bug fixes

### Monitoring

#### Metrics
1. **Performance**
   - Load times
   - Response times
   - Error rates
   - Resource usage

2. **Usage**
   - Page views
   - User engagement
   - Content popularity
   - Search rankings

---

*These standards should be reviewed and updated regularly to ensure they remain relevant and effective.*
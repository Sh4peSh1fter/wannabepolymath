---
title: Technology Stack
description: An overview of the technologies that power the knowledge base.
tags:
  - topic:meta
  - type:reference
  - status:published
---

# Technology Stack

## Overview

This document outlines the technology decisions for the Wanna be Polymath project, including the rationale behind choosing specific technologies and the evaluation process for alternatives.

## Requirements Analysis

### Core Requirements

1. **Simplicity**
   - Easy to learn and maintain
   - Minimal complexity
   - Quick to implement

2. **Content Management**
   - Easy content creation
   - Consistent formatting
   - Version control support

3. **User Experience**
   - Fast loading
   - Responsive design
   - Intuitive navigation

4. **Performance**
   - Quick page loads
   - Efficient search
   - Minimal server requirements

## Architecture Decision Records (ADRs)

### ADR 1: Static Site Generator Selection

#### Status: Accepted

#### Context

Need a solution that balances simplicity with functionality for a content-focused website.

#### Decision

Use MkDocs with Material theme as the primary static site generator.

#### Rationale

- Markdown-based content creation
- Built-in search functionality
- Responsive design
- Active community
- Easy to deploy
- No database required
- Version control friendly

#### Alternatives Considered

1. **Jekyll**
   - Pros: Mature, large community
   - Cons: Ruby dependency, slower build times

2. **Hugo**
   - Pros: Fast build times, Go-based
   - Cons: Steeper learning curve

3. **Next.js**
   - Pros: Modern, flexible
   - Cons: Overkill for static content

4. **Docusaurus**
   - Pros: Feature-rich, React-based
   - Cons: More complex than needed

#### Consequences

- Positive:
  - Simple content management
  - Easy deployment
  - Good performance
- Negative:
  - Limited dynamic features
  - Basic search capabilities

### ADR 2: Hosting Solution

#### Status: Accepted

#### Context

Need reliable, cost-effective hosting for a static website.

#### Decision

Use GitHub Pages for hosting.

#### Rationale

- Free hosting
- Direct integration with Git
- Automatic deployment
- Good performance
- SSL support
- Custom domain support

#### Alternatives Considered

1. **Vercel**
   - Pros: Great performance, easy deployment
   - Cons: Free tier limitations

2. **Netlify**
   - Pros: Feature-rich, good free tier
   - Cons: More complex than needed

3. **Cloudflare Pages**
   - Pros: Global CDN, good performance
   - Cons: More complex setup

#### Consequences

- Positive:
  - Zero hosting costs
  - Simple deployment
  - Good reliability
- Negative:
  - Limited to static content
  - Basic analytics

## Implementation Details

### 1. Core Technologies

- **Static Site Generator**: MkDocs
- **Theme**: Material for MkDocs
- **Content Format**: Markdown
- **Version Control**: Git
- **Hosting**: GitHub Pages

### 2. Key Features

- **Search**: MkDocs Material built-in search
- **Navigation**: Custom navigation structure
- **Formatting**: Markdown with extensions
- **Analytics**: Google Analytics (optional)
- **Comments**: GitHub Issues (optional)

### 3. Development Workflow

1. **Content Creation**
   - Write in Markdown
   - Use consistent formatting
   - Follow naming conventions

2. **Version Control**
   - Git for content management
   - Branch-based workflow
   - Pull request reviews

3. **Deployment**
   - GitHub Actions for CI/CD
   - Automatic builds
   - Preview deployments

## Future Considerations

### Scalability

- Content growth handling
- Performance optimization
- Search improvements

### Feature Additions

- Comment system
- Newsletter integration
- Advanced analytics

### Maintenance

- Regular updates
- Security patches
- Performance monitoring

## Success Metrics

1. **Performance**
   - Page load times
   - Build times
   - Search response time

2. **Usability**
   - Content update frequency
   - User feedback
   - Navigation effectiveness

3. **Maintenance**
   - Update frequency
   - Issue resolution time
   - Documentation quality

## References

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages](https://pages.github.com/)

---

*This document should be reviewed and updated as new technologies emerge or project requirements change.*

# Tech Stack

Following our vision, we need to decide on a solution and its technology stack.

## Features We Want

we need it to fulfill all the "must have" features we are seeking.

- simple - not too complicated solution, easy to learn and apply technology.
- no overwhelming integrations - avoid too much third-party tools and integration.
- formatting and templating - have a way to easily template and format content we write so we can keep everything in the same standard.
- accessible table of contents - for easier navigation.
- search engine -
- analytics and statistics - gather and monitor data about the performance of the content and the feedback, to improve myself.

## Components

the technology stack should consist of part or all of the following components:

- Frontend - tools and frameworks that format and style the content of the web pages, their visual layout, interactivity with the user in the client side.
  - vanila (html, css, javascript), react js, next js, Tailwind CSS, docusaurus
- Backend - server side computing and handling requests.
  - node (with express.js), python (flask, django, fastapi)
- DB - store and manage data.
  - reddis, mysql, mongodb
- CI-CD - testing and deploying changes from the source code to the hosting endpoint.
  - github actions
- Other - ?
  - hugo, gatsby,

Im no frontend developer, I like python, and I think I can learn anything pretty fast, but I don't want to complicate stuff just because I can.

## Hosting

Where should I host the website? where should I get the domain?

- vercel
- github pages
- cloudflare
- netlify

> explain what each one demands and offers. for example github pages are free but work only with static pages(?).

# Common Solutions

- react.js with flask
- next.js with flask
- write markdown and use jekyll
- write markdown and use mkdocs

# Final Decision

mkdocs for now.

# sources of inspiration

## portfolios

1. <https://github.com/HamishMW/portfolio>
   - technology stack: next.js, three.js, remix
   - hosted: cloudflare
2.

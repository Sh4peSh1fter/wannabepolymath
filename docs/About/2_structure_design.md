---
title: Structure Design
description: How we organize and structure the Wanna be Polymath project
date: 27.5.2025
tags:
  - structure
  - organization
  - navigation
---

# Structure Design

Let's talk about how we're organizing everything in the Wanna be Polymath project, and make sure the structure is intuitive, flexible, and user-friendly.

## What We're Building

We're creating a space that needs to handle:
- Different types of content
- Various levels of depth
- Multiple disciplines
- Personal and community content

## Design Principles

We've set some ground rules to keep things clear and user-friendly:

1. Keep It Simple
    - Not too many sections
    - Clear, short names
    - Logical organization
    - Easy to navigate
2. Make It Flexible
    - Easy to rearrange
    - Adaptable to change
    - Encourages improvement
    - No rigid structure
3. Optimize Everything
    - Each piece has its perfect place
    - No unnecessary nesting
    - Clear navigation paths
    - No duplicate content

## Content Types

Here's what we're working with:

### Content Types
- Article
- Blog
- Post
- Guide / Tutorial
- Projects
- Topic maps (keywords, sources, etc)

### Content Themes
- Problem and solution (analysis / debate)
- Personal project development (Idea development)
- Learning guide (educational content)
- Topic exploration and mapping (keyword collection and deepdive)
- Daily random discoveries (random thoughts and facts)
- Weekly corner (action list that repeats each week, with a defined theme)

## Navigation Structure

The navigation structure is effected from the content types and themes, and we have few options to go with:

### Option 1: Type-Based (Less Recommended for Primary Structure)
Organizes content primarily by its format (e.g., Articles, Blogs, Projects).
- **Pros:** Clear for users looking for a specific *type* of content.
- **Cons:** Can be difficult to find all information on a specific *subject* if it exists in multiple formats. May feel too generic for the "Wanna be Polymath" vision.

```
├── Home/
├── About/
├── Articles/
│   ├── <group_of_articles_1>/
│   ├── <group_of_articles_2>/
│   └── ...
├── Blogs/
│   ├── <group_of_blogs_1>/
│   ├── <group_of_blogs_2>/
│   └── ...
├── Projects/
├── Topic_Maps/
│   ├── <group_of_topics_1>/
│   ├── <group_of_topics_2>/
│   └── ...
```

### Option 2: Topic-Based (Strong for Knowledge Organization)
Organizes content primarily by subject matter or discipline.
- **Pros:** Excellent for users seeking information on a specific topic. Familiar and intuitive for knowledge bases.
- **Cons:** Might obscure the unique *purpose-driven* sections you've envisioned (Round Table, Incubator, etc.) if these become secondary.

```
├── Home/
├── About/
├── Topics/
│   ├── <topic_A>/
│   │   ├── Overviews/
│   │   ├── Tutorials/
│   │   ├── Keyword_Maps/
│   │   └── Related_Projects/
│   ├── <topic_B>/
│   └── ...
├── Corners/ (For content not fitting neatly into topics, or for unique, recurring features)
│   ├── <group_of_corners_1>/
│   ├── <group_of_corners_2>/
│   └── ...
```

### Recommended Approach: Hybrid Thematic & Topic-Driven Structure

This approach combines the engaging nature of your theme-based "Corners" with the clarity of topic-based organization, aiming for the best of both worlds.

**Core Idea:**
-   **Primary Navigation by Thematic "Corners":** The main site sections are your uniquely named "Corners" (Round Table, Incubator, Academy, Observatory, Bazaar, Forge). These define the *purpose, style, and type of interaction* for the content within them.
-   **Strong Secondary Organization by "Topics":** Every piece of content, regardless of its Corner, is tagged with relevant topics/disciplines (e.g., DevOps, Neuroscience, Philosophy).
-   **Dedicated Topic Hub Pages:** For each major topic, a dedicated hub page is created. This page aggregates and links to all content related to that topic from *across all Corners*. For example, a "DevOps" topic page would show:
    *   Tutorials from the "Academy."
    *   Keyword definitions from the "Observatory."
    *   Problem discussions from the "Round Table."
    *   Relevant projects from the "Incubator."

**Proposed High-Level Structure:**

```
├── Home/
├── About/
├── Round_Table/ (Content focused on problems, solutions, discussions)
│   ├── <topic_A_discussion_1.md> (Tagged: topic_A)
│   └── <topic_B_problem_set.md> (Tagged: topic_B)
├── Incubator/ (Content focused on project development, ideas)
│   ├── <project_X_on_topic_A.md> (Tagged: topic_A, project_X)
│   └── <idea_Y_for_topic_C.md> (Tagged: topic_C, idea_Y)
├── Academy/ (Tutorials, guides, learning materials)
│   ├── <topic_A_tutorial.md> (Tagged: topic_A)
│   └── <topic_B_guide.md> (Tagged: topic_B)
├── Observatory/ (Keywords, concepts, maps of knowledge areas)
│   ├── <topic_A_keywords.md> (Tagged: topic_A)
│   └── <topic_D_concept_map.md> (Tagged: topic_D)
├── Bazaar/ (Random discoveries, facts, tagged appropriately)
│   └── <interesting_fact_about_topic_A.md> (Tagged: topic_A, random_discovery)
├── Forge/ (Self-improvement, tools, methods)
│   └── <productivity_technique.md> (Tagged: self_improvement, tools)
├── Topics/ (Dynamically generated or curated hub pages)
│   ├── <topic_A.md> (Aggregates all content tagged "topic_A")
│   ├── <topic_B.md> (Aggregates all content tagged "topic_B")
│   └── ...
└── Other_Corners/ (If needed for unique, non-topic-specific recurring content)
```

**Addressing Discoverability:**

This hybrid model tackles the discoverability challenge in several ways:
1.  **Thematic Exploration:** Users can browse by "Corner" if they're interested in a particular type of content or interaction (e.g., "I want to learn something new" -> Academy; "I want to explore problems and solutions" -> Round Table).
2.  **Topic-Focused Exploration:** Users can go to the "Topics" section or a specific Topic Hub page to find all content related to a subject they are interested in, regardless of where it "lives" thematically.
3.  **Powerful Search:** A robust search engine is crucial. It should allow filtering by:
    *   Keywords
    *   Tags (including Topics)
    *   Thematic "Corner"
    *   Content type (article, guide, project)
    *   Date, author (if applicable with community contributions)
4.  **Rich Tagging System:** As you plan, a well-defined set of tags (including topic tags, difficulty tags, content type tags) is essential.
5.  **Cross-Linking:** Manually and potentially automatically (e.g., "Related Articles" based on shared tags) link between content. For example, a tutorial in the Academy on a specific technology could link to its keyword definition in the Observatory and a project using it in the Incubator.
6.  **Clear Signposting:** Each piece of content should clearly indicate its primary "Corner" and associated "Topic(s)". Breadcrumbs should reflect this structure.

**Benefits of the Hybrid Approach:**
-   Maintains your project's unique, engaging thematic identity.
-   Provides clear pathways for users with different goals (browsing vs. specific search).
-   Scales well as you add more topics and content.
-   Encourages interdisciplinary connections by showing how different "Corners" can address the same topic.

This approach turns the potential trade-off you identified into a strength, offering multiple ways to navigate and discover knowledge.

I decided to divide it into 6 main sections (Corners), each unique in its purpose, style and content.

## Content Guidelines

### Templates
Each section includes:
- Clear introduction
- Purpose statement
- Content guidelines
- Contribution guide

### Naming Rules
- Use lowercase
- Hyphens for spaces
- Be descriptive
- Keep it short

### File Organization
- Group related content
- Clear hierarchies
- Consistent structure
- Easy to find

## Future Plans

### Growth
- Plan for more content
- Consider new sections
- Stay flexible
- Keep improving

### Maintenance
- Regular reviews
- Content audits
- Navigation checks
- User feedback

### Community
- Gather input
- Test changes
- Document updates
- Share improvements

## How We'll Know It Works

### Navigation
- Easy to find content
- Clear user paths
- Effective search
- Happy users

### Organization
- Content in right place
- Easy to update
- Clear structure
- No confusion

### User Experience
- Intuitive navigation
- Easy discovery
- Clear purpose
- Happy community

---

*This structure is designed to evolve with our needs. We'll keep reviewing and improving it as we grow.*

### Home

the landing page of the project. this is the first thing people will see so it should be eye catching, short and interesting.
there should be a "tip of the iceberg" explanation on the purpose, the vision, how to use it, how to navigate it, and how to contribute.

#### folder layout

```
1. introduction
2. how to use it + how to navigate
3. structure
4. how to contribute
```

#### guiding questions / theme

- what is this?
- how to start using it?
- where should I start?

### 1. Round Table

a place where I write down things that I view as potential problems, optional solutions to these problems, and projects that leverage the solutions to solve the problems in real life.

the goal is to be as objective and open minded as possible, list everything down, strategize, and discuss ways to make our world a better place, starting from a variety of smaller topics.

from here we can move ripe projects to the "Incubator" section where we actively work on them.

#### folder layout

```
1. introduction
2. templates
3. <topic 1>
   - problems
   - solutions
   - projects
4. ...
```

> how should I structure the "problems", "solutions", and "projects"? because some solutions might repeat themselves. talk about it in the templates.

#### guiding questions / theme

- what are the problems in this topic?
- what things could have negative effects in this topic?
- what solutions can solve those problems?
- what things could have positive effects and try resolve parts of the problems?
- what projects can we do using the solutions to solve the problems?

### 2. Incubator

used as a portfolio, listing all the projects and ideas I'm incubating and working on.
If there will be a community I will add it's projects here as well, or maybe list only them for more focused content following this website's vision.

#### folder layout

```
1. introduction
2. templates
3. ideas
    - <idea 1>
    - ...
4. projects
    - <project 1>
    - ...
```

#### guiding questions / theme

- what ideas do we have?
- what projects are we working on?

### 3. Academy

share tutorials, howtos, guides and troubleshooting journals on different subjects.
I want all of this to be delivered as best as possible, and in different ways like articles or videos.

#### folder layout

```
1. introduction
2. templates
3. <topic 1>
    - general articles
        - <article 1>
        - ...
    - howtos
        - <guide 1>
        - ...
    - issues
        - <troubleshooting journal 1>
        - ...
4. ...
```

> in the templates define what is "general article", "howto guide" and an "issue", what each consists of and how to decide where belongs each thing that I'm writing.

#### guiding questions / theme

- what should I know about the topic?
- how do I do stuff in this topic?
- What should I do when I get an issue in this topic?

### 4. Observatory

store collections of keywords that we encountered and want to acknowledge, understand and better remember.
this also allows us to sort of see a short (hopefully) map of the key things a topic consists of.

#### folder layout

```
1. introduction
2. <topic 1>
    - keywords
    - personals and organizations
3. ...
```

> think of a better way to divide the keywords into stuff, like: concepts, methods, etc.

#### guiding questions / theme

- what are the keyword of this topic?
- what should I know when learning about this topic?

### 5. Bazaar

share small and random day to day facts and things we have learned.

#### folder layout

```
1. introduction
2.
```

> I have no clue how to divide it as it pure randomness. maybe just to general topics is enough.

#### guiding questions / theme

-

### 6. Forge

talk about ourselves, what are we made of and how to improve ourselves generally and our day to day life.

#### folder layout

```
1. introduction
2. templates
3. tools and methods
3. mental
4. physical
```

#### guiding questions / theme

- how can I improve myself?
- what tools should I use to improve myself?

### About

a small about me page. also I might include here in depth stuff about the thought path of things in this project.

#### folder layout

```
1. about me
2. vision
3. in depth structure
4. formatting our page
```

#### guiding questions / theme

- what was the thinking path of this project?
- why things done as they do?

## op 2 - follow the way of thinking and doing

my way of thinking and doing stuff should be reflected in the structure. This journey can be mapped to the Corners:

1.  I see something that interests me in one of the sources I follow, or somewhere else. (Input to potentially any Corner, especially Bazaar or Observatory)
2.  I study it and write down useful information. (Academy, Observatory)
3.  I write down the main keywords in the topic that I studied. (Observatory)
4.  I think of problems and solutions in this topic, or new stuff that I can implement in other topics. (Round Table)
5.  I start incubating ideas and working on them. (Incubator)

the two additional things that I do are random blogs that are harder to organize under topics (Bazaar, with strong tagging), and self improvement and life stuff (Forge).

## op 3 - topics and corners (Integrated into the Hybrid Approach)

(This idea is now largely integrated into the "Recommended Approach: Hybrid Thematic & Topic-Driven Structure" above, where "Topics" become a primary way to aggregate and access content across the thematic "Corners".)

instead of focused places that each stores topics in its own unique structure, maybe its better to list all the topics and inside each one will be a place with unique structure.
and corners will be a more unique place to store stuff that didn't fit the topics.

for example:

1.  home
2.  topics
    1.  devops
        - sources (Could be part of a topic page, or linked from Observatory/Academy entries)
        - observatory (Content from the Observatory Corner, tagged 'devops')
        - ...
    2.  nutrition
3.  corners (These are the primary thematic sections in the hybrid model)
4.  about
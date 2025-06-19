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

This document dives into the organizational heart of the Wanna be Polymath project. Our goal is to craft a structure that feels intuitive, remains flexible as we grow, and makes it a joy for everyone to explore and contribute.

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
    - Content is easily discoverable through multiple pathways (browsing, search, tags).

## Content Types

Here's what we're working with, described in a more active way:

### Content Types
- Crafting insightful **Articles**
- Sharing experiences and thoughts via **Blog Posts**
- Delivering focused updates as **Posts**
- Creating comprehensive **Guides / Tutorials**
- Showcasing our work through **Projects**
- Mapping knowledge with **Topic Maps** (keywords, sources, etc.)

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
-   **Strong Secondary Organization by "Topics":** Every piece of content, regardless of its Corner, is *critically* tagged with relevant topics/disciplines (e.g., DevOps, Neuroscience, Philosophy). This tagging is the backbone of our topic-centric discoverability.
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
The `Other_Corners/` directory is a placeholder for any future unique, recurring content themes that don't fit existing Corners or Topic-based aggregation, ensuring flexibility.

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

Our project's structure, like knowledge itself, is designed to be a living thing. We're committed to regularly reviewing and refining it with our community's input to ensure it beautifully serves our collective journey of exploration and growth.

### Home

Our digital front porch! The landing page is the first glimpse into the Wanna be Polymath world, so it needs to be eye-catching, concise, and intriguing. It will offer a "tip of the iceberg" overview of the project's purpose, our shared vision, how to navigate the platform, and how you can jump in and contribute.

**Content Focus:**
-   A welcoming introduction to the project.
-   A concise explanation of the "Wanna be Polymath" philosophy (drawing from [Vision](./vision.md)).
-   Highlights of the main sections (Corners) and what users can find in each.
-   Clear calls to action (e.g., "Explore Our Corners," "Join the Discussion," "Contribute Your Knowledge").
-   Featured or recent content snippets to draw users in.

**Guiding Questions / Theme:**
-   What is this place all about?
-   How can I start exploring and learning?
-   Where should I begin my journey?

### 1. Round Table

This is our collaborative space for dissecting challenges and envisioning a better future. Here, we identify potential problems across various topics, brainstorm innovative solutions, and conceptualize projects that could bring these solutions to life. The spirit is objective, open-minded, and focused on actionable strategies for positive change. Promising projects identified here may graduate to the "Incubator" for active development.

**Content Organization:**
-   An introductory page explaining the Round Table's mission and approach.
-   Templates to guide structured discussions (e.g., problem definition, solution brainstorming, project outlining).
-   Dedicated sections or pages for each <topic> under discussion, typically containing:
    -   In-depth analyses of identified problems and their impacts.
    -   Detailed explorations of potential solutions, including pros, cons, and feasibility.
    -   Outlines or proposals for projects that could implement these solutions.

> **Note on Structuring Discussions:** We need to ensure templates allow for cross-referencing solutions that might apply to multiple problems or topics. This will be key for interdisciplinary insights.

**Guiding Questions / Theme:**
-   What are the pressing problems or overlooked challenges within this topic?
-   What are the potential negative impacts or risks we should consider?
-   What innovative solutions could address these problems effectively?
-   What positive changes or opportunities could arise from these solutions?
-   What tangible projects can we undertake to implement these solutions and make a real-world difference?

### 2. Incubator

The Incubator is our portfolio of active creation – a showcase of all the projects and fledgling ideas being nurtured and developed within the Wanna be Polymath community. It's where concepts turn into tangible outcomes. If our community grows, this space will also feature and perhaps focus on community-led projects, aligning with our open and collaborative vision.

**Content Organization:**
-   An introductory page detailing the Incubator's role in fostering innovation.
-   Templates for project proposals and progress documentation.
-   A section for **Ideas Under Development:**
    -   Descriptions and initial explorations for <idea 1>, <idea 2>, etc.
-   A section for **Active Projects:**
    -   Detailed pages for <project 1>, <project 2>, etc., including goals, progress, challenges, and outcomes.

**Guiding Questions / Theme:**
-   What exciting ideas are currently brewing in our community?
-   What innovative projects are we actively working on, and what progress are we making?

### 3. Academy

Welcome to the Academy, our center for learning and skill-sharing! This is where we publish tutorials, how-to guides, troubleshooting journals, and in-depth articles on a multitude of subjects. We're committed to delivering high-quality educational content in various formats, potentially including articles, videos, and interactive modules, to make learning as effective and engaging as possible.

**Content Organization:**
-   An introductory page outlining the Academy's educational mission.
-   Templates for different content types (e.g., general articles, how-to guides, troubleshooting logs).
-   Content organized by <topic>, further divided into:
    -   **General Articles:** Overviews, conceptual explanations, and foundational knowledge for <article 1>, <article 2>, etc.
    -   **How-To Guides:** Step-by-step instructions and practical tutorials for <guide 1>, <guide 2>, etc.
    -   **Troubleshooting Journals:** Documented solutions to common issues and challenges for <issue 1>, <issue 2>, etc.

> **Note on Content Definitions:** Templates should clearly define what constitutes a "general article," "how-to guide," and an "issue/troubleshooting journal," outlining their structure and helping contributors categorize their content effectively.

**Guiding Questions / Theme:**
-   What foundational knowledge is essential for understanding this topic?
-   How can I perform specific tasks or apply concepts within this topic?
-   What are common problems encountered in this topic, and how can I solve them?

### 4. Observatory

The Observatory is where we map the constellations of knowledge. It's a space to collect, define, and connect the key terms, concepts, influential figures, and organizations we encounter across various disciplines. This helps us (and you!) to better understand, remember, and navigate the essential landmarks of any given subject area.

**Content Organization:**
-   An introductory page explaining the Observatory's role in knowledge mapping.
-   Content structured by <topic>, containing:
    -   **Keywords & Concepts:** Definitions, explanations, and relationships between key terms.
    -   **Key Figures & Organizations:** Briefs on influential individuals and relevant organizations.

> **Note on Keyword Categorization:** We should explore a more granular way to categorize keywords, perhaps into concepts, methodologies, tools, principles, etc., to enhance clarity and searchability.

**Guiding Questions / Theme:**
-   What are the fundamental keywords and core concepts of this topic?
-   What essential terminology should I grasp to navigate this field of study effectively?

### 5. Bazaar

Step into the Bazaar, our vibrant marketplace of intriguing tidbits! This is where we share fascinating, small, and often random day-to-day facts, discoveries, and insights that we've stumbled upon. Content in the Bazaar will be highly diverse and perhaps a bit eclectic. Organization will primarily rely on robust tagging (by topic, keyword, date, etc.) to allow for flexible discovery. We might also explore curated collections or "featured random discoveries" over time to highlight interesting finds.

**Content Organization:**
-   An introductory page welcoming users to the serendipitous world of the Bazaar.
-   A flexible structure, likely a stream of posts or a grid, with strong emphasis on tagging for categorization and search. We might organize by broad interest areas if natural groupings emerge.

**Guiding Questions / Theme:**
-   What interesting, surprising, or useful tidbit did I learn or encounter today?
- (This section is intentionally open-ended to capture a wide array of brief insights)

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

This is the section you're currently exploring! It's the central hub for understanding everything *about* the project itself.

**Content Focus:**
-   The project's **[Vision](./vision.md)**.
-   This very **[Structure & Design](./structure_design.md)** document.
-   Our **[Inspiration](./taking_inspiration.md)** and the research behind our choices.
-   The **[Technology Stack](./tech_stack.md)** that powers the platform.

**Guiding Questions / Theme:**
-   What was the inspiration and thinking process behind this project?
-   Why are things designed and structured the way they are?

## The Polymath's Journey: How Our Structure Supports Exploration

(This section reframes the original "op 2 - follow the way of thinking and doing" to illustrate how the site's structure mirrors a natural learning and creation process.)

Our platform's structure is designed to mirror the way many of us naturally explore, learn, and create. Think of it as a journey:

1.  **Sparking Curiosity (Bazaar, Observatory, or external sources):** You encounter something interesting – a random fact in the `Bazaar`, a new keyword in the `Observatory`, or an idea from your daily life.
2.  **Deepening Understanding (Academy, Observatory):** You decide to learn more. You might seek out tutorials and guides in the `Academy` or explore related concepts and definitions in the `Observatory`.
3.  **Identifying Connections & Challenges (Round Table):** As you learn, you start seeing patterns, identifying problems, or thinking about potential solutions. The `Round Table` is where these critical thoughts are explored.
4.  **Bringing Ideas to Life (Incubator):** Promising ideas or solutions that emerge from the `Round Table` (or elsewhere) can then be developed into tangible projects within the `Incubator`.

And throughout this journey, the `Forge` is there to help you hone your own skills and mindset for effective learning and creation. This cyclical process of discovery, learning, critical thinking, and creation is what being a "Wanna be Polymath" is all about!

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
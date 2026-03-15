# Article Format Reference

## Post Directory and Filename Convention

Each day gets its own directory. The date appears only in the directory name, not the filename.

```
posts/YYYY-MM-DD/slugified-headline.md
```

Example:
```
posts/2024-03-05/congress-bans-wd40-storage-without-red-straw.md
```

Slugify aggressively: lowercase, hyphens, no special characters, no stop words if the slug exceeds ~60 characters.

---

## Front Matter

Every post must include this front matter. Do not add Jekyll-specific fields like `layout` inside posts — handle layout at the template level.

```yaml
---
title: "Congress Unanimously Bans Storage of WD-40 Cans Without the Little Red Straw That Goes With It"
date: YYYY-MM-DD
draft: true
writer: "David R. Ashworth"
tags: [congress, hardware, consumer-safety]
image: /posts/YYYY-MM-DD/slugified-headline.jpg
excerpt: "Lawmakers cited mounting evidence that the straws, once separated, are gone forever."
---
```

For opinion columns, also include:
```yaml
writer: "Gerald K. Vanderbeek"
column: "The Free Exchange"
```

### Field Rules
- **title** — Full headline. Formal NYT style. Capitalize major words. Can be long.
- **date** — ISO format. Use today's date unless specified otherwise.
- **draft** — Always set to `true` by default. Set to `false` only when explicitly ready to publish.
- **writer** — Full name of the assigned staff writer. Must match a wiki entry in `wiki/people/`.
- **column** — Column name, for opinion pieces only.
- **tags** — 2 to 5 tags. Lowercase, hyphenated. Draw from existing tags where possible before creating new ones.
- **image** — Path to the article image relative to the site root. Uses the article slug: `/posts/YYYY-MM-DD/slugified-headline.jpg`.
- **excerpt** — One sentence. Deadpan. This appears in article previews and should function as a secondary joke.

---

## Byline Format

Every article includes a byline after the image and before the dateline:

```markdown
**By Margaret Liu-Chen**
```

For opinion columns, use the column name as a prefix:

```markdown
**The Free Exchange | By Gerald K. Vanderbeek**
```

---

## Article Image

Every article must include a generated image placed in the same directory as the article Markdown file.

### Image Requirements
- **One image per article**, generated at article creation time using an image generation model via Replicate.
- **Filename:** Use the article slug with a `.jpg` extension (e.g., `congress-bans-wd40-storage-without-red-straw.jpg`), in the same directory as the post.
- **Style:** Photojournalistic. The image should look like a real newspaper photograph — no cartoons, no illustrations, no stock-photo glossiness. Match the deadpan tone of the article.
- **Prompt construction:** Describe the scene as a press photographer would see it. Include specific visual details (setting, lighting, expressions, clothing) that sell the premise as real. Never mention satire, humor, or absurdity in the image prompt.
- **Caption:** Every image must include a deadpan caption in the Markdown alt text. Write it as a newspaper photo caption — one sentence identifying the scene, attributed to a fake photographer or wire service when appropriate. Example: `![Keith Sorvino explaining his opening theory to an unpersuaded arbiter at the Elk Grove Community Chess Club on Tuesday. Credit: Daniel Voss/The Register](slug.jpg)`
- **Front matter:** Add an `image` field pointing to the image path relative to the site root.

### Directory Layout Example
```
posts/2024-03-05/
  congress-bans-wd40-storage-without-red-straw.md
  congress-bans-wd40-storage-without-red-straw.jpg
```

### Markdown Usage
Include the image at the top of the article body (after front matter, before the dateline) using:
```markdown
![Caption text describing the scene. Credit: Photographer Name/Agency](slug.jpg)
```

---

## Article Checklist

A post is ready to commit when:
- [ ] Markdown file exists in `/posts/YYYY-MM-DD/` with correct filename format
- [ ] Front matter is complete and valid (including `writer` field)
- [ ] Writer assigned and byline present in article body
- [ ] Article voice consistent with assigned writer's Private Profile
- [ ] Wiki consulted for reusable characters and organizations
- [ ] Dateline is present in the article body
- [ ] At least two fake attributed quotes included
- [ ] Generated image exists as `slugified-headline.jpg` in the post directory
- [ ] Image referenced in front matter and article body
- [ ] Image alt text contains a deadpan caption with photographer credit
- [ ] No meta-jokes or fourth-wall breaks in the body copy
- [ ] Excerpt functions as a standalone deadpan sentence
- [ ] First mention of every wiki-entry person/org/place is hyperlinked in the article body
- [ ] Wiki entries created for all new fictional people, organizations, and institutions
- [ ] Existing wiki entries updated with back-links to this article

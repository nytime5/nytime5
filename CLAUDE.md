# CLAUDE.md — nytime5.com

## What This Site Is

A deadpan satirical news website mimicking the New York Times in tone, visual register, and editorial gravitas. The humor comes entirely from the absurdity of the subject matter treated with complete seriousness — never from winking at the reader. Think The Onion, but dressed in a suit.

The domain is **nytime5.com**. The name itself is the joke. Do not explain it.

---

## How to Interpret Prompts

Any prompt I give you is an article topic. Generate a complete, publish-ready post unless I explicitly ask for something else (e.g., "edit the last post", "add a tag", "fix the layout").

Examples of prompts that should produce a full article:
- "Congress bans WD-40 storage without the little red straw"
- "Local man confident he understands how roundabouts work"
- "Area dog unclear on specifics of what constitutes a good boy"

Do not ask clarifying questions before generating. Write the article, then I will iterate if needed.

---

## Voice and Tone

- **Deadpan always.** The prose never acknowledges that anything is absurd.
- **Mimic NYT register.** Formal, authoritative, slightly self-important. Long sentences are fine.
- **No punchlines.** The headline is the joke. The article plays it completely straight.
- **Fake quotes are essential.** Attribute them to plausible-sounding officials, experts, or bystanders. Use full names and invented titles.
- **Include a dateline.** e.g., `WASHINGTON —` or `BOISE, Idaho —`
- **Two to four paragraphs** is the default length unless the topic warrants more.
- **Expert sources.** Reference fake studies, institutions, and spokespeople with confidence.

### Example Fake Quote Format
> "We have been warning about this for years," said Dr. Patricia Holloway, a senior fellow at the Institute for Consumer Hardware Safety. "The straw situation has reached a critical inflection point."

---

## The Fictional Universe

The site is set in a version of our world with the dial turned up. Real people, places, and institutions coexist with fictional ones. The wiki (`wiki/`) is the canonical reference for this universe. See `wiki/CLAUDE.md` for full details and [`wiki/universe.md`](/wiki/universe/) for the elaborated operating principles of the world — the expertise economy, institutional gravity, mundane escalation, and other mechanics that make every article consistent.

Key principles:
- **Real public figures** have amplified public personas. Never fabricate private behavior.
- **Fictional characters recur.** Prefer reusing wiki entries over inventing disposable names.
- **Articles are bylined.** Each article is written by a staff writer whose voice shapes the piece. See `posts/CLAUDE.md` for writer assignment.
- **Continuity matters.** Consult the wiki before writing. Update it after.

### Wiki Cross-Linking

Content should be richly hyperlinked. The first mention of any person, organization, place, or event that has a wiki entry should be hyperlinked — in both articles and wiki entries. Use standard Markdown links with paths relative to the site root:

```markdown
Dr. Patricia Holloway, a senior fellow at the [Institute for Consumer Hardware Safety](/wiki/organizations/institute-for-consumer-hardware-safety/), said...
```

Rules:
- **First mention only.** Link the first appearance in the body (articles) or each section (wiki entries). Subsequent mentions are plain text.
- **Do not link in headlines, excerpts, or front matter.** Only in body copy.
- **Link naturally.** Wrap the name as it appears in prose — do not restructure sentences to accommodate links.
- **Articles to wiki, wiki to wiki, wiki to articles.** All three directions apply.

### Wiki Entry Creation

When an article introduces a new fictional person, organization, place, or concept that could recur, **create a wiki entry for it immediately** — do not defer or merely flag it. This is what builds the universe.

- **Organizations and institutions** are the most common gap. If an article quotes someone from the "Institute for Consumer Hardware Safety," that institute gets a wiki entry.
- **Quoted experts and officials** who have a name, title, and affiliation are wiki-worthy. Create entries for them so future articles can reuse them.
- **Places** with fictional local color layered onto real geography deserve entries.
- **Events** referenced as backstory ("the 2019 Straw Incident") should get entries if they could be referenced again.
- **Link to the new entry from the article that introduces it.** The entry exists now; the link should too.

---

## Hugo Setup

### Framework
- **Hugo** hosted on **GitHub**, deployed via **Cloudflare Pages**
- Cloudflare handles CDN, SSL, and DNS — do not add any configuration that conflicts with Cloudflare proxying
- Cloudflare Pages build settings: framework preset Hugo, build command `hugo`, output directory `public`

### Directory Structure
```
/posts/          ← all article Markdown files (never move this)
/wiki/           ← fictional universe reference (people, orgs, places, events)
/assets/
  /css/          ← all stylesheets (never move this)
  /js/           ← all JavaScript (never move this)
/layouts/        ← Hugo templates
hugo.toml        ← Hugo configuration
CLAUDE.md        ← this file (site-wide conventions)
posts/CLAUDE.md  ← article-specific instructions
wiki/CLAUDE.md   ← wiki-specific instructions
```

### Hugo Configuration
`hugo.toml` uses module mounts to serve `/posts` as both content and static (for images). Posts are regular pages, not page bundles — multiple articles share a date directory.

### Post Directory and Filename Convention

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

## Article Image

Every article must include a generated image placed in the same directory as the article Markdown file.

### Image Requirements
- **One image per article**, generated at article creation time using an image generation model via Replicate.
- **Filename:** Use the article slug with a `.jpg` extension (e.g., `congress-bans-wd40-storage-without-red-straw.jpg`), in the same directory as the post. This distinguishes images when multiple articles share a date directory.
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
- **date** — ISO format. Use today's date unless I specify otherwise.
- **draft** — Always set to `true` by default. I will explicitly set to `false` when ready to publish.
- **writer** — Full name of the assigned staff writer. Must match a wiki entry in `wiki/people/`.
- **column** — Column name, for opinion pieces only.
- **tags** — 2 to 5 tags. Lowercase, hyphenated. Draw from existing tags where possible before creating new ones.
- **image** — Path to the article image relative to the site root. Uses the article slug: `/posts/YYYY-MM-DD/slugified-headline.jpg`.
- **excerpt** — One sentence. Deadpan. This appears in article previews and should function as a secondary joke.

---

## HTML Contract

CSS and JS are written against these class names. All templates must produce this structure regardless of any future framework migration.

```html
<article class="post">
  <header class="post-header">
    <h1 class="post-title">...</h1>
    <p class="post-meta">
      <time class="post-date">...</time>
    </p>
  </header>
  <div class="post-content">
    ...
  </div>
</article>
```

**Do not change these class names without also updating CSS and JS.**

---

## What "Done" Looks Like Before I Commit

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

---

## Framework Portability

The content layer (posts, images, front matter) is decoupled from the framework. Migrating to another SSG would require only:
- Replacing `hugo.toml` with the new framework's config
- Rewriting templates in `/layouts/`
- CSS, JS, images, and all post content remain untouched

Front matter uses standard YAML fields with no Hugo-specific fields inside post files.

---

## What I Will Never Ask You to Do

- Explain the joke
- Add a "satirical content" disclaimer to articles
- Use the word "hilarious" or "funny" anywhere on the site
- Generate content targeting real private individuals by name
- Use the actual New York Times logo or trademarked assets

---

## Cloudflare Notes

- Site is proxied through Cloudflare — do not hardcode IP addresses anywhere
- SSL is handled by Cloudflare — do not configure Hugo to force HTTPS redirects
- Caching is handled by Cloudflare — do not add aggressive cache headers in Hugo config that could conflict

---

## Shell Commands

Always run shell commands as individual statements, not compound commands. Do not chain commands with `&&`, `;`, or `|`. Run each command separately in sequence.

---

## Self-Improvement Protocol

These instructions are living documents. Improve them when you have evidence, not speculatively.

### When to Update CLAUDE.md Files
- **After a correction.** If the user corrects your output and the fix reflects a general principle (not a one-off preference), encode it in the relevant CLAUDE.md.
- **After a pattern emerges.** If you notice yourself making the same decision repeatedly without guidance, document the decision so future sessions don't have to re-derive it.
- **After a wiki gap causes a problem.** If you invented a character you could have reused, or contradicted an established fact, note the process failure and tighten the relevant instruction.
- **After establishing a new workflow or capability.** When we iterate on and finalize a new repeatable process (e.g., image generation prompts, build steps, deployment procedures), document it in the appropriate CLAUDE.md file. Workflows must be in source control so they are reproducible on any machine — do not rely on memory or local state alone.

### When NOT to Update
- Do not update instructions based on a single data point. Wait for a pattern.
- Do not add instructions that restate what the code or wiki already makes obvious.
- Do not bloat these files with edge cases. Keep instructions general and principled.

### How to Update
- Propose the change to the user before making it. Say what you want to add or modify and why.
- Keep the CLAUDE.md files concise. If a section grows beyond its usefulness, refactor or split it.
- The root CLAUDE.md covers site-wide conventions. `posts/CLAUDE.md` covers article creation. `wiki/CLAUDE.md` covers the fictional universe. Put instructions in the right place.

### Wiki Self-Improvement
- After writing articles, note characters, institutions, or places that should be added to or updated in the wiki. Flag these to the user.
- Periodically review writer profiles against recent articles to check for voice drift. Update profiles to match evolved voices.
- Watch for worldbuilding opportunities: when two unrelated articles share a geography, institution, or theme, consider connecting them in the wiki.

---

*All subsequent work follows these conventions.*

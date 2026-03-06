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

## Jekyll Setup

### Framework
- **Jekyll** hosted on **GitHub**, deployed via **Cloudflare Pages**
- Cloudflare handles CDN, SSL, and DNS — do not add any configuration that conflicts with Cloudflare proxying

### Directory Structure
```
/posts/          ← all article Markdown files (never move this)
/assets/
  /css/          ← all stylesheets (never move this)
  /js/           ← all JavaScript (never move this)
  /images/       ← article images and site assets
/_layouts/       ← Jekyll templates
/_includes/      ← Jekyll partials
/_config.yml     ← Jekyll configuration
CLAUDE.md        ← this file
```

### Jekyll Configuration
`_config.yml` must point Jekyll to `/posts` as the posts directory so posts never need to move if the framework changes in the future.

### Post Filename Convention
```
posts/YYYY-MM-DD-slugified-headline.md
```

Example:
```
posts/2024-03-05-congress-bans-wd40-storage-without-red-straw.md
```

Slugify aggressively: lowercase, hyphens, no special characters, no stop words if the slug exceeds ~60 characters.

---

## Front Matter

Every post must include this front matter. Do not add Jekyll-specific fields like `layout` inside posts — handle layout at the template level.

```yaml
---
title: "Congress Unanimously Bans Storage of WD-40 Cans Without the Little Red Straw That Goes With It"
date: YYYY-MM-DD
tags: [congress, hardware, consumer-safety]
excerpt: "Lawmakers cited mounting evidence that the straws, once separated, are gone forever."
---
```

### Field Rules
- **title** — Full headline. Formal NYT style. Capitalize major words. Can be long.
- **date** — ISO format. Use today's date unless I specify otherwise.
- **tags** — 2 to 5 tags. Lowercase, hyphenated. Draw from existing tags where possible before creating new ones.
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
- [ ] Markdown file exists in `/posts/` with correct filename format
- [ ] Front matter is complete and valid
- [ ] Dateline is present in the article body
- [ ] At least two fake attributed quotes included
- [ ] No meta-jokes or fourth-wall breaks in the body copy
- [ ] Excerpt functions as a standalone deadpan sentence

---

## Future Framework Compatibility

This repo is designed so that migrating from Jekyll to Hugo (or another framework) requires only:
- Updating build configuration to point to `/posts/`
- Replacing templates in `/_layouts/` and `/_includes/`
- CSS, JS, images, and all post content remain untouched

Front matter must stay compatible with both Jekyll and Hugo. Avoid Jekyll-specific front matter fields inside post files.

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
- SSL is handled by Cloudflare — do not configure Jekyll to force HTTPS redirects
- Caching is handled by Cloudflare — do not add aggressive cache headers in Jekyll config that could conflict

---

*This is the first file committed to the repo. All subsequent work follows these conventions.*

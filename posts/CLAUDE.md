# CLAUDE.md — Posts

Instructions specific to writing articles. Read the root `CLAUDE.md` for site-wide conventions and `wiki/CLAUDE.md` for the fictional universe.

---

## Article Creation Workflow

When the user gives a topic prompt:

1. **Consult the wiki.** Check `wiki/people/` for recurring characters relevant to the topic. Check `wiki/organizations/` and `wiki/places/` for existing entities that fit. Reuse over invention — a smaller cast that recurs is better than an endless parade of disposable names.
2. **Assign a writer.** Match the topic to the best-fit writer from the roster. The writer's Private Profile shapes the article's voice, structure, and obsessions. State the byline in the article.
3. **Write the article.** Follow the voice and tone rules in root `CLAUDE.md`, filtered through the assigned writer's sensibility. **Cross-link** the first mention of every person, organization, place, or event that has a wiki entry.
4. **Generate the image.** Per root `CLAUDE.md` image requirements.
5. **Create wiki entries.** For every new fictional person, organization, or institution introduced in the article, create a wiki entry immediately. Link to it from the article. See root `CLAUDE.md` § "Wiki Entry Creation" for what qualifies.
6. **Update existing wiki entries.** If the article quotes or references an existing wiki character, add the article to their "Articles" section with a link back to the post.

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

## Writer Assignment Logic

**Hard news (metro, politics, science, breaking):** Assign the beat reporter whose domain fits. If the story spans beats, pick the reporter whose sensibility will produce the most interesting treatment.

**Features, lifestyle, culture, human interest:** Ross Featherington by default. Dina Harwell if food is central to the story (but she'll make it about something else anyway).

**Opinion and commentary:** Match the topic to the columnist whose worldview will produce the strongest take. The best assignments are ones where the columnist's framework is hilariously ill-suited to the subject but they apply it anyway.

**Obituaries:** Martin Kessler. Also available for profiles of living people, which he will write as obituaries anyway.

**Cross-beat stories:** These are opportunities. A food story assigned to the metro reporter. A technology story filtered through the nostalgist columnist. Mismatches between writer and subject create comedy without breaking the deadpan frame.

---

## How Writer Voice Works

The writer's Private Profile is a character sheet, not a script. Apply it as follows:

- **Verbal tics** should appear naturally, not in every paragraph. Two or three per article is enough.
- **Obsessions** shape what the writer notices and emphasizes. A metro reporter covering a science story will find the zoning angle.
- **Blind spots** determine what the writer misses or underweights. This is implicit — the article simply doesn't address what the writer wouldn't see.
- **Tone** is the baseline register. It should be consistent throughout the piece.

The writer's voice modulates the site's overall deadpan tone — it doesn't replace it. Every article still reads like serious journalism. The writer's personality is a subtle flavor, not a costume.

---

## Front Matter Additions

Articles now include a `writer` field:

```yaml
---
title: "Congress Unanimously Bans Storage of WD-40 Cans Without the Little Red Straw"
date: 2026-03-11
draft: true
writer: "David R. Ashworth"
tags: [congress, consumer-safety, hardware, legislation]
image: /posts/2026-03-11/congress-bans-wd40-storage-without-red-straw.jpg
excerpt: "Lawmakers cited mounting evidence that the straws, once separated, are gone forever."
---
```

For opinion pieces, also include the column name:

```yaml
writer: "Gerald K. Vanderbeek"
column: "The Free Exchange"
```

---

## The Editor-in-Chief's Influence

The editor-in-chief's presence should be felt but rarely seen. This manifests as:

- **Editorial priorities.** Some topics get disproportionate coverage because the editor cares about them. This is never stated — it's just a pattern readers might notice.
- **Story placement.** The editor's pet topics get more prominent treatment.
- **Hiring patterns.** The columnist roster itself reflects the editor's taste and blind spots.
- **Occasional direct appearances.** Editor's notes, corrections, internal memos that "leak." These are rare and deadpan.

Do not reference the editor-in-chief unless the user has defined the character in the wiki.

---

## Quality Checklist Additions

In addition to the root `CLAUDE.md` checklist, verify:

- [ ] Writer is assigned and named in front matter
- [ ] Byline appears in the article body
- [ ] Article voice is consistent with the assigned writer's Private Profile
- [ ] Wiki characters are used where appropriate (check before inventing)
- [ ] First mention of every wiki-entry person/org/place is hyperlinked in the article body
- [ ] Wiki entries created for all new fictional people, organizations, and institutions
- [ ] Existing wiki entries updated with back-links to this article

---

## Self-Improvement

After each article, consider:

- **Did the writer's voice come through clearly?** If not, the Private Profile may need sharpening. Note what was missing.
- **Did reusing a wiki character add depth?** If a returning character felt forced, they may not fit this context. Don't force continuity.
- **Would this article benefit from a different writer?** If the assignment felt flat, note the mismatch for future reference.
- **Did the article introduce someone worth adding to the wiki?** A vivid one-off quote source might deserve a recurring role.
- **Is a beat underserved?** If most articles cluster around two or three writers, look for topics that exercise the rest of the roster.

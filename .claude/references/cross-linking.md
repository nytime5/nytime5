# Cross-Linking Rules

Content should be richly hyperlinked. The first mention of any person, organization, place, or event that has a wiki entry should be hyperlinked — in both articles and wiki entries. Use standard Markdown links with paths relative to the site root:

```markdown
Dr. Patricia Holloway, a senior fellow at the [Institute for Consumer Hardware Safety](/wiki/organizations/institute-for-consumer-hardware-safety/), said...
```

## General Rules

- **First mention only.** Link the first appearance in the body (articles) or each section (wiki entries). Subsequent mentions are plain text.
- **Do not link in headlines, excerpts, or front matter.** Only in body copy.
- **Link naturally.** Wrap the name as it appears in prose — do not restructure sentences to accommodate links.

## Articles → Wiki

The first mention of any entity with a wiki entry gets a link to the wiki page.

## Wiki → Wiki (inter-linking)

Link between wiki entries when entities are related. A person's entry should link to the organization they lead. An organization entry should link to its director. An event entry should link to the people and places involved.

- **First mention per section**, same as articles. Link the name naturally in prose.
- Example: In Dr. Holloway's entry, the first mention of the Institute for Consumer Hardware Safety links to `/wiki/organizations/institute-for-consumer-hardware-safety/`.

## Wiki → Articles (back-links)

Every wiki entry should include an **Articles** section listing the posts where the person, organization, or place appears. Use markdown links to the actual post permalink paths:

```markdown
## Articles

- [Congress Unanimously Bans Storage of WD-40 Cans Without the Little Red Straw](/2026/03/11/congress-bans-wd40-storage-without-red-straw/) — quoted as lead expert on straw retention policy
```

Update this section each time the entity appears in a new article.

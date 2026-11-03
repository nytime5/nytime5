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

Photo captions are never linked. Whatever the dateline names, usually a place, is normally left unlinked there and linked at its first mention in the prose. When the dateline is the only mention, link it in the dateline: `[PASADENA](/wiki/places/pasadena/), Calif. —`.

## Wiki → Wiki (inter-linking)

Link between wiki entries when entities are related. A person's entry should link to the organization they lead. An organization entry should link to its director. An event entry should link to the people and places involved.

- **First mention per section**, same as articles. Link the name naturally in prose.
- Example: In Dr. Holloway's entry, the first mention of the Institute for Consumer Hardware Safety links to `/wiki/organizations/institute-for-consumer-hardware-safety/`.

## Wiki → Articles (back-links)

Back-links are generated, not written. Each wiki entry's **Articles** list is built at render time by `layouts/partials/wiki-articles.html`. It lists every published post whose body links to the entry and, for a writer, every post carrying their byline. A post appears on an entry once it is published and links the entry, and never earlier, so a back-link cannot point at an unpublished draft.

Do not add an `## Articles` section to an entry's markdown: the page would show two Articles headings. The Articles → Wiki rule above is what creates a back-link. The match is on the entry's exact path, trailing slash included (`/wiki/places/pasadena/`), anywhere in the article's markdown. An article that names an entity without linking it is not listed on the entity's page, and neither is one that names it only in a photo caption. So when you create an entry for an entity that published posts already name, link its first mention in each of those posts.

**A post's URL is `/YYYY-MM-DD/slug/`** — the date directory verbatim, then the filename without its extension. It is *not* `/YYYY/MM/DD/slug/`. Hugo derives this from the post's directory name (`posts/2026-03-11/` becomes the section `2026-03-11`); there is no permalink rewriting in `hugo.toml`, and none should be added, because every published URL and every inbound link depends on this shape. Use it wherever a wiki entry or another article links to a post.

```
posts/2026-03-11/congress-bans-wd40-storage-without-red-straw.md
  →  /2026-03-11/congress-bans-wd40-storage-without-red-straw/
```

`npm run check` fails the build on any internal link that does not resolve, so a wrong path is caught before it ships rather than 404ing silently in production.

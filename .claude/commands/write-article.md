---
description: Write a complete article from a topic prompt — assigns writer, generates image, creates wiki entries.
---

Write a complete, publish-ready article for nytime5.com. The argument is the topic prompt.

## Workflow

1. **Read references.** Read `.claude/references/article-format.md` and `.claude/references/cross-linking.md` for format specs and linking rules.

2. **Consult the wiki.** Check `wiki/people/` for recurring characters relevant to the topic. Check `wiki/organizations/` and `wiki/places/` for existing entities that fit. Reuse over invention — a smaller cast that recurs is better than an endless parade of disposable names.

3. **Assign a writer.** Match the topic to the best-fit writer from the roster (see `posts/CLAUDE.md` for assignment logic and roster). Read the assigned writer's wiki profile to internalize their Private Profile — verbal tics, obsessions, blind spots, and tone. State the byline in the article.

4. **Write the article.** Follow the voice and tone rules in root `CLAUDE.md`, filtered through the assigned writer's sensibility. Cross-link the first mention of every person, organization, place, or event that has a wiki entry.

5. **Generate the image.** Use the image requirements from the article-format reference. Use the Replicate MCP tool to generate a photojournalistic image. Save it as `slugified-headline.jpg` in the post directory.

6. **Create wiki entries.** For every new fictional person, organization, place, or institution introduced in the article, create a wiki entry immediately. Use `/create-wiki-entry` or read `.claude/references/wiki-entry-format.md` for the format. Link to each new entry from the article.

7. **Update existing wiki entries.** If the article quotes or references an existing wiki character, add the article to their "Articles" section with a link back to the post using its permalink path (`/YYYY/MM/DD/slug/`).

8. **Verify against checklist.** Review the checklist in `.claude/references/article-format.md` before finishing.

## Post-Article Reflection

After completing the article, briefly consider:
- Did the writer's voice come through? If not, their Private Profile may need sharpening.
- Did reusing a wiki character add depth, or feel forced?
- Did the article introduce someone worth a recurring role?
- Are any beats underserved in recent articles?

Flag observations to the user only if actionable.

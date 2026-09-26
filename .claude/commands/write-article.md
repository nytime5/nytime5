---
description: Write and publish a complete article from a topic prompt — assigns writer, generates image, creates wiki entries, commits, and pushes.
---

Write a complete article for nytime5.com and publish it. The argument is the topic prompt.

Publishing is the default: the article ships with `draft: false`, is committed, and is pushed. If the user asks to hold it — "draft", "don't publish", "let me review it first" — set `draft: true` and stop after step 9. `/publish` finishes the job later.

## Workflow

1. **Read references.** Read `.claude/references/article-format.md` and `.claude/references/cross-linking.md` for format specs and linking rules.

2. **Consult the wiki.** Check `wiki/people/` for recurring characters relevant to the topic. Check `wiki/organizations/` and `wiki/places/` for existing entities that fit. Reuse over invention — a smaller cast that recurs is better than an endless parade of disposable names.

3. **Assign a writer.** Match the topic to the best-fit writer from the roster (see `posts/CLAUDE.md` for assignment logic and roster). Read the assigned writer's wiki profile to internalize their Private Profile — verbal tics, obsessions, blind spots, and tone. State the byline in the article.

4. **Write the article.** Follow the voice and tone rules in root `CLAUDE.md`, filtered through the assigned writer's sensibility. Cross-link the first mention of every person, organization, place, or event that has a wiki entry.

5. **Generate the image.** Use the image requirements from the article-format reference. Use the Replicate MCP tool to generate a photojournalistic image. Save it as `slugified-headline.jpg` in the post directory.

6. **Create wiki entries.** For every new fictional person, organization, place, or institution introduced in the article, create a wiki entry immediately. Use `/create-wiki-entry` or read `.claude/references/wiki-entry-format.md` for the format. Link to each new entry from the article.

7. **Update existing wiki entries.** If the article quotes or references an existing wiki character, add the article to their "Articles" section with a link back to the post using its permalink path (`/YYYY/MM/DD/slug/`).

8. **Verify against checklist.** Review the checklist in `.claude/references/article-format.md` before finishing.

9. **Run the gate.** `npm run check` must pass — it builds the site with and without drafts and fails on any broken internal link. On a failure, fix the article or wiki entries and rerun. Never weaken the check, and never commit or push on red.

10. **Commit.** Run `git status` and stage only what this article created or changed: the post, its image, and new or updated wiki entries. Leave unrelated working-tree changes unstaged. Use the article's headline as the commit message subject.

11. **Sync.** Run `git pull --rebase`, then `git push`. The push is the deploy: Workers Builds runs `npm run deploy` on it (see `.claude/references/hugo-setup.md`). If the pull conflicts or the push is rejected, stop and report — never force-push.

12. **Report.** Give the commit hash and the article URL, `https://nytime5.com/YYYY-MM-DD/slug/`. The build runs on Cloudflare after the push, so say the article was pushed, not that it is live, unless you have fetched the URL and seen it.

## Post-Article Reflection

After completing the article, briefly consider:
- Did the writer's voice come through? If not, their Private Profile may need sharpening.
- Did reusing a wiki character add depth, or feel forced?
- Did the article introduce someone worth a recurring role?
- Are any beats underserved in recent articles?

Flag observations to the user only if actionable.

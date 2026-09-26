---
description: Publish a held draft article — sets draft to false, commits, and pushes.
---

Publish a draft article by setting `draft: false`, committing, and pushing. `/write-article` already publishes by default; this is for an article the user asked to hold as a draft.

## Workflow

1. **Identify the article.** The argument is the article slug, filename, or a recent topic description. If ambiguous, list recent drafts and ask the user to confirm.

2. **Find the file.** Look in `posts/` for the matching Markdown file.

3. **Set draft to false.** Edit the front matter to change `draft: true` to `draft: false`.

4. **Verify completeness.** Read `.claude/references/article-format.md` and check the article against the checklist. Flag any missing items to the user before committing.

5. **Run the gate.** `npm run check` must pass. Never weaken the check, and never commit or push on red.

6. **Commit.** Stage the changed file and create a commit. Use the article's headline as the commit message subject.

7. **Sync.** Run `git pull --rebase`, then `git push`. The push is the deploy (Workers Builds). If the pull conflicts or the push is rejected, stop and report — never force-push.

8. **Report.** Give the commit hash and the article URL, `https://nytime5.com/YYYY-MM-DD/slug/`. Say it was pushed, not that it is live, unless you have fetched the URL and seen it.

---
description: Publish a draft article — sets draft to false and commits.
---

Publish a draft article by setting `draft: false` and committing the changes.

## Workflow

1. **Identify the article.** The argument is the article slug, filename, or a recent topic description. If ambiguous, list recent drafts and ask the user to confirm.

2. **Find the file.** Look in `posts/` for the matching Markdown file.

3. **Set draft to false.** Edit the front matter to change `draft: true` to `draft: false`.

4. **Verify completeness.** Read `.claude/references/article-format.md` and check the article against the checklist. Flag any missing items to the user before committing.

5. **Commit.** Stage the changed file and create a commit. Use the article's headline as the commit message subject.

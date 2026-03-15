---
description: Recommend a staff writer for a given topic without writing the article.
---

Given a topic, recommend the best staff writer assignment. The argument is the topic or headline.

## Workflow

1. **Read the roster.** Check `wiki/CLAUDE.md` for the current roster of beat reporters and opinion columnists.

2. **Identify the beat.** Determine which beat(s) the topic falls under. Consult `posts/CLAUDE.md` for assignment logic:
   - Hard news (metro, politics, science, breaking) → beat reporter whose domain fits
   - Features, lifestyle, culture → Ross Featherington; food → Dina Harwell
   - Opinion and commentary → columnist whose worldview produces the strongest take
   - Obituaries → Martin Kessler
   - Cross-beat stories are opportunities for comic mismatch

3. **Read the writer's profile.** Pull up the recommended writer's wiki entry (`wiki/people/`) to confirm the match — their obsessions and blind spots should interact interestingly with the topic.

4. **Present the recommendation.** State the recommended writer, why they're a good fit, and what angle their voice would bring to the topic. If a cross-beat mismatch would be funnier, suggest that too.

5. **Do not write the article.** This skill is advisory only. The user can then invoke `/write-article` with the topic if they agree.

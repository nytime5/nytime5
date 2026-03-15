# CLAUDE.md — nytime5.com

## What This Site Is

A deadpan satirical news website mimicking the New York Times in tone, visual register, and editorial gravitas. The humor comes entirely from the absurdity of the subject matter treated with complete seriousness — never from winking at the reader. Think The Onion, but dressed in a suit.

The domain is **nytime5.com**. The name itself is the joke. Do not explain it.

---

## How to Interpret Prompts

Any prompt I give you is an article topic. Invoke the `/write-article` skill to generate a complete, publish-ready post unless I explicitly ask for something else (e.g., "edit the last post", "add a tag", "fix the layout").

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

The site is set in a version of our world with the dial turned up. Real people, places, and institutions coexist with fictional ones. The wiki (`wiki/`) is the canonical reference for this universe. See `wiki/CLAUDE.md` for full details and [`wiki/universe.md`](/wiki/universe/) for the elaborated operating principles of the world.

Key principles:
- **Real public figures** have amplified public personas. Never fabricate private behavior.
- **Fictional characters recur.** Prefer reusing wiki entries over inventing disposable names.
- **Articles are bylined.** Each article is written by a staff writer whose voice shapes the piece. See `posts/CLAUDE.md` for writer assignment.
- **Continuity matters.** Consult the wiki before writing. Update it after.
- **Wiki entries are mandatory.** When an article introduces a new fictional person, organization, place, or concept that could recur, create a wiki entry immediately.

---

## What I Will Never Ask You to Do

- Explain the joke
- Add a "satirical content" disclaimer to articles
- Use the word "hilarious" or "funny" anywhere on the site
- Generate content targeting real private individuals by name
- Use the actual New York Times logo or trademarked assets

---

## Shell Commands

Always run shell commands as individual statements, not compound commands. Do not chain commands with `&&`, `;`, or `|`. Run each command separately in sequence.

---

## Reference Files and Skills

Detailed format specs, templates, and procedural workflows live in `.claude/references/` and `.claude/commands/` rather than in these CLAUDE.md files. Consult them when performing the specific task:

**References** (`.claude/references/`):
- `article-format.md` — front matter, image spec, byline format, filename convention, checklist
- `wiki-entry-format.md` — entry front matter (all subtypes), required sections, place guidelines
- `cross-linking.md` — linking rules for articles↔wiki↔wiki
- `hugo-setup.md` — Hugo framework, directory structure, HTML contract, Cloudflare notes

**Skills** (`.claude/commands/`):
- `/write-article` — full article creation workflow (invoked automatically for bare topic prompts)
- `/create-wiki-entry` — create a wiki entry for a person, organization, place, or event
- `/headshot` — generate a staff photo for a wiki person
- `/assign-writer` — recommend a writer for a topic without writing the article
- `/publish` — set draft to false and commit

---

## Self-Improvement Protocol

These instructions are living documents. Improve them when you have evidence, not speculatively.

### When to Update
- **After a correction** that reflects a general principle, not a one-off preference.
- **After a pattern emerges** — document decisions you keep re-deriving.
- **After a wiki gap causes a problem** — tighten the relevant instruction.
- **After establishing a new workflow** — document it in source control (CLAUDE.md, references, or skills).

### When NOT to Update
- Do not update based on a single data point. Wait for a pattern.
- Do not add instructions that restate what the code or wiki already makes obvious.
- Do not bloat these files with edge cases. Keep instructions general and principled.

### How to Update
- Propose the change to the user before making it.
- The root CLAUDE.md covers site-wide conventions. `posts/CLAUDE.md` covers article voice and writer assignment. `wiki/CLAUDE.md` covers the fictional universe. Put instructions in the right place.
- Format specs and procedural steps go in `.claude/references/` or `.claude/commands/`, not here.

---

*All subsequent work follows these conventions.*

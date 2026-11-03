---
description: Create a wiki entry for a person, organization, place, or event.
---

Create a wiki entry for the specified entity. The argument is the entity name and optionally its type (e.g., "Institute for Consumer Hardware Safety, organization" or "Dr. Patricia Holloway").

## Workflow

1. **Read references.** Read `.claude/references/wiki-entry-format.md` for front matter structure, required sections, and type-specific fields. Read `.claude/references/cross-linking.md` for linking rules.

2. **Check for duplicates.** Search `wiki/` to confirm this entity doesn't already exist under a different name or slug. Then search `posts/` for the name: once the entry exists, link the first mention in each published post that already names the entity, or those posts stay off its page (see `.claude/references/cross-linking.md`).

3. **Determine type and subtype.** Infer from context or ask the user:
   - `person` — expert, official, bystander, beat-reporter, opinion-columnist
   - `organization` — institute, agency, corporation, club, association
   - `place` — city, town, neighborhood, landmark, building
   - `event` — past incidents referenced as backstory

4. **Choose the file path.** Place the entry in the appropriate subdirectory:
   ```
   wiki/people/slugified-name.md
   wiki/organizations/slugified-name.md
   wiki/places/slugified-name.md
   wiki/events/slugified-name.md
   ```

5. **Write the entry.** Include:
   - **Front matter** with all required and type-specific fields.
   - **Public Biography / Public Profile** — deadpan, encyclopedic, entertaining standalone. Specific details: fake credentials, publications, career histories, notable statements.
   - **Private Profile** — behavioral and personality notes for generation. Written well enough to eventually publish as "behind the scenes" content.
   - **No Articles section.** The page lists every published article that links to it, generated at render time (see `.claude/references/cross-linking.md`). A hand-written list renders a second Articles heading.

6. **Cross-link.** Link to related wiki entries (people → their organizations, organizations → their directors, etc.) on first mention per section.

7. **For place entries**, follow the Place Entry Guidelines in the wiki-entry-format reference: start from reality, turn the dial up, give the place reputations and fixations, include concrete specifics.

8. **For multiverse counterparts or evil twins**, include the appropriate front matter fields and ensure headshot requirements account for visual resemblance.

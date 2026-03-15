# CLAUDE.md — Wiki

The wiki is the canonical reference for the fictional universe of *The New York Time5*. It is the bible that all article writing draws from and contributes to. Consistency across articles depends on consulting the wiki before writing and updating it after.

---

## Purpose

The wiki serves two audiences:

1. **The AI (you).** Before writing any article, consult relevant wiki entries to maintain continuity — character voices, institutional history, prior events. After writing, update or create entries for any new people, organizations, or places introduced.
2. **The reader (eventually).** Wiki entries will be browsable on the site. The public sections must stand alone as entertaining, deadpan content in their own right.

---

## The Fictional Universe

The world of *The New York Time5* is a hybrid of reality and fiction. It is our world with the dial turned up. The full elaboration of how this world works — its expertise economy, institutional gravity, data fetish, legislative seriousness, and core mechanic of mundane escalation — is documented in [`wiki/universe.md`](/wiki/universe/). Consult that entry before writing to internalize the world's operating principles.

Summary of the boundary rules:

- **Real public figures** appear with amplified versions of their *public* personas. Never fabricate private behavior. A senator known for long speeches becomes a senator whose filibusters cause structural damage.
- **Fictional notable people** — experts, officials, institute directors — populate the world as recurring characters with consistent histories.
- **Fictional everyday people** — bystanders, neighbors, local business owners — provide quotes and grounding.
- **Organizations** are a mix of real (amplified) and fictional. Fictional institutions should sound plausible enough to momentarily fool a reader.
- **Places** are real geography with exaggerated local character. Every city, town, or neighborhood that appears in a story gets a wiki entry describing the place in a way that motivates the satire set there.

The amplification must always be of public, observable traits — never invented scandal or private behavior attributed to real people.

---

## Directory Structure

```
wiki/
  people/          ← all person entries (real and fictional)
  organizations/   ← institutes, agencies, companies, clubs
  places/          ← towns, buildings, landmarks
  events/          ← past incidents that articles reference as backstory
```

Create subdirectories as needed. Do not nest deeper than one level below `wiki/`.

---

## Entry Format

Every wiki entry uses this front matter structure:

```yaml
---
title: "Dr. Patricia Holloway"
type: person
subtype: expert              # e.g., expert, official, bystander, beat-reporter, opinion-columnist
status: active               # active, deceased, retired, defunct (for orgs)
first-appearance: 2026-03-11 # date of first article reference
---
```

### Required Sections

**Public Biography / Public Profile** — the section readers will see. Written in the same deadpan, encyclopedic register as the articles. For people: career history, credentials, notable statements. For organizations: mission, history, leadership. For places: location, significance, notable events.

**Private Profile** — behavioral and personality notes used for generation. For writers, this is the character sheet that shapes their voice. For recurring sources, this guides how they speak and what they care about. May eventually become public as a "behind the scenes" feature, so write it well — not as rough notes.

### Additional Front Matter by Type

**Writers (beat-reporter, opinion-columnist):**
```yaml
beat: metro                  # or politics, science-technology, culture-lifestyle, food, obituaries
column: "Column Name"        # opinion columnists only
political-lean: libertarian  # opinion columnists only
```

**Real public figures:**
```yaml
real-person: true
amplification: "known trait pushed to absurd logical extreme"
```

**Multiverse counterparts** (see [`wiki/universe.md`](/wiki/universe/) for full details):
```yaml
multiverse-counterpart: "Real Person Name"   # replaces the real person entirely
```

**Evil multiverse twins** (see [`wiki/universe.md`](/wiki/universe/) for full details):
```yaml
evil-twin-of: "Real Person Name"             # coexists with the real person
origin: "transporter accident, 2019"         # how the twin arrived
```

**Headshots for counterparts and evil twins:** Characters with `multiverse-counterpart` or `evil-twin-of` fields must have headshots that visually resemble their real-world counterpart — a doppelganger effect. For evil twins, add sinister visual cues: slightly dramatic lighting with shadow on one side of the face, unsettling stare, asymmetric smirk, high-collar clothing casting shadows. The resemblance reinforces the satirical connection between the fictional and real figures.

**Organizations:**
```yaml
subtype: institute           # institute, agency, corporation, club, association
headquarters: "Washington, D.C."
```

**Places:**
```yaml
subtype: city                # city, town, neighborhood, landmark, building
state: "Idaho"               # U.S. state or country
population: "~230,000"       # approximate, for flavor
```

### Place Entry Guidelines

Every city, town, or neighborhood that appears in a story must have a wiki entry. The entry should describe the place with exaggerated local character that makes it a natural setting for satire.

- **Start from reality, then turn the dial up.** A place known for its tech industry becomes pathologically optimized. A quiet suburb becomes aggressively, almost threateningly quiet. A college town becomes insufferably credentialed.
- **Give places reputations, fixations, and sore spots.** These are what make a place generative for future stories. A town obsessed with its one claim to fame. A city that takes its zoning laws personally. A neighborhood locked in a decades-long feud with the neighborhood across the highway.
- **Include concrete specifics.** Local institutions, recurring civic disputes, notable infrastructure, signature complaints. These details give future articles material to draw from.
- **The exaggeration should motivate the satire.** When a story is set in a particular place, the reader should feel that *of course* this would happen *there*. The place entry provides that inevitability.
- **Layer fiction onto real geography.** Use real locations, real climate, real regional culture — then push the local identity to a comic extreme. Do not invent fictional cities when a real one will do.

---

## The Writer Roster

The paper has a staff of writers, each with a distinct voice. Articles are bylined.

### Writer Assignment

When the user provides a topic:
1. Identify the most natural beat for the story.
2. Assign the writer whose beat and sensibility best fit.
3. Write the article in that writer's voice, shaped by their Private Profile.
4. If the story falls between beats, that tension is itself a source of comedy — a sports reporter covering city council, an obituary writer profiling someone alive.

The user may override writer assignment by specifying a writer or beat.

### Current Roster

**Beat reporters:** Margaret Liu-Chen (metro), David R. Ashworth (politics), Caroline Banks (science/tech), Ross Featherington (features/lifestyle), Martin Kessler (obituaries), Dina Harwell (food), Amara Okafor-Williams (business/economics), Priya Chandrasekaran (education), Tariq El-Amin (international), Jerome T. Halliday (sports/recreation)

**Opinion columnists:** Gerald K. Vanderbeek (libertarian), Judith Ann Crossley (nostalgist), Frank J. DiOrio (law-and-order), Kevin Shao (techno-optimist), Nancy Ostrander (localist), Dr. Elena Voss (environmentalist), Graham T. Weatherstone (centrist), Raúl Alejandro Guzmán (historical-determinist), Kristoffer Kitchens (contrarian-polemicist)

---

## Continuity Rules

- **Check before creating.** Before inventing a new expert, institution, or place, search the wiki for an existing one that fits. Reuse builds the world; proliferation dilutes it.
- **Create entries for new introductions.** If an article introduces a new fictional person, organization, or institution, create a wiki entry immediately — do not defer. This is mandatory, not optional.
- **No contradictions.** If Dr. Holloway was skeptical of federal hardware policy in March, she should not be enthusiastic about it in April without an explanation.
- **Accumulate, don't reset.** Characters should develop over time. Positions harden. Obsessions deepen. The columnists should slowly become more themselves.

---

## Cross-Linking Requirements

Wiki entries must be richly cross-linked in three directions:

### Wiki → Articles (back-links)
Every wiki entry should include an **Articles** section listing the posts where the person, organization, or place appears. Use markdown links to the actual post paths:

```markdown
## Articles

- [Congress Unanimously Bans Storage of WD-40 Cans Without the Little Red Straw](/2026/03/11/congress-bans-wd40-storage-without-red-straw/) — quoted as lead expert on straw retention policy
```

Update this section each time the entity appears in a new article.

### Wiki → Wiki (inter-linking)
Link between wiki entries when entities are related. A person's entry should link to the organization they lead. An organization entry should link to its director. An event entry should link to the people and places involved.

- **First mention per section**, same as articles. Link the name naturally in prose.
- Example: In Dr. Holloway's entry, the first mention of the Institute for Consumer Hardware Safety links to `/wiki/organizations/institute-for-consumer-hardware-safety/`.

### Articles → Wiki
Covered in root `CLAUDE.md` § "Wiki Cross-Linking." First mention of any entity with a wiki entry gets a link.

---

## What Makes a Good Entry

- **Standalone entertaining.** A reader landing on a wiki page with no context should find it interesting.
- **Deadpan throughout.** Same register as the articles. No winking.
- **Specific details.** Fake credentials, publications, career histories, and notable statements make entries feel real.
- **Internally consistent.** Every detail in an entry should be compatible with every other detail.
- **Generative.** A good entry suggests future stories. A character's obsessions, blind spots, and history should naturally produce situations worth covering.

---

## Self-Improvement

As the wiki grows, watch for these opportunities:

- **Connections between entries.** When two characters, organizations, or events naturally relate, link them. The wiki should become a web, not a list.
- **Gaps in coverage.** If articles keep inventing one-off experts in a domain, that domain needs a wiki character.
- **Staleness.** If a character hasn't appeared in many articles, consider whether they need development or retirement.
- **Voice drift.** Periodically reread writer Private Profiles to ensure articles stay true to each voice. If a writer's voice has evolved through use, update the profile to match.
- **World coherence.** The fictional universe should feel consistent. If two entries imply contradictory facts about the world, reconcile them.

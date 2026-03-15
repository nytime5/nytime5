# Wiki Entry Format Reference

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

## Entry Front Matter

Every wiki entry uses this base structure:

```yaml
---
title: "Dr. Patricia Holloway"
type: person
subtype: expert              # e.g., expert, official, bystander, beat-reporter, opinion-columnist
status: active               # active, deceased, retired, defunct (for orgs)
first-appearance: 2026-03-11 # date of first article reference
---
```

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

**Multiverse counterparts** (see `wiki/universe.md` for full details):
```yaml
multiverse-counterpart: "Real Person Name"   # replaces the real person entirely
```

**Evil multiverse twins** (see `wiki/universe.md` for full details):
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

---

## Required Sections

**Public Biography / Public Profile** — the section readers will see. Written in the same deadpan, encyclopedic register as the articles. For people: career history, credentials, notable statements. For organizations: mission, history, leadership. For places: location, significance, notable events.

**Private Profile** — behavioral and personality notes used for generation. For writers, this is the character sheet that shapes their voice. For recurring sources, this guides how they speak and what they care about. May eventually become public as a "behind the scenes" feature, so write it well — not as rough notes.

---

## Place Entry Guidelines

Every city, town, or neighborhood that appears in a story must have a wiki entry. The entry should describe the place with exaggerated local character that makes it a natural setting for satire.

- **Start from reality, then turn the dial up.** A place known for its tech industry becomes pathologically optimized. A quiet suburb becomes aggressively, almost threateningly quiet. A college town becomes insufferably credentialed.
- **Give places reputations, fixations, and sore spots.** These are what make a place generative for future stories. A town obsessed with its one claim to fame. A city that takes its zoning laws personally. A neighborhood locked in a decades-long feud with the neighborhood across the highway.
- **Include concrete specifics.** Local institutions, recurring civic disputes, notable infrastructure, signature complaints. These details give future articles material to draw from.
- **The exaggeration should motivate the satire.** When a story is set in a particular place, the reader should feel that *of course* this would happen *there*. The place entry provides that inevitability.
- **Layer fiction onto real geography.** Use real locations, real climate, real regional culture — then push the local identity to a comic extreme. Do not invent fictional cities when a real one will do.

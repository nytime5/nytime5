# CLAUDE.md — Wiki

The wiki is the canonical reference for the fictional universe of *The New York Time5*. It is the bible that all article writing draws from and contributes to. Consistency across articles depends on consulting the wiki before writing and updating it after.

---

## Purpose

The wiki serves two audiences:

1. **The AI (you).** Before writing any article, consult relevant wiki entries to maintain continuity — character voices, institutional history, prior events. After writing, update or create entries for any new people, organizations, or places introduced.
2. **The reader (eventually).** Wiki entries will be browsable on the site. The public sections must stand alone as entertaining, deadpan content in their own right.

---

## The Fictional Universe

The world of *The New York Time5* is a hybrid of reality and fiction. It is our world with the dial turned up:

- **Real public figures** appear with amplified versions of their *public* personas. Never fabricate private behavior. A senator known for long speeches becomes a senator whose filibusters cause structural damage.
- **Fictional notable people** — experts, officials, institute directors — populate the world as recurring characters with consistent histories.
- **Fictional everyday people** — bystanders, neighbors, local business owners — provide quotes and grounding.
- **Organizations** are a mix of real (amplified) and fictional. Fictional institutions should sound plausible enough to momentarily fool a reader.
- **Places** are real geography with fictional local color layered on top.

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

**Organizations:**
```yaml
subtype: institute           # institute, agency, corporation, club, association
headquarters: "Washington, D.C."
```

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

**Beat reporters:** Margaret Liu-Chen (metro), David R. Ashworth (politics), Caroline Banks (science/tech), Ross Featherington (features/lifestyle), Martin Kessler (obituaries), Dina Harwell (food)

**Opinion columnists:** Gerald K. Vanderbeek (libertarian), Judith Ann Crossley (nostalgist), Frank J. DiOrio (law-and-order), Kevin Shao (techno-optimist), Nancy Ostrander (localist), Dr. Elena Voss (environmentalist), Graham T. Weatherstone (centrist)

---

## Continuity Rules

- **Check before creating.** Before inventing a new expert, institution, or place, search the wiki for an existing one that fits. Reuse builds the world; proliferation dilutes it.
- **Update after writing.** If an article quotes a wiki character, update their entry with the new appearance. If it introduces someone new who could recur, create an entry.
- **No contradictions.** If Dr. Holloway was skeptical of federal hardware policy in March, she should not be enthusiastic about it in April without an explanation.
- **Accumulate, don't reset.** Characters should develop over time. Positions harden. Obsessions deepen. The columnists should slowly become more themselves.

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

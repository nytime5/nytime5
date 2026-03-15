---
description: Generate a headshot for the specified person.
---

## Input

The argument is a person's name (e.g., "Jerome T. Halliday") or a physical description. If a name is given, look up their wiki profile in `wiki/people/` for physical description details. If no wiki entry exists, ask the user for a brief physical description.

## Model and Settings

- **Model:** `black-forest-labs/flux-1.1-pro` on Replicate (via `create_models_predictions`)
- **Settings:** `aspect_ratio: "1:1"`, `output_format: "jpg"`, `output_quality: 90`, `safety_tolerance: 5`

## Prompt Template

```
Close-up headshot photograph of [physical description],
[imperfections: e.g. five o'clock shadow, slight bags under eyes, visible pores and skin texture],
frame includes full head with all hair visible and a small margin above,
bottom of frame cuts at the adam's apple showing just a hint of shirt collar,
plain off-white background, flat even lighting, not retouched,
135mm lens, professional newspaper staff photo
```

## Key Principles

- **Imperfections are essential.** Include skin texture, stubble, under-eye bags, slightly messy hair. These prevent the "AI headshot" look.
- **Anti-glamour lighting.** Always "flat even lighting, not retouched" — never studio lighting or dramatic shadows.
- **Framing for circular crop.** The head must be centered with enough margin on all sides that a circle inscribed in the square won't clip hair, ears, or chin. No shirt/shoulders — just a hint of collar at the bottom edge. These are displayed as 120x120px circles (CSS `border-radius: 50%`).
- **Lens choice.** 135mm gives a tight portrait without macro distortion.
- **Physical descriptions** should be adapted from the person's wiki profile when available. Vary age, ethnicity, hair, clothing details, and expression to match the character.

## Output

Save the headshot as a `.jpg` colocated with the person's wiki profile (e.g., `wiki/people/jerome-t-halliday.jpg`). If no wiki entry exists, save to the path specified by the user.

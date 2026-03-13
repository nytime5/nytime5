Generate a staff writer headshot for the specified writer.

## Input

The argument is a writer name (e.g., "Jerome T. Halliday"). Look up their wiki profile in `wiki/people/` to get physical description details.

## Model and Settings

- **Model:** `black-forest-labs/flux-1.1-pro` on Replicate (via `create_models_predictions`)
- **Settings:** `aspect_ratio: "1:1"`, `output_format: "jpg"`, `output_quality: 90`, `safety_tolerance: 5`

## Prompt Template

```
Close-up headshot photograph of [physical description from wiki profile],
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
- **Physical descriptions** should be adapted from each writer's wiki profile. Vary age, ethnicity, hair, clothing details, and expression to match the character.

## Output

Save the headshot as a `.jpg` in the same directory as the writer's wiki profile (e.g., `wiki/people/jerome-t-halliday.jpg`).

---
description: Generate a headshot for the specified person.
---

## Input

The argument is a person's name (e.g., "Jerome T. Halliday") or a physical description. If a name is given, look up their wiki profile in `wiki/people/` for physical description details. If no wiki entry exists, ask the user for a brief physical description.

## Determine Workflow

Check the person's wiki front matter for `multiverse-counterpart` or `evil-twin-of` fields:

- **If present → use the Doppelganger Workflow** (face-reference generation via PuLID)
- **If absent → use the Standard Workflow** (text-only generation via Flux 1.1 Pro)

---

## Standard Workflow

### Model and Settings

- **Model:** `black-forest-labs/flux-1.1-pro` on Replicate (via `create_models_predictions`)
- **Settings:** `aspect_ratio: "1:1"`, `output_format: "jpg"`, `output_quality: 90`, `safety_tolerance: 5`

### Prompt Template

```
Close-up headshot photograph of [physical description],
[imperfections: e.g. five o'clock shadow, slight bags under eyes, visible pores and skin texture],
frame includes full head with all hair visible and a small margin above,
bottom of frame cuts at the adam's apple showing just a hint of shirt collar,
plain off-white background, flat even lighting, not retouched,
135mm lens, professional newspaper staff photo
```

---

## Doppelganger Workflow

Used when the person has a `multiverse-counterpart` or `evil-twin-of` field. This workflow uses a reference photo of the real public figure to generate a headshot that preserves their facial identity.

### Step 1: Find a Reference Photo

Fetch the real person's Wikipedia page image via the MediaWiki API:

```
curl -s "https://en.wikipedia.org/w/api.php?action=query&titles=[PERSON_NAME]&prop=pageimages&format=json&pithumbsize=500"
```

Extract the `thumbnail.source` URL from the response. Download the image to `/tmp/` using curl with a `User-Agent` header (Wikimedia blocks requests without one).

### Step 2: Upload to Replicate

Upload the downloaded reference photo to Replicate's file hosting so the model can access it:

```
curl -s -X POST https://api.replicate.com/v1/files \
  -H "Authorization: Bearer $REPLICATE_API_TOKEN" \
  -H 'Content-Type: multipart/form-data' \
  -F 'content=@/tmp/[filename];type=image/jpeg;filename=[filename]'
```

Extract the file URL from the response: `urls.get` field.

### Step 3: Generate with PuLID

- **Model:** `zsxkib/flux-pulid` on Replicate (via `create_predictions`)
- **Version:** `8baa7ef2255075b46f4d91cd238c21d31181b3e6a864463f967960bb0112525b`
- **Settings:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| `main_face_image` | Replicate file URL from Step 2 | Required |
| `prompt` | See prompt template below | |
| `width` | `896` | Square for circular crop |
| `height` | `896` | |
| `id_weight` | `1.2` | Slightly above default for strong resemblance |
| `start_step` | `0` | Maximum identity fidelity |
| `num_steps` | `20` | |
| `guidance_scale` | `4` | |
| `output_format` | `png` | Model does not support "jpg" |
| `output_quality` | `90` | |
| `num_outputs` | `2` | Generate two options for the user to pick |

### Doppelganger Prompt Template

For **multiverse counterparts:**
```
Close-up headshot photograph of [physical description],
[imperfections: e.g. slight bags under eyes, visible pores and skin texture],
frame includes full head with all hair visible and a small margin above,
bottom of frame cuts at the adam's apple showing just a hint of shirt collar,
plain off-white background, flat even lighting, not retouched,
135mm lens, professional newspaper staff photo
```

For **evil twins**, add sinister elements:
```
Close-up headshot photograph of [physical description],
[imperfections: e.g. slight bags under eyes, visible pores and skin texture],
slightly dramatic lighting with shadow on one side of face, unsettling stare, asymmetric smirk,
frame includes full head with all hair visible and a small margin above,
bottom of frame cuts at the adam's apple showing just a hint of shirt collar,
off-white background, not retouched,
135mm lens, professional newspaper staff photo
```

### Step 4: Present Options

Show both generated images to the user. Save the chosen image as a `.png` file.

---

## Key Principles

- **Imperfections are essential.** Include skin texture, stubble, under-eye bags, slightly messy hair. These prevent the "AI headshot" look.
- **Anti-glamour lighting.** Always "flat even lighting, not retouched" — never studio lighting or dramatic shadows. (Exception: evil twins get slightly dramatic lighting.)
- **Framing for circular crop.** The head must be centered with enough margin on all sides that a circle inscribed in the square won't clip hair, ears, or chin. No shirt/shoulders — just a hint of collar at the bottom edge. These are displayed as 120x120px circles (CSS `border-radius: 50%`).
- **Lens choice.** 135mm gives a tight portrait without macro distortion.
- **Physical descriptions** should be adapted from the person's wiki profile when available. Vary age, ethnicity, hair, clothing details, and expression to match the character.

## Output

Save the headshot colocated with the person's wiki profile (e.g., `wiki/people/jerome-t-halliday.jpg`). Use `.jpg` for standard workflow, `.png` for doppelganger workflow. If no wiki entry exists, save to the path specified by the user.

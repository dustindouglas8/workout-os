# Exercise Media + Cue Source Strategy

## Purpose

Workout OS should not link users to a generic exercise website. Each exercise in the generated HTML needs a mapped media/cue record tied to the exact Workout OS exercise ID.

The goal is:
- One-click cue/video access from the exercise card.
- Stable fallback if a source lacks the exact movement.
- Clear source quality and review status.
- No generic links that force the user to search again.

---

## Recommended Source Stack

### Tier 1 — Structured Exercise Data

Use for canonical metadata, muscle tags, equipment, substitutions, and app-ready media records.

| Source | Best Use | Strengths | Weaknesses | Workout OS Use |
|---|---|---|---|---|
| ExerciseDB OSS | Structured exercise IDs, GIF media, body part/equipment/target metadata | API-like structure, 1,500+ exercises, GIF previews | Non-commercial attribution limits; not always enough coaching nuance | Candidate structured fallback and media seed |
| EDB Exercise Intelligence | App-ready dataset with GIFs, substitutions, progressions, regressions, taxonomy | Built for workout apps; relationship data is useful for substitutions | Paid/product dependency | Best paid option if we want durable mapping |
| PlainExercise | Written cues, equipment tags, common mistakes, safer alternatives | Structured text and plain-language cueing; free to browse | No videos | Strong cue fallback and validation source |
| Wrkout API | Exercise info, images, videos, audio instructions | Media-rich and API-first | Paid/API dependency; verify licensing | Candidate if video-first product quality is required |

### Tier 2 — Public Reference Libraries

Use for individual exercise page links and human review.

| Source | Best Use | Strengths | Weaknesses | Workout OS Use |
|---|---|---|---|---|
| ACE Exercise Library | Credible cert-org source, general fitness videos and exercise pages | Good authority; body-part organization | Not all Workout OS exercises; pages can be broad | Reference source for common exercises and warm-up education |
| NASM Exercise Library | Exercise and stretch instructions | Cert-org authority; good for flexibility/corrective style content | May not cover ring/calisthenics variants | Good for warm-up, corrective, and mobility cues |
| Virtuagym Exercise Library | Free video exercise pages, broad equipment/muscle filters | Large video library; equipment and difficulty filters | External site UX, source-specific names may differ | Video fallback for common gym movements |
| Fitbod Exercise Pages | Professionally filmed exercise pages and instructions | Large library; practical gym demos | Commercial source; mapping stability must be checked | Human-review source for common strength exercises |

### Tier 3 — Warm-Up / Mobility Education

Use to design warm-up logic, not as direct media for every card.

| Source | Best Use | Workout OS Use |
|---|---|---|
| ACE Dynamic Warm-Up PDF | Tissue/neuromuscular readiness drill cues | Warm-up drill cue validation |
| NASM dynamic stretching articles | Warm-up sequencing and dynamic mobility rationale | Warm-up architecture guidance |

---

## Recommendation

Use a local Workout OS mapping table. Do not rely on one external site.

The mapping table should live beside `exercises.md` as:

```text
exercise-media-map.md
```

or, if the generator prefers structured data:

```text
exercise-media-map.json
```

The generator should read this table and attach exact source links to each exercise card. If an exercise has no exact mapping, the generated app should show `media pending`, not a generic search-site link.

---

## Required Mapping Fields

Each Workout OS exercise gets a media/cue record:

```yaml
- workout_os_id: jefferson_curl
  display_name: Jefferson Curl
  source_status: needs_review
  primary_source:
    provider: custom
    url:
    media_type: none
    match_type: exact
    license_notes: pending
  fallback_sources:
    - provider: NASM
      url:
      media_type: article/video
      match_type: related
      note: use for spinal mobility cue validation, not exact Jefferson curl demo
    - provider: PlainExercise
      url:
      media_type: text
      match_type: related
      note: use for common mistakes / safety language if exact page exists
  cue_pack:
    setup:
    execution:
    breathing:
    common_mistakes: []
    contraindications: []
  warmup_transfer:
    mobility_unlock:
    neural_prime:
    ramp_rule:
  reviewed_by:
  reviewed_date:
```

---

## Match Types

| Match Type | Meaning | App Behavior |
|---|---|---|
| exact | Same exercise and same equipment/context | Show source as primary media |
| close_variant | Same pattern but different equipment or setup | Show with "variant" label |
| related | Useful cue source but not the same movement | Use for cue validation only; do not display as demo |
| contraindicated | Source movement conflicts with Workout OS version | Do not show |
| missing | No approved source | Show `media pending` |

---

## Source Status

| Status | Meaning |
|---|---|
| missing | No mapped source yet |
| candidate | Found but not reviewed |
| needs_review | Looks useful but needs human check |
| approved | Correct movement, correct context, acceptable source |
| rejected | Wrong movement, bad cueing, poor match, or licensing issue |

---

## App Rendering Rules

1. Exercise cards link to exact mapped media only.
2. Never render a generic provider homepage as the exercise link.
3. If the exact exercise is unavailable, render `Media pending` plus local cues.
4. If only a close variant exists, label it clearly:
   - `Video: close variant — DB version`
   - `Cue source: related, not exact demo`
5. Warm-up cards use the same media map but prefer short local cue packs over external links.
6. Exercise Library can show multiple sources; active workout cards should show at most one primary media link and one cue drawer.

---

## Initial Source Selection By Exercise Type

| Workout OS Type | Primary Source Strategy | Notes |
|---|---|---|
| Common strength movement | EDB / ExerciseDB / Fitbod / Virtuagym | Good video/GIF coverage likely |
| Kettlebell / dumbbell movement | Fitbod / Virtuagym / EDB | Check equipment match |
| Bodyweight / calisthenics | EDB / Virtuagym / Fitbod | Rings may need custom or close variants |
| Corrective / warm-up drill | ACE / NASM / PlainExercise | Prioritize cue quality over flashy video |
| Mobility / end-range skill | NASM / ACE / custom review | Avoid random influencer links unless reviewed |
| Ring-specific skill | Custom or expert-reviewed source | Many generic libraries lack exact ring context |

---

## First Mapping Pass

Start with these Workout OS exercises because they are high-use and currently user-facing:

| Workout OS ID | Exercise | Mapping Priority | Notes |
|---|---|---:|---|
| ring_push_up | Ring Push-Up | High | May require close variant if source only has push-up |
| ring_fly | Ring Fly | High | Needs exact ring context or custom |
| kb_goblet_squat | KB Goblet Squat | High | Common, easy to map |
| kb_bulgarian_split_squat | KB Bulgarian Split Squat | High | Need setup cue |
| pull_up_strict | Pull-Up Strict | High | Common |
| ring_row | Ring Row | High | TRX/suspension row may be close variant |
| kb_romanian_deadlift | KB Romanian Deadlift | High | Common |
| nordic_hamstring_curl | Nordic Hamstring Curl | High | Safety-sensitive |
| jefferson_curl | Jefferson Curl | High | Safety-sensitive; exact source required or media pending |
| skin_the_cat | Skin the Cat | High | Skill-specific; likely custom/reviewed only |
| pancake_stretch | Pancake Stretch | High | Must clarify duration/holds |
| pike_stretch | Pike Stretch | High | Must clarify active/passive sequence |
| band_external_rotation | Band External Rotation | High | Prehab staple |
| dead_bug | Dead Bug | High | Common |
| tibialis_raise | Tibialis Raise | Medium | May need custom |
| single_leg_soleus_raise | Single-Leg Soleus Raise | Medium | May need close variant |

---

## Generator Validation

Before HTML generation, fail or warn:

- Exact exercise has no approved/candidate media record.
- Exercise card points to a generic provider homepage.
- Source match is `related` but app tries to display it as a demo.
- Safety-sensitive exercise has no contraindication cue.
- Warm-up drill has no one-line execution cue.
- Timed mobility exercise has no total duration definition.


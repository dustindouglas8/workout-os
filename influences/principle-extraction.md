# Principle Extraction Method

## Purpose

This file defines how Workout OS should translate expert influence into usable system rules without copying routines.

## Extraction Pipeline

```text
Expert idea
  -> Principle
  -> Workout OS rule
  -> Module or field
  -> Exercise/progression/log behavior
  -> Test or gate
```

## Example

```text
Influence: Nippard-style evidence-based hypertrophy
Principle: enough hard sets, managed proximity to failure
Rule: hypertrophy accessories use 1-3 RIR unless readiness is Yellow
Module: exercise card RIR field
Behavior: Yellow changes 2 RIR to 4 RIR or drops accessory
Gate: progress only if reps improve and pain/readiness are stable
```

## Source Types

| Source Type | Use |
|---|---|
| Official public source | Best for bio, claims, system definitions |
| Book or paid material user owns | Use as private reference; extract principles only |
| Public YouTube/video | Use for cue ideas and public principles; do not transcribe full content |
| Scientific paper | Use for high-stakes claims and physiology rules |
| Personal experience | Use as Dustin-specific notes, not universal rules |

## High-Fidelity Extraction Checklist

For every influence-derived rule, record:

- Source or origin.
- Domain: hypertrophy, rehab, mobility, strength, conditioning, skill, nutrition.
- Principle in one sentence.
- When it applies.
- When it does not apply.
- How it changes exercise selection, dose, progression, or logging.
- Safety guardrail.
- Example sequence written originally for Workout OS.

## What Not To Do

- Do not paste paid program days, week tables, meal plans, or proprietary progressions.
- Do not use a famous coach's name as proof.
- Do not mix incompatible methods in the same phase without deciding the hierarchy.
- Do not add principles that the app cannot operationalize.

## Method Hierarchy

When influences conflict:

1. Safety and pain rules win.
2. User recovery status wins.
3. Current block goal wins.
4. Equipment reality wins.
5. Preference wins only after the above are satisfied.

## Current Workout OS Synthesis

```text
Nippard -> hypertrophy dose and progression discipline
Cavaliere -> joint-aware exercise choice and pain-aware substitution
Starrett -> position-first movement and daily maintenance
McGill -> spine-sparing core and hinge guardrails
Verkhoshansky -> block sequencing and special strength progression
Simmons -> variation, weak-point accessories, concurrent qualities
Francis -> high-low weekly stress organization
Poliquin -> tempo and structural balance
Myers -> chain-based reasoning
FRC -> active range and daily joint control
```

## Output Locations

| Extracted Idea | Goes In |
|---|---|
| Philosophy or big principle | `philosophy.md` |
| Annual/block planning | `annual-roadmap.md` |
| Daily recovery or readiness | `recovery-model.md`, `daily-practice.md` |
| Exercise cue or substitution | `exercises.md` |
| Progression rule or test | `progressions.md` |
| UI behavior | `screens.md`, `html-design-notes.md` |
| User-specific preference | `program-config.md` |


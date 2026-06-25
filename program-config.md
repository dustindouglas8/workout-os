# Program Config

## Purpose

This file defines the user-specific values that drive program generation. In the final system, each user should have one config. Dustin's config is the reference implementation, not the universal template.

## Config Shape

```yaml
user:
  name:
  age:
  sex:
  bodyweight_lbs:
  training_age:
  primary_goal:
  secondary_goals: []

timeline:
  annual_start_date:
  current_block:
  current_phase:
  roadmap:
    - block:
      goal:
      duration_weeks:
      detail_level:

schedule:
  training_days_per_week:
  split_architecture:
  available_days: []
  week_start_day:
  session_time_cap_minutes:
  training_time_of_day:
  travel_frequency:

recovery:
  bias:
  sleep_home_average:
  sleep_travel_average:
  rhr_baseline:
  hrv_available:
  stress_level:
  readiness_threshold_overrides:

health:
  current_pain:
    - location:
      score:
      notes:
  injury_history: []
  movement_limitations: []
  medical_flags: []

equipment:
  home: []
  travel: []
  recovery_tools: []
  unavailable: []

nutrition:
  goal:
  fasting_protocol:
  eating_window:
  macro_tracking_level:
  protein_target:
  dietary_constraints: []
  preferred_templates: []
  preworkout_inputs: []

skills:
  preferred_skill_day_options: []

logging:
  daily_log_enabled: true
  weekly_checkin_enabled: true
  photos_enabled:
  waist_measurement_enabled:
```

## Dustin Reference Config

```yaml
user:
  name: Dustin
  age:
  sex: male
  bodyweight_lbs: 225
  training_age:
  primary_goal: recomp
  secondary_goals:
    - strength
    - mobility
    - long-term joint resilience

timeline:
  annual_start_date:
  current_block: 1
  current_phase: 1
  roadmap:
    - block: 1
      goal: recomp + tissue capacity + movement quality
      duration_weeks: 12
      detail_level: full
    - block: 2
      goal: strength or specialization, finalized after Block 1 tests
      duration_weeks: 12
      detail_level: draft
    - block: 3
      goal: hypertrophy, performance, endurance, or skill emphasis
      duration_weeks: 12
      detail_level: directional
    - block: 4
      goal: consolidation, specialization, or repeat cycle
      duration_weeks: 12
      detail_level: directional

schedule:
  training_days_per_week: 6
  split_architecture: Lower First
  available_days:
    - Sunday
    - Monday
    - Tuesday
    - Wednesday
    - Thursday
    - Friday
    - Saturday
  week_start_day: Sunday
  session_time_cap_minutes: 60
  training_time_of_day: early morning
  travel_frequency: variable

recovery:
  bias: recovery-biased
  sleep_home_average: 7-8 hours
  sleep_travel_average: about 1 hour less than home
  rhr_baseline:
  hrv_available:
  stress_level:
  readiness_threshold_overrides:

health:
  current_pain: []
  injury_history:
    - shoulders / rotator cuff emphasis
    - lower back / hip flexor emphasis
    - knees / ankles emphasis
  movement_limitations: []
  medical_flags: []

equipment:
  home:
    - mounted pull-up bar
    - gymnastic rings
    - resistance bands
    - adjustable weight vest
    - sliders
    - kettlebells
    - dumbbells
    - jump rope
    - yoga mat
    - stability ball
    - pneumatic compression sleeves
  travel:
    - resistance bands
    - hotel gym dumbbells/cables when available
    - bodyweight fallback
  recovery_tools:
    - pneumatic compression sleeves
  unavailable: []

nutrition:
  goal: recomp
  fasting_protocol: 16:8
  eating_window: 8am-2pm
  macro_tracking_level: moderate
  protein_target: high-protein anchor
  dietary_constraints: []
  preferred_templates:
    - recovery shake
    - egg and oat bowl
    - lentil and fish bowl
    - casein or Greek yogurt closing meal
  preworkout_inputs:
    - matcha
    - EAAs
    - creatine
    - electrolytes

skills:
  preferred_skill_day_options:
    - boxing
    - animal flow
    - Tai Chi
    - salsa

logging:
  daily_log_enabled: true
  weekly_checkin_enabled: true
  photos_enabled: optional
  waist_measurement_enabled: optional
```

## Config Rules

- User-specific values should live here, not inside invariant docs.
- Missing values should be explicit blanks, not silently assumed.
- If a generator must choose a default, it should record that default in the output.
- Dustin-specific nutrition, equipment, and recovery assumptions should not become universal behavior.

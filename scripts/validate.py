#!/usr/bin/env python3
"""
Workout OS — Validate Script
Checks the template for common programming errors before build.

Usage:
    python3 scripts/validate.py           # check template
    python3 scripts/validate.py --dist    # check dist/index.html instead

Exit codes:
    0 — passed (warnings allowed)
    1 — one or more ERRORs found
"""

import re
import sys
import json
from pathlib import Path

ROOT      = Path(__file__).parent.parent
TMPL      = ROOT / "src" / "app" / "template.html"
DIST      = ROOT / "docs" / "index.html"
EXERCISES = ROOT / "src" / "data" / "exercises.json"

ERRORS   = []
WARNINGS = []

def err(msg):  ERRORS.append(f"  ERROR   {msg}")
def warn(msg): WARNINGS.append(f"  WARN    {msg}")
def ok(msg):   print(f"  ok      {msg}")


# ── Parsers ────────────────────────────────────────────────────────────────────

def load_exercises() -> list[dict]:
    """Load the exercise library from its JSON source of truth."""
    if not EXERCISES.exists():
        err(f"Exercise data not found: {EXERCISES}")
        return []
    return json.loads(EXERCISES.read_text(encoding="utf-8"))


def extract_session_exercise_names(html: str) -> list[str]:
    """
    Pull exercise names referenced inside session spec objects.
    Looks for: n:'ExerciseName' inside the SESSIONS/SESSION_SPECS block.
    This is a heuristic — catches most inline session references.
    """
    # Find the session specs block (between SESSION_SPECS and the closing };)
    match = re.search(r"(SESSION_SPECS|SESSIONS)\s*=\s*\{(.+?)^\};",
                      html, re.DOTALL | re.MULTILINE)
    if not match:
        return []
    block = match.group(2)
    return re.findall(r"n:'([^']+)'", block)


def extract_warmup_names(html: str) -> list[str]:
    """Pull exercise names from warm-up blocks."""
    matches = re.findall(r"warmup[^{]*\{[^}]*n:'([^']+)'", html)
    return matches


# ── Checks ─────────────────────────────────────────────────────────────────────

def check_exlib_duplicates(names: list[str]):
    seen = {}
    for n in names:
        seen[n] = seen.get(n, 0) + 1
    dupes = [n for n, c in seen.items() if c > 1]
    if dupes:
        for d in dupes:
            err(f"Duplicate EX_LIB entry: '{d}'")
    else:
        ok(f"EX_LIB: no duplicates ({len(names)} entries)")


def check_session_exercises_have_lib_entries(session_names: list[str], lib_names: list[str]):
    lib_set = set(lib_names)
    missing = [n for n in session_names if n not in lib_set]
    if missing:
        for m in missing:
            warn(f"Session exercise has no EX_LIB entry: '{m}'  → cue drawer will show warning")
    else:
        ok(f"Session exercises: all {len(session_names)} have EX_LIB entries")


def check_warmup_exercises_have_lib_entries(warmup_names: list[str], lib_names: list[str]):
    lib_set = set(lib_names)
    missing = [n for n in warmup_names if n not in lib_set]
    if missing:
        for m in set(missing):
            warn(f"Warm-up exercise has no EX_LIB entry: '{m}'")
    elif warmup_names:
        ok(f"Warm-up exercises: all {len(warmup_names)} have EX_LIB entries")


def check_safety_sensitive(exercises: list[dict]):
    """Safety-sensitive exercises must have contraindication or caution copy."""
    sensitive = ["Jefferson Curl", "Nordic Hamstring Eccentric", "Skin the Cat",
                 "Nordic Hamstring Curl"]
    by_name = {e["n"]: e for e in exercises}
    for ex in sensitive:
        entry = by_name.get(ex)
        if entry is not None:
            if entry.get("mistakes"):
                ok(f"Safety: '{ex}' has mistake cues")
            else:
                warn(f"Safety: '{ex}' is in EX_LIB but has no mistake cues")


def check_timed_exercises_have_duration(html: str):
    """Exercises with 'hold' or 'min' prescriptions should have a duration."""
    # Look for rx fields with hold/min but no number
    pattern = r"rx:'([^']*(?:hold|min)[^']*)'"
    matches = re.findall(pattern, html, re.IGNORECASE)
    missing_duration = [m for m in matches if not re.search(r'\d', m)]
    if missing_duration:
        for m in missing_duration:
            warn(f"Timed prescription has no duration: '{m}'")
    else:
        ok(f"Timed prescriptions: all contain numeric duration")


def check_pwa_hooks(html: str):
    checks = {
        'manifest link':         'rel="manifest"',
        'service worker reg':    'serviceWorker.register',
        'apple-mobile-web-app':  'apple-mobile-web-app-capable',
        'theme-color meta':      'theme-color',
    }
    for label, marker in checks.items():
        if marker in html:
            ok(f"PWA: {label} present")
        else:
            warn(f"PWA: {label} missing — run build.py to inject")


def check_exlib_cue_completeness(exercises: list[dict]):
    """Every EX_LIB entry should have setup, exec, and breath fields."""
    incomplete = []
    for entry in exercises:
        missing_fields = [f for f in ('setup', 'exec', 'breath') if not entry.get(f)]
        if missing_fields:
            incomplete.append(f"'{entry.get('n')}' missing: {', '.join(missing_fields)}")
    if incomplete:
        for i in incomplete:
            warn(f"EX_LIB incomplete entry: {i}")
    else:
        ok(f"EX_LIB entries: all have setup/exec/breath fields")


# ── Main ───────────────────────────────────────────────────────────────────────

def validate(path: Path):
    print(f"── Workout OS Validate ───────────────────────────────")
    print(f"   File: {path}")

    if not path.exists():
        err(f"File not found: {path}")
        print("\n".join(ERRORS))
        return False

    html = path.read_text(encoding="utf-8")
    lines = html.count("\n") + 1
    print(f"   Size: {len(html):,} chars, {lines} lines\n")

    exercises     = load_exercises()
    lib_names     = [e["n"] for e in exercises]
    session_names = extract_session_exercise_names(html)
    warmup_names  = extract_warmup_names(html)

    check_exlib_duplicates(lib_names)
    check_session_exercises_have_lib_entries(session_names, lib_names)
    check_warmup_exercises_have_lib_entries(warmup_names, lib_names)
    check_exlib_cue_completeness(exercises)
    check_safety_sensitive(exercises)
    check_timed_exercises_have_duration(html)
    check_pwa_hooks(html)

    print()
    if WARNINGS:
        print("\n".join(WARNINGS))
    if ERRORS:
        print()
        print("\n".join(ERRORS))
        print(f"\n── {len(ERRORS)} error(s), {len(WARNINGS)} warning(s) — BUILD BLOCKED ──")
        return False

    if WARNINGS:
        print(f"\n── 0 errors, {len(WARNINGS)} warning(s) — build allowed ──")
    else:
        print(f"\n── All checks passed ─────────────────────────────────")
    return True


if __name__ == "__main__":
    use_dist = "--dist" in sys.argv
    target = DIST if use_dist else TMPL
    ok_result = validate(target)
    raise SystemExit(0 if ok_result else 1)

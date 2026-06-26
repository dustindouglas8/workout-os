#!/usr/bin/env python3
"""
Workout OS — Build Script
Reads src/app/template.html, adds PWA files, writes dist/

Usage:
    python3 scripts/build.py

Output:
    dist/index.html     — app ready to open or deploy
    dist/manifest.json  — PWA installability
    dist/sw.js          — offline cache (service worker)
    dist/icons/         — app icons (if present in src/icons/)
"""

import os
import json
import shutil
import hashlib
from datetime import datetime, timezone
from pathlib import Path

ROOT   = Path(__file__).parent.parent
SRC    = ROOT / "src"
DIST   = ROOT / "docs"
TMPL   = SRC / "app" / "template.html"
EXERCISES = SRC / "data" / "exercises.json"

# ── Manifest ──────────────────────────────────────────────────────────────────

MANIFEST = {
    "name": "Training OS",
    "short_name": "Training OS",
    "description": "Personal workout tracker — recomposition program",
    "start_url": "./",
    "scope": "./",
    "display": "standalone",
    "orientation": "portrait",
    "background_color": "#0e0e0f",
    "theme_color": "#0e0e0f",
    "icons": [
        {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}
    ]
}

# ── Service Worker ─────────────────────────────────────────────────────────────

SW_TEMPLATE = """\
// Training OS — Service Worker
// Cache version bumps on every build to force refresh after deploy
const CACHE = 'training-os-{version}';
const ASSETS = [
  './',
  './index.html',
  './manifest.json'
];

self.addEventListener('install', e => {{
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(ASSETS))
  );
  self.skipWaiting();
}});

self.addEventListener('activate', e => {{
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
}});

self.addEventListener('fetch', e => {{
  // Network-first for navigation; cache-first for assets
  if (e.request.mode === 'navigate') {{
    e.respondWith(
      fetch(e.request).catch(() => caches.match('./index.html'))
    );
  }} else {{
    e.respondWith(
      caches.match(e.request).then(r => r || fetch(e.request))
    );
  }}
}});
"""

# ── PWA injection ──────────────────────────────────────────────────────────────

PWA_HEAD = """\
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0e0e0f">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Training OS">
  <link rel="apple-touch-icon" href="icons/icon-192.png">"""

SW_REGISTRATION = """\
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('sw.js').catch(() => {});
      });
    }
  </script>"""

BUILD_COMMENT = f"  <!-- Built: {{ts}} -->"

# ── Helpers ────────────────────────────────────────────────────────────────────

def inject_html(html: str, version: str) -> str:
    """Inject PWA manifest link and SW registration into the template."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Inject before </head>
    if "</head>" in html:
        html = html.replace(
            "</head>",
            PWA_HEAD + "\n" + BUILD_COMMENT.format(ts=ts) + "\n</head>",
            1
        )

    # Inject before </body>
    if "</body>" in html:
        html = html.replace("</body>", SW_REGISTRATION + "\n</body>", 1)

    return html


def content_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()[:8]


def inject_exercises(html: str) -> str:
    """Replace the EX_LIB placeholder with exercises.json data."""
    if not EXERCISES.exists():
        print(f"  ERROR: exercise data not found at {EXERCISES}")
        raise SystemExit(1)
    exercises = json.loads(EXERCISES.read_text(encoding="utf-8"))
    placeholder = "const EX_LIB = /*__EXERCISES_JSON__*/;"
    if placeholder not in html:
        print(f"  ERROR: EX_LIB placeholder not found in template")
        raise SystemExit(1)
    replacement = "const EX_LIB = " + json.dumps(exercises, ensure_ascii=False) + ";"
    print(f"  Exercises: {len(exercises)} entries from {EXERCISES.relative_to(ROOT)}")
    return html.replace(placeholder, replacement, 1)


# ── Build ──────────────────────────────────────────────────────────────────────

def build():
    print("── Workout OS Build ──────────────────────────────────")

    # 1. Check template exists
    if not TMPL.exists():
        print(f"  ERROR: template not found at {TMPL}")
        print("  Run:  cp ~/Downloads/dustin_training_os_v10.html src/app/template.html")
        return False

    # 2. Read template
    html = TMPL.read_text(encoding="utf-8")
    print(f"  Template:  {TMPL.name}  ({len(html):,} chars, {html.count(chr(10))+1} lines)")

    # 3. Inject exercise data
    html = inject_exercises(html)

    # 4. Generate version hash from content
    version = content_hash(html)
    print(f"  Version:   {version}")

    # 5. Inject PWA hooks
    html = inject_html(html, version)

    # 6. Create dist/
    DIST.mkdir(exist_ok=True)

    # 7. Write index.html
    out = DIST / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"  Output:    docs/index.html  ({len(html):,} chars)")

    # 8. Write manifest.json
    manifest_path = DIST / "manifest.json"
    manifest_path.write_text(json.dumps(MANIFEST, indent=2), encoding="utf-8")
    print(f"  Manifest:  docs/manifest.json")

    # 9. Write sw.js
    sw_path = DIST / "sw.js"
    sw_path.write_text(SW_TEMPLATE.format(version=version), encoding="utf-8")
    print(f"  SW:        docs/sw.js  (cache={version})")

    # 10. Copy icons if they exist
    icons_src = SRC / "icons"
    if icons_src.exists():
        icons_dst = DIST / "icons"
        if icons_dst.exists():
            shutil.rmtree(icons_dst)
        shutil.copytree(icons_src, icons_dst)
        count = len(list(icons_dst.iterdir()))
        print(f"  Icons:     docs/icons/  ({count} files)")
    else:
        print(f"  Icons:     none (add PNG icons to src/icons/ for full PWA install)")

    print(f"── Build complete ────────────────────────────────────")
    print(f"   Open:    open docs/index.html")
    print(f"   Deploy:  push docs/ to GitHub Pages")
    return True


if __name__ == "__main__":
    ok = build()
    raise SystemExit(0 if ok else 1)

#!/usr/bin/env python3
"""
Workout OS — Icon Generator
Writes src/icons/icon-192.png and icon-512.png as plain PNGs
(dumbbell glyph on dark background) using only zlib/struct — no
image library dependency.

Usage:
    python3 scripts/make_icons.py
"""

import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).parent.parent
ICONS = ROOT / "src" / "icons"

BG     = (14, 14, 15)      # #0e0e0f
ACCENT = (62, 207, 142)    # #3ecf8e


def make_png(size: int) -> bytes:
    # Dumbbell glyph proportions, scaled to `size`
    cx = cy = size / 2
    bar_w, bar_h = size * 0.50, size * 0.055
    plate_w, plate_h = size * 0.12, size * 0.35
    gap = bar_w / 2
    plate_radius = size * 0.03

    def in_rounded_rect(x, y, x0, y0, x1, y1, r):
        if x0 <= x <= x1 and y0 <= y <= y1:
            # corner check
            cxs = [ (x0+r, y0+r), (x1-r, y0+r), (x0+r, y1-r), (x1-r, y1-r) ]
            for ccx, ccy in cxs:
                if (x < x0+r or x > x1-r) and (y < y0+r or y > y1-r):
                    if (x-ccx)**2 + (y-ccy)**2 > r*r:
                        return False
            return True
        return False

    bar_box = (cx - bar_w/2, cy - bar_h/2, cx + bar_w/2, cy + bar_h/2)
    plate_boxes = [
        (cx - gap - plate_w/2, cy - plate_h/2, cx - gap + plate_w/2, cy + plate_h/2),
        (cx + gap - plate_w/2, cy - plate_h/2, cx + gap + plate_w/2, cy + plate_h/2),
    ]

    rows = []
    for y in range(size):
        row = bytearray()
        for x in range(size):
            px, py = x + 0.5, y + 0.5
            pixel = BG
            if in_rounded_rect(px, py, *bar_box, bar_h/2):
                pixel = ACCENT
            else:
                for box in plate_boxes:
                    if in_rounded_rect(px, py, *box, plate_radius):
                        pixel = ACCENT
                        break
            row += bytes(pixel)
        rows.append(bytes([0]) + bytes(row))  # filter type 0 per scanline

    raw = b"".join(rows)
    compressed = zlib.compress(raw, 9)

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (struct.pack(">I", len(data)) + tag + data +
                struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)  # 8-bit RGB
    return sig + chunk(b"IHDR", ihdr) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")


def main():
    ICONS.mkdir(parents=True, exist_ok=True)
    for size in (192, 512):
        out = ICONS / f"icon-{size}.png"
        out.write_bytes(make_png(size))
        print(f"  wrote {out.relative_to(ROOT)} ({out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate the checked-in JAMESOS source preset bank without altering firmware."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "JAMESOS-SOURCE-BANK.md"
EXPECTED = {"SYNTHWAVE": 17, "VAPORWAVE": 17, "IDM & BRAINDANCE": 16}
ROW = re.compile(
    r"^\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
    r"\s*(\d{1,3})\s*/\s*(\d{1,3})\s*/\s*(\d{1,3})\s*\|\s*([^|]+?)\s*\|$"
)

def main() -> int:
    text = SOURCE.read_text(encoding="utf-8")
    section = None
    counts = {name: 0 for name in EXPECTED}
    entries = []
    for line in text.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            section = heading.split(" (")[0]
            if section not in EXPECTED:
                section = None
            continue
        match = ROW.match(line)
        if not match:
            continue
        if section is None:
            raise SystemExit(f"Preset row outside a known category: {line}")
        number, name, engine, h, t, m, notes = match.groups()
        values = [int(h), int(t), int(m)]
        if any(value > 100 for value in values):
            raise SystemExit(f"Macro percentage out of range in preset {number}")
        entries.append((int(number), name, engine, values, notes, section))
        counts[section] += 1

    ids = [entry[0] for entry in entries]
    if len(entries) != 50:
        raise SystemExit(f"Expected 50 presets, found {len(entries)}")
    if sorted(ids) != list(range(1, 51)) or len(set(ids)) != 50:
        raise SystemExit("Preset IDs must be unique and cover 01..50")
    if counts != EXPECTED:
        raise SystemExit(f"Category counts differ: {counts!r}")
    if any(not e[1].strip() or not e[2].strip() or not e[4].strip() for e in entries):
        raise SystemExit("Every preset needs a name, source engine and design notes")
    print("JAMESOS bank valid: 50 unique presets (17 Synthwave / 17 Vaporwave / 16 IDM & Braindance)")
    return 0

if __name__ == "__main__":
    sys.exit(main())

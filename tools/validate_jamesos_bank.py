#!/usr/bin/env python3
"""Validate the HORATIO-1 source bank and its 50 compiled factory preset labels."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "HORATIO-1-SOURCE-BANK.md"
EXPECTED = {"SYNTHWAVE": 17, "VAPORWAVE": 17, "IDM & BRAINDANCE": 16}
ROW = re.compile(
    r"^\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
    r"\s*(\d{1,3})\s*/\s*(\d{1,3})\s*/\s*(\d{1,3})\s*\|\s*([^|]+?)\s*\|$"
)

# ID: (firmware source file, compiled factory preset label).
IMPLEMENTED = {
    1: ("eng_analog.c", "OUTRUN SUB"),
    2: ("eng_analog.c", "NIGHTCALL PWM"),
    3: ("eng_macro.c", "JUNO BRASS 84"),
    4: ("eng_vps.c", "MIAMI HORIZON"),
    5: ("eng_analog.c", "TURBO ARP"),
    6: ("eng_digital.c", "LASER HARP"),
    7: ("eng_analog.c", "CHROME LEAD"),
    8: ("eng_macro.c", "NEON POLY"),
    9: ("eng_vps.c", "KAVINSKY GRWL"),
    10: ("eng_macro.c", "SUNSET STRINGS"),
    11: ("eng_digital.c", "RETRO BELL"),
    12: ("eng_analog.c", "ARCADE OCT"),
    13: ("eng_digital.c", "TOM FM BASS"),
    14: ("eng_macro.c", "VANGELIS SWELL"),
    15: ("eng_phase.c", "GRID RUNNER"),
    16: ("eng_analog.c", "TAPE DETUNE"),
    17: ("eng_phys.c", "MIDNIGHT SKY"),
    18: ("eng_digital.c", "MALLSOFT EP"),
    19: ("eng_macro.c", "VHS CHOIR"),
    20: ("eng_macro.c", "MACINTOSH PAD"),
    21: ("eng_phys.c", "SEAPUNK PLUCK"),
    22: ("eng_vps.c", "MUZAK SLAP"),
    23: ("eng_formant.c", "LOBBY SAX"),
    24: ("eng_macro.c", "ECCOJAM LOOP"),
    25: ("eng_phys.c", "CRYSTAL FNT"),
    26: ("eng_analog.c", "FADED CASSETTE"),
    27: ("eng_drawbar.c", "PLAZA ORGAN"),
    28: ("eng_digital.c", "DREAMCAST"),
    29: ("eng_macro.c", "LATE NIGHT WX"),
    30: ("eng_phys.c", "POOL MARIMBA"),
    31: ("eng_grain.c", "HYPNAGOGIC"),
    32: ("eng_digital.c", "SEGA SUNSET"),
    33: ("eng_macro.c", "ELEVATOR CHIME"),
    34: ("eng_noise.c", "SLOWED FLUTE"),
    35: ("eng_phys.c", "CLOCK MODAL"),
    36: ("eng_grain.c", "AUTECHRE GRAIN"),
    37: ("eng_vps.c", "APHEX RUBBER"),
    38: ("eng_phys.c", "GLASS WIRE"),
    39: ("eng_noise.c", "MICRO GLITCH"),
    40: ("eng_analog.c", "BOC WARP TAPE"),
    41: ("eng_digital.c", "FM METAL PING"),
    42: ("eng_macro.c", "LIQUID FORMANT"),
    43: ("eng_vps.c", "SQUAREPUSHER"),
    44: ("eng_macro.c", "INHARM BELL"),
    45: ("eng_grain.c", "DATA STREAM"),
    46: ("eng_phys.c", "RESON PIPE"),
    47: ("eng_digital.c", "ACID 303 FM"),
    48: ("eng_macro.c", "FRACTURED CHRD"),
    49: ("eng_noise.c", "STATIC GEIGER"),
    50: ("eng_macro.c", "SUBHARM PULSE"),
}


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
    if set(IMPLEMENTED) != set(range(1, 51)):
        raise SystemExit("Firmware mapping must cover IDs 01..50 exactly once")

    firmware = ROOT / "firmware" / "src"
    for preset_id, (filename, label) in IMPLEMENTED.items():
        source = (firmware / filename).read_text(encoding="utf-8")
        pattern = re.compile(r'\{\s*"' + re.escape(label) + r'"\s*,')
        if not pattern.search(source):
            raise SystemExit(f"Preset {preset_id:02d}: {label!r} missing from {filename}")

    ui = (firmware / "ui.c").read_text(encoding="utf-8")
    for preset_id, (_, label) in IMPLEMENTED.items():
        pattern = re.compile(r'\{\s*BK_HORATIO-1\s*,\s*[^,]+,\s*"' + re.escape(label) + r'"\s*\}')
        if not pattern.search(ui):
            raise SystemExit(f"Preset {preset_id:02d}: {label!r} missing from the unified HORATIO-1 browser list")

    print("HORATIO-1 bank valid: 50 source presets, 50 compiled factory presets and 50 unified browser entries")
    print("Categories: 17 Synthwave / 17 Vaporwave / 16 IDM & Braindance")
    return 0


if __name__ == "__main__":
    sys.exit(main())

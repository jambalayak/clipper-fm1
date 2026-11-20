# JAMESOS 50-sound bank implementation plan

## Source bank

The user supplied 50 sounds on 2026-11-20:
- 01–17: SYNTHWAVE
- 18–34: VAPORWAVE
- 35–50: IDM & BRAINDANCE

Every source entry has a name, a Plaits engine/model label, H/T/M percentages, and filter/envelope/LFO design notes. Preserve those source values verbatim in a manifest before translating them.

## Storage decision

- The FM-1 user-preset store is 32 slots (two 16-record banks). It is not large enough for the 50 factory sounds and must remain available for user saves.
- Factory sounds are compiled into engine-specific preset tables. JAMESOS should curate/replace factory entries across suitable engines or add a dedicated factory-bank presentation layer without changing the user-preset record format.
- Keep user-created presets intact; the user has approved deleting legacy factory presets if required.

## Translation rules

- MACRO is Plaits-inspired, not a complete Plaits port. Its models are CHORD, SWARM, ADDTV and SPEECH.
- For MACRO entries, H/T/M map to HARM/TIMB/MORPH (0–127 scale from percentage).
- For all other destination engines, map the three macro values to the closest meaningful native controls; do not apply a blind one-to-one mapping.
- Record both source and destination values, and mark approximation when a source Plaits model has no close Clipper equivalent.
- HYBRID is a separate 3-oscillator / 2-filter voice with two envelopes, two LFOs and a modulation matrix; it is a good fallback for complex or non-Plaits-like source designs.

## Trio combinations

The 12 user-supplied three-track combinations should be retained as reference performance concepts in the source manifest. Clipper synth mode is a single instrument (with an optional second layer), not a three-independent-synth-track groovebox. Do not represent a trio as a native three-track preset unless it is deliberately redesigned for the Clipper layer architecture. Drum lanes are excluded throughout.

## Implementation sequence

1. [x] Recover and check in the exact 50 source entries and 12 trio templates.
2. [x] Preserve stable IDs, source model labels, H/T/M values and sound-design notes in the source bank.
3. [x] Create a first-pass Clipper engine destination map for all 50 sounds.
4. [ ] Translate each entry into engine-native factory preset records and curate the JAMESOS browse order.
5. [x] Add a validator for 50 unique IDs, category counts 17/17/16, bounded H/T/M values and complete notes; run it in GitHub Actions.
6. [ ] Run the full host test suite and FM-1 target build before publishing an installable firmware package.

## Current status

The complete source bank and trio reference are now committed. The JAMESOS bank validator passed in GitHub Actions. A first-pass engine map is committed, with GRAIN presets explicitly marked as needing user sample sources. The first 10 JAMESOS sounds are now compiled into `MACRO_PRESETS` in `firmware/src/eng_macro.c`. Their H/T/M values map to native HARM/TIMB/MORPH controls; model, envelope, filter and FX values are translated to Clipper's schema. The remaining 40 sounds still need engine-native programming. The latest host-test workflow is running against this change; no FM-1 target build or `.fwsc` package has been verified.
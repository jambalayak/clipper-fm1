# JAMESOS porting notes

This branch is the working branch for the JAMESOS FM-1 firmware adaptation.
The upstream `main` branch is kept unchanged.

## Product direction

- Name the finished firmware JAMESOS.
- Keep the Clipper synthesizer as the technical base.
- No drum machine, drum tracks, drum lanes, or drum presets in the finished instrument.
- Build a 50-sound bank: SYNTHWAVE 01–17, VAPORWAVE 18–34, IDM & BRAINDANCE 35–50.
- Keep the MicroFreak-inspired control layout and the established vaporwave visual direction.
- Preserve existing user data wherever practical; factory sounds may be replaced.

## What Clipper already provides

Clipper is already a synth rather than a groovebox: its README describes 23 synthesis engines and 407 factory sounds, with no drum machine, song mode, or built-in samples. It includes a Plaits-inspired MACRO engine with four models:

| Clipper MACRO model | Sound-design role |
| --- | --- |
| CHORD | Four-oscillator chord voice |
| SWARM | Eight drifting oscillators |
| ADDTV | Additive harmonics |
| SPEECH | Formant / vocal synthesis |

This is not the complete Mutable Instruments Plaits engine set. Preset labels that name other Plaits models must be translated to the closest Clipper engine or implemented as a new model; they must not be silently mislabeled as Plaits.

## Preset translation

The supplied JAMESOS bank uses H / T / M percentages. For Clipper's MACRO engine, the closest direct mapping is:

- H → HARM
- T → TIMB
- M → MORPH

The mapping is only direct for MACRO sounds. For other Clipper engines, translate the three values to the relevant engine parameters and document the result per preset. Preserve the original source values in the bank data so the port remains auditable.

Clipper's HYBRID engine is a separate, fully editable three-oscillator / two-filter voice with envelopes, LFOs, and a modulation matrix. It is a strong destination for sounds whose Plaits model has no close equivalent.

## Preset-bank architecture

The supplied bank contains 50 sounds (17 SYNTHWAVE, 17 VAPORWAVE, 16 IDM & BRAINDANCE). Do not place these in the 32-slot user-preset store: that store is reserved for the owner's editable sounds and is persistent FM-1 storage.

Clipper's factory presets are compiled into each engine's preset table. The intended implementation is to translate each source entry to a destination Clipper engine and its actual parameter schema, then curate a dedicated JAMESOS factory collection. Keep a machine-readable source manifest with the original Plaits model label, H/T/M percentages, and sound-design notes alongside the translated destination engine/parameters. This makes approximations explicit and allows later refinement without losing the user's original design.

Do not simply copy H/T/M into every engine. MACRO maps H/T/M to HARM/TIMB/MORPH; other engines need a per-engine translation. Engine parameter values, envelopes, FX, and modulation must be set in the engine's native preset structure.

The 12 supplied three-part combinations are performance ideas, not automatically Clipper presets: Clipper synth mode is a single instrument with an optional second layer, not a three-independent-track groovebox. Preserve the trio descriptions as reference material and only adapt them to the instrument's layer/voice architecture where the result is musically faithful. All drum lanes remain excluded.

## Safety and validation rules

1. Make changes on this branch, not `main`.
2. Do not remove or rewrite the upstream source engines merely to simplify preset browsing.
3. Keep the user-preset storage format compatible unless a deliberate versioned migration is implemented.
4. Do not change drum-related compile-time defaults until the build configuration and all drum-only dependencies have been traced.
5. Run the host test suite after firmware or preset-data changes; run the target build before producing an installable `.fwsc`.
6. Do not claim the firmware is install-ready until the target build and package validation pass.

## Current implementation status

- Base: Clipper 1.3.1; working branch: `jamesos-development`; upstream `main` remains untouched.
- `firmware/src/eng_macro.c` now includes 10 JAMESOS MACRO factory presets: JUNO BRASS 84, NEON POLY, SUNSET STRINGS, VHS CHOIR, MACINTOSH PAD, ECCOJAM LOOP, LATE NIGHT WX, ELEVATOR CHIME, LIQUID FORMANT and FRACTURED CHRD.
- These are native Clipper MACRO patches. Their source-bank H/T/M percentages are scaled to HARM/TIMB/MORPH (0–127); the destination model, envelope, filter and FX fields are authored for Clipper. They are not full Mutable Instruments Plaits patches.
- `firmware/src/eng_phys.c` now includes four JAMESOS modal-resonator factory presets: CRYSTAL FNT, POOL MARIMBA, CLOCK MODAL and RESON PIPE. These use the PHYS model's own structure, brightness, damping, strike/bow and excitation parameters.
- `firmware/src/eng_analog.c` now includes eight JAMESOS synthwave/vaporwave virtual-analog presets: OUTRUN SUB, NIGHTCALL PWM, TURBO ARP, CHROME LEAD, ARCADE OCT, TAPE DETUNE, FADED CASSETTE and BOC WARP TAPE. They are guarded by `CLIPPER_SYNTH`, preserving the non-synth preset table.
- The other 28 sounds remain design targets in the source bank and have not yet been added to firmware.
- GitHub Actions is running the host suite for the first preset commit. The `.fwsc` target build/package is still pending.

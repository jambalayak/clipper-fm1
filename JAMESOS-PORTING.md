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

| ClIipper MACRO model | Sound-design role |
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

## Safety and validation rules

1. Make changes on this branch, not `main`.
2. Do not remove or rewrite the upstream source engines merely to simplify preset browsing.
3. Keep the user-preset storage format compatible unless a deliberate versioned migration is implemented.
4. Do not change drum-related compile-time defaults until the build configuration and all drum-only dependencies have been traced.
5. Run the host test suite after firmware or preset-data changes; run the target build before producing an installable `.fwsc`.
6. Do not claim the firmware is install-ready until the target build and package validation pass.

## Current baseline

- Base: Clipper 1.3.1, branch `main` at the time this branch was created.
- Working branch: `jamesos-development`.
- No firmware source files have been changed yet.

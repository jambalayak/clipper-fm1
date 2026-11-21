# HORATIO-1

HORATIO-1 is a drum-free synthesizer firmware project for the M-VAVE FM-1, developed on the `jamesos-development` branch of this repository.

## Product direction

- Four-voice paraphonic synth mode with a shared four-voice budget and shared gate/amplitude envelope.
- MicroFreak-inspired control layout, adapted for the FM-1's small display.
- Vaporwave / retro-futurist visual identity: neon magenta, cyan and violet, gradient surfaces, restrained scanlines, and chrome/glass accents.
- An original audio-reactive home-screen visualizer inspired by the era of 2000s desktop media-player visualizers; do not copy proprietary Microsoft artwork.
- A curated 45-sound factory collection spanning Synthwave, Vaporwave, and IDM / Braindance.
- No drum part, drum sequencer, or legacy drum-system UI in the intended product.

## Current implementation

- The 45 active source-bank sounds are translated into native Clipper engine factory preset records. The engine map documents the actual destination engine and compiled label for each sound.
- The preset bank is exposed as one contiguous category in the factory browser. The compact on-device category label is `HORATIO`; the product name is HORATIO-1.
- The HOME screen now has an original 40-band, audio-reactive visualizer with magenta/cyan/violet bars, a soft mirrored reflection, and restrained scanline detailing. It samples the existing 512-sample scope ring, so it adds no FFT workspace and does no extra work in the audio interrupt.
- Synth mode defaults to four voices. The legacy non-synth/groovebox configuration retains its original eight-voice default.
- The LOFI engine is not compiled into the HORATIO-1 synth build; its historical engine-number slot remains reserved as a harmless compatibility placeholder so later engine IDs do not shift. The original non-synth/groovebox build retains LOFI.
- Preset 38 is now GLASS BELL, a modal-resonator replacement for the low-note tuning-unstable GLASS WIRE string patch; the PHYS engine and its other string models remain available.
- The host validator checks the 45 active source entries, category counts, parameter bounds, native factory preset labels, and browser entries. Five overlapping sounds are retired from the HORATIO category: Retrowave Bell, Vangelis Swell, Late Night Weather, Elevator Chime and Micro-Glitch Dust. Their old engine-table records remain dormant to preserve native engine preset indices.

## Important scope and accuracy notes

- This is currently a Clipper-derived engine adaptation, not a complete Mutable Instruments Plaits port. Several source-model ideas are approximated using the available native engines.
- Mutable Instruments Beads effects have not yet been ported.
- The full vaporwave UI treatment remains planned work. The new HOME visualizer is an initial, lightweight implementation; it is not yet the complete multi-style visualizer or a finished visual redesign.
- The original SLOOP / Clipper lineage and upstream licensing notices remain intact.

## Build and testing

The dedicated GitHub Actions workflows validate the source bank and host tests, and build the FM-1 target package. The installable `.fwsc` output is produced by the target build; always use the latest successful workflow artifact rather than an older build after source changes.

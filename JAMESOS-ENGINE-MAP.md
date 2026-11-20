# JAMESOS source-to-Clipper engine map

This is a first-pass destination map for the 50 original source designs. It is not yet the finished patch bank. The source labels describe the intended Plaits model; the destination column names the actual Clipper engine to program. No destination is being represented as a complete Mutable Instruments Plaits port.

| ID | JAMESOS sound | Source model | Clipper destination | Translation notes |
|---:|---|---|---|---|
| 01 | Outrun Sub | Virtual Analog | ANALOG | Saw/sub voice; low-pass and short filter envelope |
| 02 | Nightcall Pulse | Virtual Analog | ANALOG | Pulse-width modulation and slow LFO |
| 03 | Juno Brass 84 | Chords | MACRO / CHORD | Chord voicing, inversion and warm amplitude envelope |
| 04 | Miami Horizon | Waveshaping | VPS | Bright phase-shaping approximation; add stereo reverb |
| 05 | Turbo Arp | Virtual Analog | ANALOG | Short amp/filter envelope; arp configuration remains common preset data |
| 06 | Laser Harp | Two-Op FM | DIGITAL | Native two-operator FM engine; bright ratio/index |
| 07 | Chrome Lead | Virtual Analog | ANALOG | Detuned saws and pitch vibrato |
| 08 | Neon Poly | Chords | MACRO / CHORD | Major ninth voicing and moderate cutoff |
| 09 | Kavinsky Growl | Wavefolder | WAVE | Use FOLD wavetable as a folded-spectrum approximation; filter resonance |
| 10 | Sunset Strings | Additive | MACRO / ADDTV | Closest additive engine; slow envelope and morph movement |
| 11 | Retrowave Bell | Two-Op FM | DIGITAL | DX-style tine/chime patch |
| 12 | Arcade Octaver | Virtual Analog | ANALOG | Saw/pulse plus octave oscillator or sub |
| 13 | Analog Tom-Bass | Two-Op FM | DIGITAL | Percussive FM patch with falling pitch envelope |
| 14 | Vangelis Swell | Harmonic Osc | MACRO / ADDTV | Additive harmonic pad; long swell and reverb |
| 15 | Grid Runner | Phase Distortion | PHASE | Native phase-distortion engine |
| 16 | Tape Detune Keys | Virtual Analog | ANALOG | Detuned oscillators and triangle pitch LFO |
| 17 | Midnight Skyline | String (Karplus) | PHYS | Physical string model; pluck excitation and stereo delay |
| 18 | Mallsoft DX EP | Two-Op FM | DIGITAL | Soft electric-piano FM; slow pitch modulation |
| 19 | VHS Choir | Formant / Vowel | MACRO / SPEECH | Vowel/formant model; slow attack and morph sweep |
| 20 | Macintosh Pad | Additive | MACRO / ADDTV | Additive partials, dark low-pass and long release |
| 21 | Seapunk Pluck | String (Karplus) | PHYS | Physical string pluck; chorus/reverb send |
| 22 | Muzak Slap Bass | Wavefolder | WAVE | Folded wavetable with short filter decay |
| 23 | Lobby Sax | Formant / Vowel | MACRO / SPEECH | Formant voice with pitch vibrato |
| 24 | Eccojam Loop | Chords | MACRO / CHORD | Minor chord stab and slow pitch drift |
| 25 | Crystal Fountain | Modal Resonator | PHYS | Modal resonator with long decay and delay |
| 26 | Faded Cassette | Virtual Analog | ANALOG | Dark low-pass, unstable pitch LFO |
| 27 | Plaza Organ | Harmonic Osc | WHEEL | Drawbar organ is the closest organ-specific engine |
| 28 | Dreamcast Menu | Two-Op FM | DIGITAL | Glassy FM bell with long amp attack/reverb |
| 29 | Late Night Weather | Chords | MACRO / CHORD | Suspended/jazz chord voicing |
| 30 | Poolside Marimba | Modal Resonator | PHYS | Modal bar/mallet model and short decay |
| 31 | Hypnagogic Drift | Granular Cloud | GRAIN | Requires a user-supplied sample in a Clipper sample slot; no built-in sample is assumed |
| 32 | Sega Sunset | Two-Op FM | DIGITAL | Warm FM brass/pad |
| 33 | Elevator Chime | Additive | MACRO / ADDTV | High partial content, long release |
| 34 | Slowed Flute | Particle Noise | NOISE | Pitched-noise approximation; tune and filter the resonant component |
| 35 | Clockwork Modal | Modal Resonator | PHYS | Modal resonator with fast sample-and-hold modulation |
| 36 | Autechre Grain | Granular Cloud | GRAIN | Requires a user-supplied source sample; fast density/position modulation |
| 37 | Aphex Rubber | Waveshaping | ACID | Acid filter/drive engine is closer to the requested squelchy bass behaviour than a static waveshaper |
| 38 | Glass Wire | String (Karplus) | PHYS | Bright, high-tension physical string |
| 39 | Micro-Glitch Dust | Particle Noise | NOISE | Pitched impulses/noise with very short amp envelope |
| 40 | BoC Warped Tape | Virtual Analog | ANALOG | Detuned saw and slow random/triangle pitch drift |
| 41 | FM Metallic Ping | Two-Op FM | DIGITAL | Inharmonic FM ratios and very short transient |
| 42 | Liquid Formant | Formant / Vowel | MACRO / SPEECH | Fast vowel/formant morph |
| 43 | Squarepusher Sub | Wavefolder | WAVE | Folded-spectrum bass with low-pass and fast envelope |
| 44 | Inharmonic Bell | Additive | MACRO / ADDTV | Inharmonic partial balance; S&H movement approximated with modulation |
| 45 | Data Stream | Granular Cloud | GRAIN | Requires a user-supplied sample; Punch FX stutter is an additional performance effect |
| 46 | Resonant Pipe | Modal Resonator | PHYS | Bowed/modal resonator with slow attack |
| 47 | Acid 303-FM | Two-Op FM | DIGITAL | Feedback FM patch; filter resonance/accents need common engine modulation |
| 48 | Fractured Chord | Chords | MACRO / CHORD | Chord voicing with modulation of harmonic/inversion controls |
| 49 | Static Geiger | Particle Noise | NOISE | Sparse resonant noise impulses; trigger sparsely |
| 50 | Sub-Harmonic Pulse | Harmonic Osc | MACRO / ADDTV | Additive sub-partial approximation with slow timbre movement |

## Important implementation constraints

- MACRO has four models: CHORD, SWARM, ADDTV and SPEECH. It is Plaits-inspired, not the full Plaits engine.
- DIGITAL is Clipper's two-operator FM engine; FM6 and FMX are separate six-operator engines.
- PHYS includes physical string and modal models.
- GRAIN in Clipper synth mode uses user-uploaded sample slots. Presets 31, 36 and 45 cannot sound as designed until a suitable sample source is supplied or a sample-free redesign is approved.
- H/T/M percentages map directly to MACRO HARM/TIMB/MORPH only. Other engines need engine-specific parameter translation.
- The current preset browser is organized by engine. This mapping therefore creates a set of related sounds spread across engine pages, not yet a single 50-entry JAMESOS bank screen.
- The 12 three-track combinations remain performance reference material: Clipper synth mode is one instrument with an optional layer, not a three-independent-track groovebox.
- Drum systems remain out of scope. Do not re-enable drum lanes or add drum presets.

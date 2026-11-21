# HORATIO-1 source preset bank (verbatim design specification)

Instrument: M-VAVE FM-1
Genres: SYNTHWAVE, VAPORWAVE, IDM & BRAINDANCE
Drums: none

Each entry preserves the requested source Plaits label, H/T/M percentages and sound-design notes. These are design targets, not claims that Clipper already implements every named Plaits model.

## SYNTHWAVE (01–17; five retired IDs retained as gaps)

| # | Name | Plaits Engine | H / T / M (%) | Filter, Env & LFO Notes |
|---:|---|---|---:|---|
| 01 | Outrun Sub | Virtual Analog | 35 / 60 / 20 | LP 30%, Res 25%; snappy filter decay (25%) for driving 8th-note bass |
| 02 | Nightcall Pulse | Virtual Analog | 20 / 45 / 80 | Narrow PWM square; LFO 1 (Sine, slow) to Timbre for chorus width |
| 03 | Juno Brass 84 | Chords | 40 / 55 / 45 | Minor 7th voicing; slow Amp Attack (25%), LFO 1 subtle pitch drift |
| 04 | Miami Horizon | Waveshaping | 50 / 65 / 40 | Rich saw-fold; long release (55%) + stereo reverb send |
| 05 | Turbo Arp | Virtual Analog | 30 / 70 / 35 | Short Amp & Filter Decay (18%), zero sustain; crisp arpeggiator pluck |
| 06 | Laser Harp | Two-Op FM | 65 / 75 / 30 | Sync-like bright harmonic bite; medium delay send |
| 07 | Chrome Lead | Virtual Analog | 50 / 80 / 25 | Detuned dual-saw; LFO 1 (5 Hz Sine) to Pitch for solo vibrato |
| 08 | Neon Poly | Chords | 60 / 40 / 50 | Major 9th chord; medium filter cutoff (45%) with warm envelope |
| 09 | Kavinsky Growl | Wavefolder | 25 / 75 / 60 | Aggressive folded bass; LP cutoff 35% with high env depth |
| 10 | Sunset Strings | Additive | 45 / 50 / 65 | Slow attack (45%), long release (65%); LFO 2 slow sweep on Morph |
| 12 | Arcade Octaver | Virtual Analog | 50 / 50 / 10 | Locked 1-octave spread; punchy envelope for bass/lead doubling |
| 13 | Analog Tom-Bass | Two-Op FM | 40 / 60 / 20 | Pitch envelope drop on attack; hybrid percussive synth bass |
| 15 | Grid Runner | Phase Distortion | 35 / 65 / 50 | Resonant digital saw; tight 16th-note decay |
| 16 | Tape Detune Keys | Virtual Analog | 42 / 38 / 30 | LP 40%; LFO 1 triangle gently detuning pitch |
| 17 | Midnight Skyline | String (Karplus) | 50 / 60 / 75 | Bright plucked synth-guitar; stereo delay |

## VAPORWAVE (18–34; five retired IDs retained as gaps)

| # | Name | Plaits Engine | H / T / M (%) | Filter, Env & LFO Notes |
|---:|---|---|---:|---|
| 18 | Mallsoft DX EP | Two-Op FM | 75 / 35 / 20 | Soft EP tine; slow random/triangle LFO to Pitch for tape warble |
| 19 | VHS Choir | Formant / Vowel | 50 / 40 / 65 | Dark "ooh/aah" formant; slow attack (55%), LFO 2 sweeping Morph |
| 20 | Macintosh Pad | Additive | 45 / 30 / 70 | Filtered, hazy partials; LP cutoff 38%, long release (75%) |
| 21 | Seapunk Pluck | String (Karplus) | 60 / 45 / 55 | Glassy chorus-like pluck; medium decay + lush reverb |
| 22 | Muzak Slap Bass | Wavefolder | 25 / 45 / 35 | Rubbery mid-range 80s fretless tone; snappy filter decay |
| 23 | Lobby Sax | Formant / Vowel | 65 / 50 / 40 | Breathy, lo-fi synth reed; LFO 1 vibrato on Pitch |
| 24 | Eccojam Loop | Chords | 30 / 35 / 60 | Minor chord stab; LP 35%, pitch LFO for slowed-tape sag |
| 25 | Crystal Fountain | Modal Resonator | 55 / 40 / 65 | Shimmering water-drop harmonics; long decay + delay |
| 26 | Faded Cassette | Virtual Analog | 40 / 25 / 50 | Heavily low-passed (28%); irregular LFO pitch flutter |
| 27 | Plaza Organ | Harmonic Osc | 60 / 35 / 45 | Warm drawbar-style organ; zero attack, medium release |
| 28 | Dreamcast Menu | Two-Op FM | 80 / 40 / 25 | Airy glassy bell pad; slow attack (35%), high reverb |
| 30 | Poolside Marimba | Modal Resonator | 35 / 50 / 30 | Warm wooden mallet tone; short decay (28%) |
| 31 | Hypnagogic Drift | Granular Cloud | 45 / 30 / 70 | Soft, smeared harmonic cloud; slow LFO on Harmonics |
| 32 | Sega Sunset | Two-Op FM | 50 / 45 / 35 | Warm 16-bit FM brass/pad hybrid; medium attack |
| 34 | Slowed Flute | Particle Noise | 40 / 35 / 80 | Pitched airy noise resonance; soft attack (30%) |

## IDM & BRAINDANCE (35–50; five retired IDs retained as gaps)

| # | Name | Plaits Engine | H / T / M (%) | Filter, Env & LFO Notes |
|---:|---|---|---:|---|
| 35 | Clockwork Modal | Modal Resonator | 62 / 55 / 40 | Inharmonic metallic pluck; LFO 1 (S&H, 1/16) to Harmonics & Morph |
| 36 | Autechre Grain | Granular Cloud | 70 / 60 / 50 | Scattered micro-grains; LFO 2 (Fast S&H) to Timbre + cond. trigs |
| 37 | Aphex Rubber | Waveshaping | 25 / 70 / 65 | Squelchy acid bass; Res 70%, S&H LFO modulating Filter Cutoff |
| 38 | Glass Bell | Modal Resonator | 75 / 80 / 35 | Bright, inharmonic glass-bell strike; short decay and subtle random timbre movement |
| 40 | BoC Warped Tape | Virtual Analog | 45 / 35 / 55 | Nostalgic detuned saw; LFO 1 slow S&H/Triangle pitch drift |
| 41 | FM Metallic Ping | Two-Op FM | 88 / 70 / 60 | Non-integer FM ratio; razor-sharp transient (Attack 0, Decay 15%) |
| 42 | Liquid Formant | Formant / Vowel | 55 / 75 / 50 | Squelchy vocal-filter sweep; fast LFO 1 modulating Morph |
| 43 | Squarepusher Sub | Wavefolder | 20 / 65 / 80 | Growling folded sub-bass; fast envelope for rapid 16th-note runs |
| 44 | Inharmonic Bell | Additive | 85 / 60 / 40 | Clashing upper partials; LFO 1 (S&H) randomizing partial tilt |
| 45 | Data Stream | Granular Cloud | 90 / 85 / 30 | High-density digital stutter texture; pair with Punch FX stutter |
| 46 | Resonant Pipe | Modal Resonator | 30 / 70 / 85 | Hollow bowed tube; slow attack (35%) + LFO on Harmonics |
| 47 | Acid 303-FM | Two-Op FM | 33 / 75 / 55 | Feedback-driven FM acid; high filter resonance + accented env |
| 48 | Fractured Chord | Chords | 65 / 70 / 40 | LFO 1 (S&H) to Harmonics so every note jumps chord inversions |
| 49 | Static Geiger | Particle Noise | 60 / 40 / 90 | Sparse resonant clicks; trigger sparingly via sequencer probability |
| 50 | Sub-Harmonic Pulse | Harmonic Osc | 15 / 65 / 50 | Deep shifting sub-partials; LFO 2 slowly modulating Timbre |

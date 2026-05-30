# TabForge

**Vocal melody to playable guitar tabs.**

TabForge is a local-first audio/ML and algorithmic music project that converts vocal melodies into playable guitar tabs. The project was inspired by a real problem: many Bollywood songs do not have electric guitar tabs for the vocal melody, even though those melodies are often the parts beginner guitarists want to play.

The first goal is a command-line proof of concept. The long-term goal is to evolve TabForge into a polished tool that can process isolated vocal audio, generate playable tabs, and eventually support web-based tab viewing and editing.

## Current Status

TabForge currently supports:

- converting MIDI pitch sequences into possible guitar positions
- choosing simple lead-style guitar positions
- rendering basic ASCII guitar tabs
- running from the command line
- saving generated tabs to a text file

The current version does **not** process audio yet. Audio transcription will be added later using an audio-to-MIDI/pitch transcription tool.

## Example

Generate a tab from MIDI notes:

```bash
tabforge from-notes 64,66,68,71,73
```

Example output:

```txt
e|-0--2--4--7--9-
B|---------------
G|---------------
D|---------------
A|---------------
E|---------------
```

Save the generated tab:

```bash
tabforge from-notes 64,66,68,71,73 --out data/output/tab.txt
```

Short version:

```bash
tabforge from-notes 64,66,68,71,73 -o data/output/tab.txt
```

## Project Roadmap

### Milestone 0: Local Tab Engine

- [x] Created Python package structure
- [x] Added CLI with Typer
- [x] Added MIDI pitch to guitar position mapping
- [x] Added simple fingering position chooser
- [x] Added ASCII tab rendering
- [x] Added output file support
- [x] Added basic tests

### Milestone 1: Better Fingering Algorithm

- [ ] Consider previous note position when choosing the next position
- [ ] Minimize awkward fret jumps
- [ ] Prefer B and high e strings for lead-style melodies
- [ ] Add beginner-friendly and accuracy-focused modes

### Milestone 2: Audio Transcription

- [ ] Accept isolated vocal MP3/WAV files
- [ ] Use an audio-to-MIDI or pitch transcription model
- [ ] Extract note events from vocals
- [ ] Clean noisy note events
- [ ] Convert cleaned notes into guitar tabs

### Milestone 3: Product Layer

- [ ] Add FastAPI backend
- [ ] Add upload and processing endpoints
- [ ] Store results and metadata
- [ ] Build a web interface for viewing and editing tabs

## Development Setup

This project uses `uv` for dependency management.

Create or sync the environment:

```bash
uv sync
```

Run the CLI:

```bash
uv run tabforge demo
```

Run tests:

```bash
uv run pytest
```

Add a normal dependency:

```bash
uv add package-name
```

Add a development dependency:

```bash
uv add --dev package-name
```

## Project Structure

```txt
tabforge/
├── README.md
├── pyproject.toml
├── uv.lock
├── data/
│   ├── input/
│   └── output/
├── src/
│   └── tabforge/
│       ├── __init__.py
│       ├── cli.py
│       ├── fingering.py
│       ├── guitar.py
│       ├── models.py
│       └── tab_render.py
└── tests/
    └── test_guitar.py
```

## Tech Stack

Current:

- Python
- Typer
- pytest
- uv

Planned:

- Basic Pitch or another audio-to-MIDI/pitch transcription tool
- librosa / numpy for audio and signal processing
- FastAPI for the backend
- PostgreSQL for storing uploads/results
- React or Next.js for the frontend later

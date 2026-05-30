import json
from pathlib import Path

import typer

from tabforge.fingering import choose_positions_for_melody
from tabforge.tab_render import render_ascii_tab


def parse_pitch_list(notes: str) -> list[int]:
    """Parse a comma-separated list of MIDI pitches."""
    pitches = []

    for note in notes.split(","):
        note = note.strip()

        if not note:
            continue

        pitches.append(int(note))
    
    return pitches

app = typer.Typer(help="TabForge: vocal melody to playable guitar tabs.")


@app.callback()
def main() -> None:
    """Tabforge CLI."""


@app.command()
def demo() -> None:
    """Generate a demo ASCII guitar tab from hardcoded MIDI notes."""
    melody = [64, 66, 68, 71, 73]
    positions = choose_positions_for_melody(melody)
    tab = render_ascii_tab(positions)

    typer.echo(tab)


@app.command("from-notes")
def from_notes(
    notes: str,
    out: Path | None = typer.Option(
        None,
        "--out",
        "-o",
        help="Optional path to save the generated tab.",
    ),
    debug_json: Path | None = typer.Option(
        None,
        "--debug-json",
        help="Optional path to save chosen note positions as JSON.",
    ),
) -> None:
    """Generate ASCII guitar tab from comma-separated MIDI pitches."""
    pitches = parse_pitch_list(notes)
    positions = choose_positions_for_melody(pitches)
    tab = render_ascii_tab(positions)

    typer.echo(tab)

    if out is not None:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(tab + "\n")
        typer.echo(f"\nSaved tab to {out}")

    if debug_json is not None:
        debug_json.parent.mkdir(parents=True, exist_ok=True)

        debug_data = [
            {
                "pitch": position.pitch,
                "string": position.string,
                "fret": position.fret,
            }
            for position in positions
        ]

        debug_json.write_text(json.dumps(debug_data, indent=2) + "\n")
        typer.echo(f"Saved debug JSON to {debug_json}")


if __name__ == "__main__":
    app()
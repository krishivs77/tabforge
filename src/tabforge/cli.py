import typer

from tabforge.guitar import get_possible_positions

app = typer.Typer(help="TabForge: vocal melody to playable guitar tabs.")


@app.callback()
def main() -> None:
    """Tabforge CLI."""


@app.command()
def demo() -> None:
    """Generate a demo guitar tab from hardcoded MIDI notes."""
    pitch = 64
    positions = get_possible_positions(pitch)

    typer.echo(f"Possible guitar positions for MIDI pitch {pitch}:")
    for position in positions:
        typer.echo(
            f"string={position.string}, fret={position.fret}, pitch={position.pitch}"
        )


if __name__ == "__main__":
    app()
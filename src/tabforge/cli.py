import typer

from tabforge.fingering import choose_positions_for_melody

app = typer.Typer(help="TabForge: vocal melody to playable guitar tabs.")


@app.callback()
def main() -> None:
    """Tabforge CLI."""


@app.command()
def demo() -> None:
    """Choose demo guitar positions from hardcoded MIDI notes."""
    melody = [64, 66, 68, 71, 73]
    positions = choose_positions_for_melody(melody)

    typer.echo("Chosen guitar positions:")

    for position in positions:
        typer.echo(
            f"pitch={position.pitch}, string={position.string}, fret={position.fret}"
        )


if __name__ == "__main__":
    app()
import typer

from tabforge.fingering import choose_best_position

app = typer.Typer(help="TabForge: vocal melody to playable guitar tabs.")


@app.callback()
def main() -> None:
    """Tabforge CLI."""


@app.command()
def demo() -> None:
    """Choose demo guitar positions from hardcoded MIDI notes."""
    melody = [64, 66, 68, 71, 73]

    typer.echo("Chosen guitar positions:")

    for pitch in melody:
        position = choose_best_position(pitch)
        typer.echo(
            f"pitch={pitch}, string={position.string}, fret={position.fret}"
        )


if __name__ == "__main__":
    app()
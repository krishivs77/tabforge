import typer

app = typer.Typer(help="TabForge: vocal melody to playable guitar tabs.")


@app.callback()
def main() -> None:
    """Tabforge CLI."""


@app.command()
def demo() -> None:
    """Generate a demo guitar tab from hardcoded MIDI notes."""
    typer.echo("TabForge demo is working.")
    typer.echo("Next step: convert hardcoded MIDI notes into ASCII tab.")


if __name__ == "__main__":
    app()
import typer

from tabforge.fingering import choose_positions_for_melody
from tabforge.tab_render import render_ascii_tab

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


if __name__ == "__main__":
    app()
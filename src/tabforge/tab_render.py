from tabforge.models import GuitarPosition

STRING_NAMES = ["e", "B", "G", "D", "A", "E"]


def render_ascii_tab(positions: list[GuitarPosition]) -> str:
    """Render guitar positions as a simple ASCII tab."""
    lines = {string_index: f"{name}|" for string_index, name in enumerate(STRING_NAMES)}

    for position in positions:
        for string_index in range(len(STRING_NAMES)):
            if string_index == position.string:
                lines[string_index] += f"-{position.fret}-"
            else:
                lines[string_index] += "---"
    
    return "\n".join(lines[string_index] for string_index in range(len(STRING_NAMES)))
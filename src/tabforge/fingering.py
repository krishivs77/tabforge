from tabforge.guitar import get_possible_positions
from tabforge.models import GuitarPosition


def choose_best_position(pitch: int) -> GuitarPosition:
    """Choose a reasonable guitar position for a MIDI pitch.
    
    First simple strategy:
    - Prefer the B and high e strings.
    - Avoid lower strings unless needed.
    - Among available options, choose the smallest string index.
    """
    positions = get_possible_positions(pitch)

    if not positions:
        raise ValueError(f"MIDI pitch {pitch} is not playable on guitar.")
    
    return min(positions, key=lambda position: position.string)

def choose_positions_for_melody(pitches: list[int]) -> list[GuitarPosition]:
    """Choose guitar positions for a sequence of MIDI pitches."""
    positions = []

    for pitch in pitches:
        position = choose_best_position(pitch)
        positions.append(position)
    
    return positions
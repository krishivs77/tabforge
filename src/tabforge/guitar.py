from tabforge.models import GuitarPosition

# Internal string order matches ASCII tab order:
# 0 = high E, 1 = B, 2 = G, 3 = D, 4 = A, 5 = low E
STANDARD_TUNING = [64, 59, 55, 50, 45, 40]


def get_possible_positions(pitch: int, max_fret: int = 19) -> list[GuitarPosition]:
    """Return all playable guitar positions for a MIDI pitch."""
    positions = []

    for string_index, open_string_pitch in enumerate(STANDARD_TUNING):
        fret = pitch - open_string_pitch

        if 0 <= fret <= max_fret:
            positions.append(
                GuitarPosition(
                    string=string_index,
                    fret=fret,
                    pitch=pitch
                )
            )
    
    return positions
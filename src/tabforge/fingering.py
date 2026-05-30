from tabforge.guitar import get_possible_positions
from tabforge.models import GuitarPosition


def get_fret_zone(fret: int) -> int:
    """Return a rough hand-position zone for a fret.

    Open strings are treated as their own special zone.
    Frets 1-4 are zone 1, frets 5-8 are zone 2, etc.
    """
    if fret == 0:
        return 0

    return ((fret - 1) // 4) + 1


def score_position(
    candidate: GuitarPosition,
    previous: GuitarPosition | None = None,
) -> float:
    """Score a candidate guitar position.

    Lower scores are better.

    Current priorities:
    - Prefer high e and B strings for lead-style melodies.
    - Avoid large fret jumps.
    - Avoid unnecessary hand-position shifts.
    - Reward useful open strings.
    - Slightly penalize switching strings.
    """
    score = 0.0

    # Prefer higher strings, but not so much that it causes awkward choices.
    score += candidate.string * 0.5

    # Open strings are often easy and natural in melody tabs.
    if candidate.fret == 0:
        score -= 2.0

    if previous is not None:
        fret_distance = abs(candidate.fret - previous.fret)
        string_distance = abs(candidate.string - previous.string)

        score += fret_distance * 0.8
        score += string_distance * 1.0

        previous_zone = get_fret_zone(previous.fret)
        candidate_zone = get_fret_zone(candidate.fret)

        # Penalize shifting the fretting hand to a new position.
        # Open strings are exempt because they do not require a fretting-hand shift.
        if candidate.fret != 0 and previous.fret != 0:
            zone_shift = abs(candidate_zone - previous_zone)
            score += zone_shift * 3.0

    return score


def choose_best_position(
    pitch: int,
    previous: GuitarPosition | None = None,
) -> GuitarPosition:
    """Choose a reasonable guitar position for a MIDI pitch."""
    positions = get_possible_positions(pitch)

    if not positions:
        raise ValueError(f"MIDI pitch {pitch} is not playable on guitar.")

    return min(
        positions,
        key=lambda position: score_position(position, previous),
    )


def choose_positions_for_melody(pitches: list[int]) -> list[GuitarPosition]:
    """Choose guitar positions for a sequence of MIDI pitches."""
    chosen_positions = []
    previous = None

    for pitch in pitches:
        position = choose_best_position(pitch, previous)
        chosen_positions.append(position)
        previous = position

    return chosen_positions
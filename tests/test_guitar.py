from tabforge.guitar import get_possible_positions


def test_get_possible_positions_for_middle_e() -> None:
    positions = get_possible_positions(64)

    string_fret_pairs = [(position.string, position.fret) for position in positions]
    
    assert string_fret_pairs == [
        (0, 0),
        (1, 5),
        (2, 9),
        (3, 14),
        (4, 19),
    ]
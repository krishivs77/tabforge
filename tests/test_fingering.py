from tabforge.fingering import choose_positions_for_melody


def test_choose_positions_prefers_open_b_at_end_of_phrase() -> None:
    positions = choose_positions_for_melody([59, 62, 64, 66, 67, 66, 64, 62, 59])

    string_fret_pairs = [(position.string, position.fret) for position in positions]

    assert string_fret_pairs == [
        (1, 0),
        (1, 3),
        (0, 0),
        (0, 2),
        (0, 3),
        (0, 2),
        (0, 0),
        (1, 3),
        (1, 0)
    ]
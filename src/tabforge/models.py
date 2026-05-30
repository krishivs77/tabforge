from dataclasses import dataclass


@dataclass(frozen=True)
class GuitarPosition:
    string: int
    fret: int
    pitch: int
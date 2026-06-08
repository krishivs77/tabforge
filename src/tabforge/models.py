from dataclasses import dataclass


@dataclass(frozen=True)
class NoteEvent:
    pitch: int
    start: float
    end: float
    confidence: float = 1.0


@dataclass(frozen=True)
class GuitarPosition:
    string: int
    fret: int
    pitch: int
from dataclasses import dataclass


@dataclass(slots=True)
class Score:
    """Score for a prompt based on several criteria."""

    clarity: int
    context: int
    constraints: int
    intent: int
    overall: float

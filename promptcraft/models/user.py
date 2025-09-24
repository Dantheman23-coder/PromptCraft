from dataclasses import dataclass


@dataclass(slots=True)
class User:
    """User metadata."""

    id: str
    name: str

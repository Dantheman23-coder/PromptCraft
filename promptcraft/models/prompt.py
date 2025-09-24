from dataclasses import dataclass


@dataclass(slots=True)
class Prompt:
    """Simple representation of a prompt."""

    text: str

"""Prompt scoring metrics."""

from dataclasses import dataclass


@dataclass
class Score:
    clarity: int
    context: int
    constraints: int
    intent: int

    @property
    def overall(self) -> float:
        return (self.clarity + self.context + self.constraints + self.intent) / 4


def score_prompt(prompt: str) -> Score:
    length = len(prompt)
    clarity = min(100, max(0, 100 - length // 2))
    return Score(clarity, clarity, clarity, clarity)

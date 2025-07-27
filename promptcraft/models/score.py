from pydantic import BaseModel


class Score(BaseModel):
    clarity: int
    context: int
    constraints: int
    intent: int
    overall: float

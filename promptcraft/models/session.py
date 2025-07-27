from pydantic import BaseModel


class Session(BaseModel):
    user_id: str
    prompts: list[str] = []

from dataclasses import dataclass, field


@dataclass(slots=True)
class Session:
    """Record of a prompt crafting session."""

    user_id: str
    prompts: list[str] = field(default_factory=list)

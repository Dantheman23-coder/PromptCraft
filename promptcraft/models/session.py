from __future__ import annotations

try:  # pragma: no cover - prefer Pydantic models when available
    from pydantic import BaseModel, Field
    try:
        from pydantic import ConfigDict
    except ImportError:  # pragma: no cover
        ConfigDict = None  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - fall back to dataclasses
    BaseModel = None  # type: ignore
    ConfigDict = None  # type: ignore
    Field = None  # type: ignore


if BaseModel is None:  # pragma: no cover - executed when Pydantic is unavailable
    from dataclasses import dataclass, field

    @dataclass(slots=True)
    class Session:
        """Record of a prompt crafting session."""

        user_id: str
        prompts: list[str] = field(default_factory=list)
else:

    class Session(BaseModel):
        """Record of a prompt crafting session."""

        user_id: str
        prompts: list[str] = Field(default_factory=list)

        if ConfigDict is not None:
            model_config = ConfigDict(validate_assignment=True)
        else:  # pragma: no cover - Pydantic v1 fallback
            class Config:
                validate_assignment = True

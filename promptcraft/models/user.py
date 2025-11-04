from __future__ import annotations

try:  # pragma: no cover - prefer Pydantic models when available
    from pydantic import BaseModel
    try:
        from pydantic import ConfigDict
    except ImportError:  # pragma: no cover
        ConfigDict = None  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - fall back to dataclasses
    BaseModel = None  # type: ignore
    ConfigDict = None  # type: ignore


if BaseModel is None:  # pragma: no cover - executed when Pydantic is unavailable
    from dataclasses import dataclass

    @dataclass(slots=True)
    class User:
        """User metadata."""

        id: str
        name: str
else:

    class User(BaseModel):
        """User metadata."""

        id: str
        name: str

        if ConfigDict is not None:
            model_config = ConfigDict(frozen=True)
        else:  # pragma: no cover - Pydantic v1 fallback
            class Config:
                allow_mutation = False

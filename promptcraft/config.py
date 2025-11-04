"""Lightweight settings management."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(slots=True)
class Settings:
    """Configuration values sourced from the environment."""

    openai_api_key: str = ""
    openai_base_url: str = ""


def _env(*names: str, default: str = "") -> str:
    """Return the first populated environment variable from ``names``."""

    for name in names:
        value = os.getenv(name)
        if value:
            return value
    return default


def get_settings() -> Settings:
    """Return application settings using environment fallbacks."""

    return Settings(
        openai_api_key=_env("PROMPTCRAFT_OPENAI_API_KEY", "OPENAI_API_KEY"),
        openai_base_url=_env("PROMPTCRAFT_OPENAI_BASE_URL", "OPENAI_BASE_URL"),
    )

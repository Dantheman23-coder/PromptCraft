"""Lightweight settings management."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(slots=True)
class Settings:
    """Configuration values sourced from the environment."""

    openai_api_key: str = ""


def get_settings() -> Settings:
    """Return application settings using environment fallbacks."""

    return Settings(openai_api_key=os.getenv("PROMPTCRAFT_OPENAI_API_KEY", ""))

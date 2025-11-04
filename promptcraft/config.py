"""Lightweight settings management."""

from __future__ import annotations

import os
from dataclasses import dataclass

try:  # pragma: no cover - prefer Pydantic implementation when available
    from pydantic import Field
    try:
        from pydantic_settings import BaseSettings, SettingsConfigDict
    except ImportError:  # pragma: no cover - fallback to Pydantic's BaseSettings
        from pydantic import BaseSettings  # type: ignore

        SettingsConfigDict = None  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - fall back to dataclass implementation
    Field = None  # type: ignore
    BaseSettings = None  # type: ignore
    SettingsConfigDict = None  # type: ignore


if BaseSettings is None:  # pragma: no cover - executed when Pydantic is unavailable
    @dataclass(slots=True)
    class Settings:
        """Configuration values sourced from the environment."""

        openai_api_key: str = ""
        openai_base_url: str = ""
        openai_organization: str = ""


    def _env(*names: str, default: str = "") -> str:
        for name in names:
            value = os.getenv(name)
            if value:
                return value
        return default


    def get_settings() -> Settings:
        """Return application settings using environment fallbacks."""

        return Settings(
            openai_api_key=_env("PROMPTCRAFT_OPENAI_API_KEY", "OPENAI_API_KEY"),
            openai_base_url=_env("PROMPTCRAFT_OPENAI_BASE_URL", "OPENAI_BASE_URL", "OPENAI_API_BASE"),
            openai_organization=_env(
                "PROMPTCRAFT_OPENAI_ORG",
                "PROMPTCRAFT_OPENAI_ORGANIZATION",
                "OPENAI_ORG",
                "OPENAI_ORGANIZATION",
            ),
        )
else:

    class Settings(BaseSettings):
        """Configuration values sourced from the environment."""

        openai_api_key: str = Field(
            default="",
            env=["PROMPTCRAFT_OPENAI_API_KEY", "OPENAI_API_KEY"],
        )
        openai_base_url: str = Field(
            default="",
            env=[
                "PROMPTCRAFT_OPENAI_BASE_URL",
                "OPENAI_BASE_URL",
                "OPENAI_API_BASE",
            ],
        )
        openai_organization: str = Field(
            default="",
            env=[
                "PROMPTCRAFT_OPENAI_ORG",
                "PROMPTCRAFT_OPENAI_ORGANIZATION",
                "OPENAI_ORG",
                "OPENAI_ORGANIZATION",
            ],
        )

        if SettingsConfigDict is not None:
            model_config = SettingsConfigDict(env_prefix="", extra="ignore")
        else:  # pragma: no cover - Pydantic v1 fallback
            class Config:
                env_prefix = ""
                extra = "ignore"


    def get_settings() -> Settings:
        """Return application settings using environment fallbacks."""

        return Settings()


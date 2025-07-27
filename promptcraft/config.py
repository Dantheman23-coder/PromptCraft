try:
    from pydantic_settings import BaseSettings
except ImportError:  # pragma: no cover
    from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str = ""

    class Config:
        env_prefix = "PROMPTCRAFT_"


def get_settings() -> Settings:
    return Settings()

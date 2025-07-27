from __future__ import annotations

import openai
from .cache import get, set
from .config import get_settings
from .logger import logger


class AIClient:
    def __init__(self, model: str = "gpt-4o"):
        self.model = model
        self.settings = get_settings()

    def chat(self, prompt: str) -> str:
        cache_key = f"{self.model}:{prompt}"
        if cached := get(cache_key):
            return cached
        logger.info("Querying OpenAI API")
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        message = response.choices[0].message.content
        set(cache_key, message)
        return message

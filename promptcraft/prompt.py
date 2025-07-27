"""Prompt rewriting functions."""

from .ai_client import AIClient


def rewrite(text: str, model: str = "gpt-4o") -> str:
    """Rewrite free-form thought into a structured prompt."""
    client = AIClient(model)
    return client.chat(
        f"Rewrite the following messy thought into a precise LLM instruction:\n{text}\nConstraints: keep under 80 words, include desired output format."
    )

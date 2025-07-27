from ..prompt import rewrite


def tutorial_mode(text: str) -> str:
    """Guided tutorial rewrite."""
    return rewrite(text)

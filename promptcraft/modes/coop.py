from ..prompt import rewrite


def coop_mode(text: str) -> str:
    """Collaborative rewrite."""
    return rewrite(text)

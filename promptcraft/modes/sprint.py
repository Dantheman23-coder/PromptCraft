from ..prompt import rewrite


def sprint_mode(text: str) -> str:
    """Fast rewrite."""
    return rewrite(text)

import click

from .prompt import rewrite
from .logger import logger


@click.group()
def cli():
    """PromptCraft CLI."""


@cli.command()
@click.argument("input")
@click.option("--model", default="gpt-4o", help="OpenAI model")
def rewrite_cmd(input: str, model: str):
    """Rewrite free-form thought into a structured prompt."""
    result = rewrite(input, model=model)
    click.echo(result)
    logger.info("Prompt rewritten")

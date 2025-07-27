from promptcraft.cli import cli
from click.testing import CliRunner


def test_end_to_end(monkeypatch):
    monkeypatch.setattr("promptcraft.ai_client.AIClient.chat", lambda self, p: "done")
    runner = CliRunner()
    result = runner.invoke(cli, ["rewrite", "example"])
    assert result.exit_code == 0

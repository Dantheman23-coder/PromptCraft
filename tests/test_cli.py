from click.testing import CliRunner
from promptcraft.cli import cli


def test_cli_rewrite(monkeypatch):
    runner = CliRunner()
    monkeypatch.setattr("promptcraft.ai_client.AIClient.chat", lambda self, p: "ok")
    result = runner.invoke(cli, ["rewrite", "hi"])
    assert result.exit_code == 0
    assert "ok" in result.output

from click.testing import CliRunner
from interviewprep.cli import main
from interviewprep import storage


def test_add_command_saves_problem(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    runner = CliRunner()
    result = runner.invoke(
        main,
        ["add"],
        input="\n".join(
            [
                "Two Sum",
                "hash map",
                "Easy",
                "3",
                "15",
                "n",
                "n",
                "",
            ]
        )
        + "\n",
    )
    print(result.output)
    print(repr(result.output))
    assert result.exit_code == 0
    problems = storage.load_problems()
    assert len(problems) == 1
    assert problems[0].problem_name == "Two Sum"
    assert problems[0].pattern == "hash map"


def test_add_command_rejects_invalid_difficulty(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    runner = CliRunner()
    result = runner.invoke(
        main,
        ["add"],
        input="\n".join(
            [
                "Two Sum",
                "hash map",
                "Invalid",
                "Easy",
                "3",
                "15",
                "n",
                "n",
                "",
            ]
        )
        + "\n",
    )

    assert result.exit_code == 0
    problems = storage.load_problems()
    assert len(problems) == 1

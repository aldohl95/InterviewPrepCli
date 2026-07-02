from click.testing import CliRunner
from interviewprep.cli import main
from interviewprep import storage
from interviewprep.models import Problem, LeetcodeDifficulty


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


def make_problem(**kwargs) -> Problem:
    defaults = {
        "problem_name": "Two Sum",
        "pattern": "hash map",
        "leetcode_difficulty": LeetcodeDifficulty.EASY,
        "personal_difficulty": 3,
        "time_taken_min": 15,
        "needed_help": False,
        "needs_resolve": False,
    }

    defaults.update(kwargs)
    return Problem(**defaults)


def test_list_command_shows_problems(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    problem = make_problem()
    storage.save_problems([problem])
    runner = CliRunner()

    result = runner.invoke(
        main,
        ["list"],
    )

    assert result.exit_code == 0
    assert "Two Sum" in result.output


def test_list_command_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    runner = CliRunner()

    result = runner.invoke(
        main,
        ["list"],
    )

    assert "No Saved problems yet." in result.output


def test_view_command_shows_problem(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    runner = CliRunner()

    problem = make_problem()
    storage.save_problems([problem])

    result = runner.invoke(
        main,
        ["view", "1"],
    )

    assert "Two Sum" in result.output


def test_view_command_invalid_number(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    runner = CliRunner()

    problem = make_problem()
    storage.save_problems([problem])

    result = runner.invoke(main, ["view", "5"])

    assert result.exit_code == 1


def test_edit_command_updates_problem(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    problem = make_problem()
    runner = CliRunner()
    storage.save_problems([problem])

    result = runner.invoke(
        main,
        ["edit", "1"],
        input="\n".join(
            [
                "Reverse Linked List",
                "Linked List",
                "Easy",
                "5",
                "15",
                "\n",
                "\n",
                "\n",
            ]
        )
        + "\n",
    )
    assert result.exit_code == 0
    problems = storage.load_problems()
    assert problems[0].problem_name == "Reverse Linked List"


def test_edit_command_invalid_number(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    runner = CliRunner()
    problem = make_problem()
    storage.save_problems([problem])

    result = runner.invoke(
        main,
        ["edit", "99"],
        input="\n".join(
            [
                "\n",
                "\n",
                "\n",
                "\n",
                "15",
                "\n",
                "\n",
                "\n",
                "\n",
            ]
        )
        + "\n",
    )
    assert result.exit_code == 1

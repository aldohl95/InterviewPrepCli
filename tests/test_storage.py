from interviewprep.models import Problem, LeetcodeDifficulty
from datetime import date
from interviewprep import storage


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


def test_save_and_load_empty_list(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    storage.save_problems([])
    result = storage.load_problems()

    assert result == []


def test_save_and_load_single_problem(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    problem = make_problem()
    storage.save_problems([problem])
    result = storage.load_problems()

    assert len(result) == 1
    assert result[0].problem_name == "Two Sum"
    assert result[0].pattern == "hash map"
    assert result[0].leetcode_difficulty == LeetcodeDifficulty.EASY
    assert result[0].date_attempted == date.today()


def test_save_and_load_multiple_problems(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    problems = [
        make_problem(problem_name="Two Sum"),
        make_problem(problem_name="Best Time to Buy Stock", personal_difficulty=6),
        make_problem(problem_name="Contains Duplicate", needs_resolve=True),
    ]

    storage.save_problems(problems)
    result = storage.load_problems()

    assert len(result) == 3
    assert result[0].problem_name == "Two Sum"
    assert result[1].problem_name == "Best Time to Buy Stock"
    assert result[1].personal_difficulty == 6
    assert result[2].problem_name == "Contains Duplicate"
    assert result[2].needs_resolve is True


def test_load_returns_empty_list_when_no_file(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "problems.json")

    result = storage.load_problems()

    assert result == []

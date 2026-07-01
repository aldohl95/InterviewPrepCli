from datetime import date
from interviewprep.models import Problem, LeetcodeDifficulty
import pytest


def test_problem_creation():
    p = Problem(
        problem_name="Two sum",
        pattern="Hash Map",
        leetcode_difficulty=LeetcodeDifficulty.EASY,
        personal_difficulty=3,
        time_taken_min=15,
        needed_help=False,
        needs_resolve=False,
    )
    assert p.problem_name == "Two sum"
    assert p.leetcode_difficulty == LeetcodeDifficulty.EASY
    assert p.date_attempted == date.today()
    assert p.next_review_date is None
    assert p.recognition_sentence is None


def test_invalid_difficulty_rasies_error():
    with pytest.raises(ValueError):
        LeetcodeDifficulty("Moderate")


def test_personal_difficulty_accepts_boundary_values():
    p_low = Problem(
        problem_name="Two sum",
        pattern="Hash Map",
        leetcode_difficulty=LeetcodeDifficulty.EASY,
        personal_difficulty=1,
        time_taken_min=15,
        needed_help=False,
        needs_resolve=False,
    )
    p_high = Problem(
        problem_name="Two sum",
        pattern="Hash Map",
        leetcode_difficulty=LeetcodeDifficulty.EASY,
        personal_difficulty=10,
        time_taken_min=15,
        needed_help=False,
        needs_resolve=False,
    )
    assert p_low.personal_difficulty == 1
    assert p_high.personal_difficulty == 10


def test_personal_difficulty_rejects_below_range():
    with pytest.raises(ValueError):
        Problem(
            problem_name="Bad Problem",
            pattern="hash map",
            leetcode_difficulty=LeetcodeDifficulty.EASY,
            personal_difficulty=0,
            time_taken_min=10,
            needed_help=False,
            needs_resolve=False,
        )


def test_personal_difficulty_rejects_invalid_values():
    with pytest.raises(ValueError):
        Problem(
            problem_name="Bad Problem",
            pattern="hash map",
            leetcode_difficulty=LeetcodeDifficulty.EASY,
            personal_difficulty=11,
            time_taken_min=10,
            needed_help=False,
            needs_resolve=False,
        )

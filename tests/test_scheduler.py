from datetime import date
from interviewprep.models import Problem, LeetcodeDifficulty
from interviewprep.scheduler import calculate_next_review_date


def make_problem(personal_difficulty: int = 5, needed_help: bool = False) -> Problem:
    return Problem(
        problem_name="Test Problem",
        pattern="test",
        leetcode_difficulty=LeetcodeDifficulty.EASY,
        personal_difficulty=personal_difficulty,
        time_taken_min=10,
        needed_help=needed_help,
        needs_resolve=False,
        date_attempted=date(2026, 1, 1),
    )


def test_first_review_hard_problem_schedules_one_day_out():
    problem = make_problem(personal_difficulty=8)
    result = calculate_next_review_date(problem, prior_attempts=[])
    assert result == date(2026, 1, 2)


def test_first_review_easy_problem_schedules_three_days_out():
    problem = make_problem(personal_difficulty=3)
    result = calculate_next_review_date(problem, prior_attempts=[])
    assert result == date(2026, 1, 4)


def test_first_review_boundary_at_five_schedules_three_days_out():
    problem = make_problem(personal_difficulty=5)
    result = calculate_next_review_date(problem, prior_attempts=[])
    assert result == date(2026, 1, 4)


def test_first_review_boundary_at_six_schedules_one_day_out():
    problem = make_problem(personal_difficulty=6)
    result = calculate_next_review_date(problem, prior_attempts=[])
    assert result == date(2026, 1, 2)


def test_subsequent_needed_help_schedules_one_day_out():
    prior = [make_problem()]
    problem = make_problem(personal_difficulty=3, needed_help=True)
    result = calculate_next_review_date(problem, prior_attempts=prior)
    assert result == date(2026, 1, 2)


def test_subsequent_difficulty_eight_schedules_one_day_out():
    prior = [make_problem()]
    problem = make_problem(personal_difficulty=8)
    result = calculate_next_review_date(problem, prior_attempts=prior)
    assert result == date(2026, 1, 2)


def test_subsequent_difficulty_six_schedules_three_days_out():
    prior = [make_problem()]
    problem = make_problem(personal_difficulty=6)
    result = calculate_next_review_date(problem, prior_attempts=prior)
    assert result == date(2026, 1, 4)


def test_subsequent_difficulty_four_schedules_seven_days_out():
    prior = [make_problem()]
    problem = make_problem(personal_difficulty=4)
    result = calculate_next_review_date(problem, prior_attempts=prior)
    assert result == date(2026, 1, 8)


def test_subsequent_difficulty_two_schedules_fourteen_days_out():
    prior = [make_problem()]
    problem = make_problem(personal_difficulty=2)
    result = calculate_next_review_date(problem, prior_attempts=prior)
    assert result == date(2026, 1, 15)


def test_subsequent_difficulty_one_schedules_thirty_days_out():
    prior = [make_problem()]
    problem = make_problem(personal_difficulty=1)
    result = calculate_next_review_date(problem, prior_attempts=prior)
    assert result == date(2026, 1, 31)

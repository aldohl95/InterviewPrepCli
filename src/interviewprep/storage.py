import json
from pathlib import Path
from datetime import date
from platformdirs import user_data_dir
from interviewprep.models import Problem, LeetcodeDifficulty

DATA_DIR = Path(user_data_dir("interviewprep"))
DATA_FILE = DATA_DIR / "problems.json"
STREAK_FILE = DATA_DIR / "streak.json"


def _problem_to_dict(problem: Problem) -> dict:
    return {
        "problem_name": problem.problem_name,
        "pattern": problem.pattern,
        "leetcode_difficulty": problem.leetcode_difficulty.value,
        "personal_difficulty": problem.personal_difficulty,
        "time_taken_min": problem.time_taken_min,
        "needed_help": problem.needed_help,
        "needs_resolve": problem.needs_resolve,
        "date_attempted": problem.date_attempted.isoformat(),
        "next_review_date": (
            problem.next_review_date.isoformat() if problem.next_review_date else None
        ),
        "recognition_sentence": problem.recognition_sentence,
    }


def _dict_to_problem(data: dict) -> Problem:
    return Problem(
        problem_name=data["problem_name"],
        pattern=data["pattern"],
        leetcode_difficulty=LeetcodeDifficulty(data["leetcode_difficulty"]),
        personal_difficulty=data["personal_difficulty"],
        time_taken_min=data["time_taken_min"],
        needed_help=data["needed_help"],
        needs_resolve=data["needs_resolve"],
        date_attempted=date.fromisoformat(data["date_attempted"]),
        next_review_date=(
            date.fromisoformat(data["next_review_date"])
            if data["next_review_date"]
            else None
        ),
        recognition_sentence=data.get("recognition_sentence"),
    )


def save_streak(streak: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(STREAK_FILE, "w") as f:
        json.dump(streak, f, indent=2)


def load_streak() -> dict:
    if not STREAK_FILE.exists():
        return {
            "current_streak": 0,
            "longest_streak": 0,
            "last_completed": None,
        }
    with open(STREAK_FILE) as f:
        return json.load(f)


def save_problems(problems: list[Problem]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump([_problem_to_dict(p) for p in problems], f, indent=2)


def load_problems() -> list[Problem]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        return [_dict_to_problem(d) for d in json.load(f)]


def find_attempts_by_name(problems: list[Problem], name: str) -> list[Problem]:
    return [p for p in problems if p.problem_name == name]


def find_attempts_by_needs_resolve(
    problems: list[Problem], needs_resolve: bool
) -> list[Problem]:
    return [p for p in problems if p.needs_resolve == needs_resolve]


def find_overdue_attempts_by_date(
    problems: list[Problem], review_date: date
) -> list[Problem]:
    return [
        p
        for p in problems
        if p.next_review_date is not None and p.next_review_date < review_date
    ]


def find_due_today_attempts_by_date(
    problems: list[Problem], review_date: date
) -> list[Problem]:
    return [
        p
        for p in problems
        if p.next_review_date is not None and p.next_review_date == review_date
    ]


def find_attempts_due_later_by_date(
    problems: list[Problem], review_date: date
) -> list[Problem]:
    return [
        p
        for p in problems
        if p.next_review_date is not None and p.next_review_date > review_date
    ]

from dataclasses import dataclass, field
from datetime import date
from typing import Optional
from enum import Enum


class LeetcodeDifficulty(Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


@dataclass
class Problem:
    problem_name: str
    pattern: str
    leetcode_difficulty: LeetcodeDifficulty
    personal_difficulty: int
    time_taken_min: int
    needed_help: bool
    needs_resolve: bool
    date_attempted: date = field(default_factory=date.today)
    next_review_date: Optional[date] = None
    recognition_sentence: Optional[str] = None

    def __post_init__(self):
        self.problem_name = self.problem_name.strip()
        if not 1 <= self.personal_difficulty <= 10:
            raise ValueError(
                "personal_difficulty must be between 1 & 10, "
                f"{self.personal_difficulty} not a valid number"
            )

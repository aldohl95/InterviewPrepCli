from datetime import timedelta, date
from interviewprep.models import Problem


def calculate_next_review_date(problem: Problem, prior_attempts: list[Problem]) -> date:
    if not prior_attempts:
        if problem.personal_difficulty > 5:
            days = 1
        else:
            days = 3
    else:
        if problem.needed_help or problem.personal_difficulty >= 8:
            days = 1
        elif problem.personal_difficulty >= 6:
            days = 3
        elif problem.personal_difficulty >= 4:
            days = 7
        elif problem.personal_difficulty >= 2:
            days = 14
        else:
            days = 30
    return problem.date_attempted + timedelta(days=days)

from typing import Optional
from interviewprep.models import Problem, LeetcodeDifficulty
import click


def prompt_for_problem(existing: Optional[Problem] = None) -> Problem:
    problem_name = click.prompt(
        "Problem Name:  ", default=existing.problem_name if existing else ""
    )

    pattern = click.prompt("Pattern: ", default=existing.pattern if existing else "")

    difficulty_choice = click.prompt(
        "Leetcode Difficulty: ",
        type=click.Choice(["Easy", "Medium", "Hard"], case_sensitive=False),
        default=existing.leetcode_difficulty.value if existing else "Easy",
    )

    leetcode_difficulty = LeetcodeDifficulty(difficulty_choice.capitalize())

    personal_difficulty = click.prompt(
        "Personal Difficulty: ",
        type=click.IntRange(1, 10),
        default=existing.personal_difficulty if existing else 1,
    )

    time_taken_min = click.prompt(
        "Time Taken to Complete(min): ",
        type=int,
        default=existing.time_taken_min if existing else 15,
    )

    needed_help = click.confirm(
        "Did you need help/hint? ", default=existing.needed_help if existing else False
    )

    needs_resolve = click.confirm(
        "Does this need resolve? ",
        default=existing.needs_resolve if existing else False,
    )

    recognition_sentence = click.prompt(
        "Recognition Sentence: ",
        default=existing.recognition_sentence or "" if existing else "",
        show_default=False,
    )

    problem = Problem(
        problem_name=problem_name,
        pattern=pattern,
        leetcode_difficulty=leetcode_difficulty,
        personal_difficulty=personal_difficulty,
        time_taken_min=time_taken_min,
        needed_help=needed_help,
        needs_resolve=needs_resolve,
        recognition_sentence=recognition_sentence if recognition_sentence else None,
    )

    return problem

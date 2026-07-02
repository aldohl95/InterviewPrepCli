import click
from interviewprep.storage import load_problems, save_problems
from interviewprep.models import Problem, LeetcodeDifficulty


@click.command()
@click.argument("number", type=int)
def edit(number):
    problems = load_problems()
    num = number - 1

    if 0 <= num < len(problems):
        problem = problems[num]
        problem_name = click.prompt("Problem Name: ", default=problem.problem_name)

        pattern = click.prompt("Pattern: ", default=problem.pattern)

        difficulty_choice = click.prompt(
            "Leetcode Dificulty: ",
            type=click.Choice(["Easy", "Medium", "Hard"], case_sensitive=False),
            default=problem.leetcode_difficulty.value,
        )

        leetcode_difficulty = LeetcodeDifficulty(difficulty_choice.capitalize())

        personal_difficulty = click.prompt(
            "Personal Difficulty(1-10): ",
            type=click.IntRange(1, 10),
            default=problem.personal_difficulty,
        )

        time_taken_min = click.prompt(
            "How long to solve(mins): ", type=int, default=problem.time_taken_min
        )

        needed_help = click.confirm(
            "Did you use help/hint: ", default=problem.needed_help
        )

        needs_resolve = click.confirm(
            "Does this need resolve? ", default=problem.needs_resolve
        )

        recognition_sentence = click.prompt(
            "Recognition Sentence: ",
            default=problem.recognition_sentence or "",
            show_default=False,
        )

        updated_problem = Problem(
            problem_name=problem_name,
            pattern=pattern,
            leetcode_difficulty=leetcode_difficulty,
            personal_difficulty=personal_difficulty,
            time_taken_min=time_taken_min,
            needed_help=needed_help,
            needs_resolve=needs_resolve,
            recognition_sentence=recognition_sentence,
        )

        problems[num] = updated_problem
        save_problems(problems)
        click.echo("\n Edit Saved Succesfully!")
    else:
        click.echo("That problem does not exist!")
        raise SystemExit(1)

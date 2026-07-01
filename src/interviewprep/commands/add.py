import click
from interviewprep.models import Problem, LeetcodeDifficulty
from interviewprep.storage import save_problems, load_problems


@click.command()
def add():
    click.echo("===Add New Problem===")

    problem_name = click.prompt("Problem name")
    pattern = click.prompt("What pattern is this problem?")

    difficulty_choice = click.prompt(
        "Leetcode Difficulty",
        type=click.Choice(["Easy", "Medium", "Hard"], case_sensitive=False),
    )

    leetcode_difficulty = LeetcodeDifficulty(difficulty_choice.capitalize())

    personal_difficulty = click.prompt(
        "Personal difficulty (1-10)", type=click.IntRange(1, 10)
    )

    time_taken_min = click.prompt("How long to solve(mins):", type=int)
    needed_help = click.confirm("Did you use help/hint")
    needs_resolve = click.confirm("Does this need resolve?")
    recognition_sentence = click.prompt(
        "Recognition Sentence(Optional)", default="", show_default=False
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

    problems = load_problems()
    problems.append(problem)
    save_problems(problems)

    click.echo(f"\nSaved '{problem_name}' saved successfully")

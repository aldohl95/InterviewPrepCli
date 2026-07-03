import click
from interviewprep.storage import load_problems, save_problems
from interviewprep.prompts import prompt_for_problem


@click.command()
@click.argument("number", type=int)
def edit(number):
    problems = load_problems()
    num = number - 1

    if 0 <= num < len(problems):
        problem = problems[num]

        updated_problem = prompt_for_problem(existing=problem)

        problems[num] = updated_problem
        save_problems(problems)
        click.echo("\n Edit Saved Succesfully!")
    else:
        click.echo("That problem does not exist!")
        raise SystemExit(1)

import click
from interviewprep.storage import save_problems, load_problems
from interviewprep.prompts import prompt_for_problem


@click.command()
def add():
    click.echo("===Add New Problem===")

    problem = prompt_for_problem()

    problems = load_problems()
    problems.append(problem)
    save_problems(problems)

    click.echo(f"\nSaved '{problem.problem_name}' saved successfully")

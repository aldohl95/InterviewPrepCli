import click
from interviewprep.storage import save_problems, load_problems, find_attempts_by_name
from interviewprep.prompts import prompt_for_problem
from interviewprep.scheduler import calculate_next_review_date


@click.command()
def add():
    click.echo("===Add New Problem===")

    problem = prompt_for_problem()
    problems = load_problems()
    prior = find_attempts_by_name(problems, problem.problem_name)
    problem.next_review_date = calculate_next_review_date(problem, prior)
    problems.append(problem)
    save_problems(problems)

    click.echo(f"\nSaved '{problem.problem_name}' saved successfully")

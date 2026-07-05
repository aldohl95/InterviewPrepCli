import click
from interviewprep.storage import load_problems, save_problems, find_attempts_by_name
from datetime import date
from interviewprep.prompts import prompt_for_problem
from interviewprep.scheduler import calculate_next_review_date


@click.command()
@click.argument("number", type=int)
def review(number):
    problems = load_problems()
    num = number - 1

    if 0 <= num < len(problems):
        reviewed_problem = problems[num]

        new_problem = prompt_for_problem(reviewed_problem)
        new_problem.date_attempted = date.today()
        prior = find_attempts_by_name(problems, new_problem.problem_name)
        new_problem.next_review_date = calculate_next_review_date(new_problem, prior)
        problems.append(new_problem)
        save_problems(problems)
    else:
        click.echo("That problem does not exist")
        raise SystemExit(1)

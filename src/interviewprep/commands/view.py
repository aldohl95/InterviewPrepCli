import click
from interviewprep.storage import load_problems


@click.command()
@click.argument("number", type=int)
def view(number):
    problems = load_problems()
    num = number - 1

    if 0 <= num < len(problems):
        problem = problems[num]
        click.echo(f"Problem Name: {problem.problem_name}")
        click.echo(f"Pattern: {problem.pattern}")
        click.echo(f"Leetcode Difficulty: {problem.leetcode_difficulty.value}")
        click.echo(f"Personal Difficulty: {problem.personal_difficulty}")
        click.echo(f"Time Taken(min): {problem.time_taken_min}")
        click.echo(f"Did You Use Help {problem.needed_help}")
        click.echo(f"Needs Resolve: {problem.needs_resolve}")
        click.echo(f"Date Attempted: {problem.date_attempted}")
        click.echo(f"Next Review Date: {problem.next_review_date}")
        click.echo(f"Recognition Sentence: {problem.recognition_sentence}")
    else:
        click.echo("Error: invalid problem number.")
        raise SystemExit(1)

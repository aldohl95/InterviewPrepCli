import click
from interviewprep.storage import load_problems, save_problems


@click.command()
@click.argument("number", type=int)
def delete(number):
    problems = load_problems()
    num = number - 1

    if 0 <= num < len(problems):
        problem = problems[num]
        sure = click.confirm(
            f"Are you sure you want to delete problem {number}:{problem.problem_name}? "
        )
        if sure:
            problems.pop(num)
            save_problems(problems)
            click.echo(f"You have Succesfully deleted problem {number}")
        else:
            click.echo("Problem was not deleted")
    else:
        click.echo(f"Problem {number} does not exist")
        raise SystemExit(1)

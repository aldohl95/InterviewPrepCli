import click
from interviewprep.storage import load_problems
from rich.console import Console
from rich.table import Table


@click.command(name="list")
def list_problems():
    click.echo("===List Problems===")

    problems = load_problems()
    console = Console()
    table = Table()

    table.add_column("#")
    table.add_column("Problem Name")
    table.add_column("Date Attempted")
    table.add_column("Personal Difficulty")
    table.add_column("Needs Resolve")

    if not problems:
        click.echo("No Saved problems yet.")
        return

    for i, problem in enumerate(problems, start=1):
        table.add_row(
            str(i),
            problem.problem_name,
            problem.date_attempted.isoformat(),
            str(problem.personal_difficulty),
            "Yes" if problem.needs_resolve else "No",
        )

    console.print(table)

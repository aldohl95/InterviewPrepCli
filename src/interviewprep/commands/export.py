import click
from pathlib import Path
from interviewprep.storage import load_problems, write_problems_to_file


@click.command()
@click.option("--output", "-o", required=True, type=click.Path())
def export(output):
    path = Path(output)
    problems = load_problems()
    count = len(problems)

    if count == 0:
        click.echo("No problems to export")
        return

    write_problems_to_file(problems, path)
    click.echo(f"You have successfully exported {count} problems to {path}")

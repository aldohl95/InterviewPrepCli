import click
from interviewprep.storage import load_problems, save_problems, read_problems_from_file
from pathlib import Path


@click.command(name="import")
@click.option("--input", "-i", required=True, type=click.Path())
@click.option(
    "--mode",
    type=click.Choice(["merge", "replace"], case_sensitive=False),
    default="merge",
    show_default=True,
)
def import_problems(input, mode):
    path = Path(input)

    try:
        new_problems = read_problems_from_file(path)
    except FileNotFoundError:
        click.echo(f"Error: file '{path}' not found.")
        raise SystemExit(1)
    except ValueError as e:
        click.echo(f"Error reading file: {e}")
        raise SystemExit(1)

    count = len(new_problems)

    if mode == "merge":
        existing = load_problems()
        save_problems(existing + new_problems)
        click.echo(f"You have successfully imported {count} new problems to your list")
    elif mode == "replace":
        save_problems(new_problems)
        click.echo(f"You have succesfully imported {count} problems")

import click
from interviewprep.commands.add import add


@click.group()
def main():
    """Interview CLI - manage your technical interview preparation."""
    pass


main.add_command(add)

import click
from interviewprep.commands.add import add
from interviewprep.commands.list import list_problems


@click.group()
def main():
    """Interview CLI - manage your technical interview preparation."""
    pass


main.add_command(add)
main.add_command(list_problems)

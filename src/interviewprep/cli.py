import click
from interviewprep.commands.add import add
from interviewprep.commands.list import list_problems
from interviewprep.commands.view import view
from interviewprep.commands.edit import edit
from interviewprep.commands.delete import delete
from interviewprep.commands.review import review
from interviewprep.commands.dashboard import dashboard


@click.group()
def main():
    """Interview CLI - manage your technical interview preparation."""
    pass


main.add_command(add)
main.add_command(list_problems)
main.add_command(view)
main.add_command(edit)
main.add_command(delete)
main.add_command(review)
main.add_command(dashboard)

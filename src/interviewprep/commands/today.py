import click
from interviewprep.storage import (
    load_problems,
    find_overdue_attempts_by_date,
    find_due_today_attempts_by_date,
    find_attempts_due_later_by_date,
    load_streak,
)
from rich.console import Console
from rich.table import Table
from datetime import date
import heapq


@click.command()
def today():
    problems = load_problems()
    console = Console()
    overdue_table = Table()
    due_today_table = Table()
    upcoming_due_table = Table()
    streak_table = Table()
    today = date.today()
    streak = load_streak()

    overdue_table.add_column("#")
    overdue_table.add_column("Problem name")
    overdue_table.add_column("Pattern")
    overdue_table.add_column("Days Overdue")
    due_today_table.add_column("#")
    due_today_table.add_column("Problem Name")
    due_today_table.add_column("Pattern")
    upcoming_due_table.add_column("#")
    upcoming_due_table.add_column("Problem Name")
    upcoming_due_table.add_column("Pattern")
    upcoming_due_table.add_column("Resolve Date")
    streak_table.add_column("Current Streak")
    streak_table.add_column("Longest Streak")
    streak_table.add_column("Last problem Completed")

    if not problems:
        click.echo("No Saved Problems")
        return

    # overdue Table
    overdue = find_overdue_attempts_by_date(problems, today)
    for i, problem in enumerate(overdue, start=1):
        days_overdue = (today - problem.next_review_date).days
        overdue_table.add_row(
            str(i),
            problem.problem_name,
            problem.pattern,
            days_overdue,
        )

    # due today Table
    due_today = find_due_today_attempts_by_date(problems, today)
    for i, problem in enumerate(due_today, start=1):
        due_today_table.add_row(
            str(i),
            problem.problem_name,
            problem.pattern,
        )

    # due later Table
    due_later = find_attempts_due_later_by_date(problems, today)
    five_upcoming_resolves = heapq.nsmallest(
        5, due_later, key=lambda p: p.next_review_date
    )
    for i, problem in enumerate(five_upcoming_resolves, start=1):
        upcoming_due_table.add_row(
            str(i),
            problem.problem_name,
            problem.pattern,
            problem.next_review_date.isoformat(),
        )

    # streak table
    streak_table.add_row(
        str(streak["current_streak"]),
        str(streak["longest_streak"]),
        (streak["last_completed"]),
    )

    if due_today:
        console.print("Problems due today")
        console.print(due_today_table)
    else:
        click.echo("No problems due today")

    if overdue:
        click.echo("Problems Overdue")
        console.print(overdue_table)
    else:
        click.echo("No problems overdue")
    if due_later:
        click.echo("Upcoming Problems")
        console.print(upcoming_due_table)
    else:
        click.echo("No upcoming problems due")
    click.echo("Streak")
    console.print(streak_table)

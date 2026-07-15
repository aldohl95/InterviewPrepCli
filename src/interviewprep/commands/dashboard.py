import click
from interviewprep.storage import load_problems, find_attempts_by_needs_resolve
from rich.console import Console
from rich.table import Table
import heapq


@click.command()
def dashboard():
    problems = load_problems()
    console = Console()
    freq_table = Table()
    average_difficulty_table = Table()
    resolve_count_table = Table()
    leetcode_difficulty_table = Table()
    pattern_frequency = {}
    difficulty_frequency = {}
    personal_difficulty_frequency = {}

    leetcode_difficulty_table.add_column("#")
    leetcode_difficulty_table.add_column("Leetcode Difficulty")
    leetcode_difficulty_table.add_column("Solved Count")
    freq_table.add_column("#")
    freq_table.add_column("Pattern")
    freq_table.add_column("Solved Count")
    average_difficulty_table.add_column("#")
    average_difficulty_table.add_column("Pattern")
    average_difficulty_table.add_column("Average Personal Difficulty")
    resolve_count_table.add_column("Total Resolves Needed")

    if not problems:
        click.echo("No Saved Problems yet")
        return

    # for Leetcode Difficulty
    for problem in problems:
        difficulty_frequency[problem.leetcode_difficulty.value] = (
            1 + difficulty_frequency.get(problem.leetcode_difficulty.value, 0)
        )

    for i, (difficulty, count) in enumerate(difficulty_frequency.items(), start=1):
        leetcode_difficulty_table.add_row(str(i), difficulty, str(count))

    # for patter frequency
    for problem in problems:
        pattern_frequency[problem.pattern] = 1 + pattern_frequency.get(
            problem.pattern, 0
        )

    top_five_patterns = heapq.nlargest(
        5, pattern_frequency.items(), key=lambda item: item[1]
    )

    for i, (pattern, count) in enumerate(top_five_patterns, start=1):
        freq_table.add_row(str(i), pattern, str(count))

    # for average difficulty
    for problem in problems:
        pattern = problem.pattern
        difficulty = problem.personal_difficulty

        if pattern not in personal_difficulty_frequency:
            personal_difficulty_frequency[pattern] = {"total_difficulty": 0, "count": 0}

        personal_difficulty_frequency[pattern]["total_difficulty"] += difficulty
        personal_difficulty_frequency[pattern]["count"] += 1

    for i, (pattern, count) in enumerate(
        personal_difficulty_frequency.items(), start=1
    ):
        average = count["total_difficulty"] / count["count"]
        average_difficulty_table.add_row(str(i), pattern, str(average))

    # problems needing resolve
    resolve_problems = find_attempts_by_needs_resolve(problems, True)
    resolve_count_table.add_row(str(len(resolve_problems)))

    console.print(leetcode_difficulty_table)
    console.print(freq_table)
    console.print(average_difficulty_table)
    console.print(resolve_count_table)

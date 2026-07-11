import click
from interviewprep.storage import load_problems, save_problems

@click.command()
def dashboard():
  problems = load_problems()
  console.Console()
  freq_table = Table()
  average_difficulty_table == Table()
  resolve_count_table = Table()

  freq_table.add_column("#")
  freq_table.add_column("Pattern")
  freq_table.add_column("Solved Count")
  average_difficulty_table.add_column("#")
  average_difficulty_table.add_column("Pattern")
  average_difficulty_table.add_column("Average Personal Difficulty")
  resolve_count_table.add_column("Resolves Today")
  resolve_count_table.add_column("Total Resolves needed")

  

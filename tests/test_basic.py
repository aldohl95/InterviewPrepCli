def test_cli_entry_point_exists():
  from interviewprep.cli import main
  assert callable(main)
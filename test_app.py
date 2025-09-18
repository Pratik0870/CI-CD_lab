def test_app_output(capsys):
    import app
    captured = capsys.readouterr()
    # Check that the output contains our expected string
    assert "Hello, CI/CD World!" in captured.out

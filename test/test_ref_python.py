import pytest
from click.testing import CliRunner
from src.reference_python_cli_app.cli.module_cli import run_operation


def test_should_return_success_result():
    runner = CliRunner()
    result = runner.invoke(run_operation, ["--param_option=someoption"])
    assert result.output.strip() == "Method executed from CLI\nsomeoption"


def test_should_return_error_result_on_wrong_argument():
    runner = CliRunner()
    result = runner.invoke(
        run_operation, ["--param_option=someoption", "--unexistent=wrong"]
    )
    assert result.output.strip() == (
        "Usage: run_operation [OPTIONS]\n"
        "Try 'run_operation --help' for help.\n"
        "\n"
        "Error: No such option: --unexistent"
    )

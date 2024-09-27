import click
import logging
import sys
import os
#from pyfiglet import Figlet
from src.supplier_app.cli.supplier_cli import supplier_cli


@click.group()
@click.version_option()
@click.pass_context
def cli(ctx):
    """Reference CLI python repository.
    (c) 2023 ASML
    """
    show_cli_header()
    ctx.ensure_object(dict)


cli.add_command(supplier_cli)


def show_cli_header():
    logging.basicConfig(stream=sys.stdout)

    click.echo("-------------------------------------------------------")
    #click.echo(Figlet().renderText("Supplier CLI"))
    click.echo(f'Reference python CLI {os.getenv("_ref_python_cliapp", "")}')
    click.echo("(c) 2024 VDL")
    click.echo("-------------------------------------------------------")
    logging.getLogger("supplier_cli").setLevel(logging.DEBUG)


if __name__ == "__main__":
    cli(obj={})

import click
from supplier_app.cli.supplierLib.Database import Database
@click.group("supplier_cli")
@click.pass_context
def supplier_cli(ctx):
    """
    Component supplier_cli
    this has a basic method to execute a simple call but can be used as an example for new modules
    """


@supplier_cli.command("get_database_connection")
@click.option(
    "--param_option",
    prompt="Parameter description for user to read. It's possible to add as much parameters as needed and also optional parameters",
    help="More details about parameter or possible values",
)
@click.pass_context
def get_database_connection(ctx, param_option):
    click.echo("Get Database Connection")
    db_obj = Database()

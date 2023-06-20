import click

from .lib import say


@click.command("py-cowsay")
@click.argument("message")
@click.option(
    "-b",
    "--bold",
    is_flag=True,
    help="Make the message bold.",
)
def cowsay(message: str, bold: bool):
    say(message, bold=bold)

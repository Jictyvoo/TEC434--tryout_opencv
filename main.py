import click

from modules import MODULES_CLI


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(name: str):
    """Simple program that greets NAME."""
    click.echo(f"Hello {name}!")


@click.group()
def cli_executor():
    pass


if __name__ == "__main__":
    # Start to add all commands to the cli executor
    commands = [hello]
    commands.extend(MODULES_CLI)
    for command in commands:
        cli_executor.add_command(command)

    # Call and start the cli
    cli_executor()

import click

from modules.remove_noise import remove_noise


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
    for command in [hello, remove_noise]:
        cli_executor.add_command(command)

    # Call and start the cli
    cli_executor()

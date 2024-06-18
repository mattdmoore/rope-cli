import click 
from rope_cli import refactor

@click.group()
def cli():
    """Rope CLI: A tool for refactoring Python code."""
    pass

@cli.command()
@click.argument('path')
@click.argument('old_name')
@click.argument('new_name')
def rename(path, old_name, new_name):
    """Rename a variable, function, or class.
    """
    refactor.rename(path, old_name, new_name)

@cli.command()
def undo():
    """Undo the last action
    """
    refactor.undo()

@cli.command()
def redo():
    """Redo the last action
    """
    refactor.redo()

if __name__ == '__main__':
    cli()

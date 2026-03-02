import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import click
from commands.setup import setup
from commands.doctor import doctor
from commands.upgrade import upgrade
from commands.documentation import documentation, docrefactoring
from commands.programming import programming, devrefactoring
from commands.media import images, videos
from commands.content import content, characters, lora

@click.group()
def cli():
    """iasuite - Suite de herramientas IA para desarrollo y creación de contenido."""
    pass

cli.add_command(setup)
cli.add_command(doctor)
cli.add_command(upgrade)
cli.add_command(documentation)
cli.add_command(docrefactoring)
cli.add_command(programming)
cli.add_command(devrefactoring)
cli.add_command(images)
cli.add_command(videos)
cli.add_command(content)
cli.add_command(characters)
cli.add_command(lora)

if __name__ == "__main__":
    cli()

# commands/characters.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv

@click.command()
@click.option('--name', '-n', default=None, help='Nombre del personaje IA a crear.')
def characters(name):
    """Crea un personaje IA consistente con personalidad, intereses y voz."""
    cmd = f"createcharacter --name {name or ''}"
    run_in_venv("createcontents-env", cmd)

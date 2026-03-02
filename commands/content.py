# commands/content.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv

@click.command()
@click.option('--profile', '-p', default=None, help='Perfil de influencer para generar contenido.')
def content(profile):
    """Genera contenido textual para influencers IA."""
    cmd = f"createcontents --profile {profile or ''}"
    run_in_venv("createcontents-env", cmd)

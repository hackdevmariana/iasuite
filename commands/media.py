# commands/media.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv

# -----------------------
# Subcomando: images
# -----------------------
@click.command()
@click.option('--output', '-o', default='./images', help='Directorio donde guardar imágenes generadas.')
def images(output):
    """Genera imágenes con IA según parámetros y personajes."""
    cmd = f"makeimages --output {output}"
    run_in_venv("makeimages-env", cmd)

# -----------------------
# Subcomando: videos
# -----------------------
@click.command()
@click.option('--output', '-o', default='./videos', help='Directorio donde guardar vídeos generados.')
def videos(output):
    """Genera vídeos con IA (avatares, lip-sync, etc.)."""
    cmd = f"makevideos --output {output}"
    run_in_venv("makevideos-env", cmd)

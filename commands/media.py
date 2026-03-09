# commands/media.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv
from commands.documentation import ensure_venv  # reutilizamos la función global

# -----------------------
# Subcomando: images
# -----------------------
@click.command()
@click.option('--output', '-o', default='./images', help='Directorio donde guardar imágenes generadas.')
@click.pass_context
def images(ctx, output):
    """Genera imágenes con IA según parámetros y personajes."""

    # Mostrar ayuda si solo se ejecuta el comando sin parámetros
    if len(sys.argv) == 2:
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe y makeimages está instalado
    ensure_venv("makeimages-env", "makeimages")

    # Construir el comando
    cmd = f"makeimages --output {output}"

    # Ejecutar dentro del entorno virtual
    run_in_venv("makeimages-env", cmd)


# -----------------------
# Subcomando: videos
# -----------------------
@click.command()
@click.option('--output', '-o', default='./videos', help='Directorio donde guardar vídeos generados.')
@click.pass_context
def videos(ctx, output):
    """Genera vídeos con IA (avatares, lip-sync, etc.)."""

    # Mostrar ayuda si solo se ejecuta el comando sin parámetros
    if len(sys.argv) == 2:
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe y makevideos está instalado
    ensure_venv("makevideos-env", "makevideos")

    # Construir el comando
    cmd = f"makevideos --output {output}"

    # Ejecutar dentro del entorno virtual
    run_in_venv("makevideos-env", cmd)

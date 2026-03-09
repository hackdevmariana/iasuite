# commands/content.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv
from commands.documentation import ensure_venv  # reutilizamos la función global

@click.command()
@click.option('--profile', '-p', default=None, help='Perfil de influencer para generar contenido.')
@click.pass_context
def content(ctx, profile):
    """Genera contenido textual para influencers IA."""

    # Mostrar ayuda si se ejecuta solo el comando sin parámetros
    if len(sys.argv) == 2:
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe y createcontents está instalado
    ensure_venv("createcontents-env", "createcontents")  # nombre del paquete o ejecutable

    # Construir el comando
    cmd = f"createcontents --profile {profile or ''}"

    # Ejecutar dentro del entorno virtual
    run_in_venv("createcontents-env", cmd)

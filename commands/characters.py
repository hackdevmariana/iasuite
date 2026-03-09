# commands/characters.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv
from commands.documentation import ensure_venv  # reutilizamos la función

@click.command()
@click.option('--name', '-n', default=None, help='Nombre del personaje IA a crear.')
@click.pass_context
def characters(ctx, name):
    """Crea un personaje IA consistente con personalidad, intereses y voz."""

    # Mostrar ayuda si se ejecuta sin parámetros (solo el comando)
    if len(sys.argv) == 2:
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe y createcharacter está instalado
    ensure_venv("createcontents-env", "createcharacter")  # nombre del paquete o ejecutable

    # Construir el comando
    cmd = f"createcharacter --name {name or ''}"

    # Ejecutar dentro del entorno virtual
    run_in_venv("createcontents-env", cmd)

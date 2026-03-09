# commands/lora.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv
from commands.documentation import ensure_venv  # reutilizamos la función global

@click.command()
@click.option('--character', '-c', default=None, help='Personaje IA para entrenar LoRA.')
@click.pass_context
def lora(ctx, character):
    """Genera LoRA para un personaje IA específico."""

    # Mostrar ayuda si solo se ejecuta el comando sin parámetros
    if len(sys.argv) == 2:
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe y createlora está instalado
    ensure_venv("createcontents-env", "createlora")

    # Construir el comando
    cmd = f"createlora --character {character or ''}"

    # Ejecutar dentro del entorno virtual
    run_in_venv("createcontents-env", cmd)

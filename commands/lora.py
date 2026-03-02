# commands/lora.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv

@click.command()
@click.option('--character', '-c', default=None, help='Personaje IA para entrenar LoRA.')
def lora(character):
    """Genera LoRA para un personaje IA específico."""
    cmd = f"createlora --character {character or ''}"
    run_in_venv("createcontents-env", cmd)

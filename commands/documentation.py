# commands/documentation.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv

# -----------------------
# Subcomando: documentation
# -----------------------
@click.command()
@click.option('--input', '-i', default='.', help='Directorio raíz de entrada')
@click.option('--output', '-o', default='./doc', help='Directorio donde generar la documentación')
@click.option('--template', '-t', default=None, help='Plantilla markdown para documentación')
@click.option('--git-commit', is_flag=True, help='Hacer commit automático de cada fichero generado')
@click.option('--mode', default='incremental', help='Modo de generación: incremental o full')
def documentation(input, output, template, git_commit, mode):
    """Genera documentación automáticamente con Aider u otra IA."""
    cmd = f"aider --input {input} --output {output} --mode {mode}"
    if template:
        cmd += f" --template {template}"
    if git_commit:
        cmd += " --git-commit"
    
    run_in_venv("docaider-env", cmd)


# -----------------------
# Subcomando: docrefactoring
# -----------------------
@click.command()
@click.option('--input', '-i', default='.', help='Directorio raíz de documentación legacy')
@click.option('--output', '-o', default='./doc', help='Directorio donde generar la documentación refactorizada')
@click.option('--template', '-t', default=None, help='Plantilla markdown')
@click.option('--git-commit', is_flag=True, help='Hacer commit automático de cada fichero generado')
@click.option('--mode', default='incremental', help='Modo de refactorización: incremental o full')
def docrefactoring(input, output, template, git_commit, mode):
    """Genera documentación refactorizada automáticamente con Aider u otra IA."""
    cmd = f"aider-refactor --input {input} --output {output} --mode {mode}"
    if template:
        cmd += f" --template {template}"
    if git_commit:
        cmd += " --git-commit"
    
    run_in_venv("docaider-env", cmd)

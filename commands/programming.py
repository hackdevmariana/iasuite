# commands/programming.py
import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv
from commands.documentation import ensure_venv  # reutilizamos la función global

# -----------------------
# Subcomando: programming
# -----------------------
@click.command()
@click.option('--input', '-i', default='.', help='Directorio raíz del código')
@click.option('--output', '-o', default='./doc', help='Directorio donde generar código o tests')
@click.option('--git-commit', is_flag=True, help='Hacer commit automático de cada fichero generado')
@click.option('--mode', default='incremental', help='Modo de generación: incremental o full')
@click.pass_context
def programming(ctx, input, output, git_commit, mode):
    """Asiste en programación, generación de tests o análisis de código."""

    # Mostrar ayuda si solo se ejecuta el comando sin parámetros
    if len(sys.argv) == 2:
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe y devaider está instalado
    ensure_venv("devaider-env", "devaider")

    # Construir el comando
    cmd = f"devaider --input {input} --output {output} --mode {mode}"
    if git_commit:
        cmd += " --git-commit"

    # Ejecutar dentro del entorno virtual
    run_in_venv("devaider-env", cmd)


# -----------------------
# Subcomando: devrefactoring
# -----------------------
@click.command()
@click.option('--input', '-i', default='.', help='Directorio raíz del código legacy')
@click.option('--output', '-o', default='./doc', help='Directorio donde generar código refactorizado')
@click.option('--git-commit', is_flag=True, help='Hacer commit automático de cada fichero generado')
@click.option('--mode', default='incremental', help='Modo de refactorización: incremental o full')
@click.pass_context
def devrefactoring(ctx, input, output, git_commit, mode):
    """Genera código refactorizado automáticamente."""

    # Mostrar ayuda si solo se ejecuta el comando sin parámetros
    if len(sys.argv) == 2:
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe y devaider-refactor está instalado
    ensure_venv("devaider-env", "devaider-refactor")

    # Construir el comando
    cmd = f"devaider-refactor --input {input} --output {output} --mode {mode}"
    if git_commit:
        cmd += " --git-commit"

    # Ejecutar dentro del entorno virtual
    run_in_venv("devaider-env", cmd)

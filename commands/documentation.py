# commands/documentation.py
import click
import sys
import os

# Importar la función de utils.system
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.system import run_in_venv

def ensure_venv(venv_name: str, package_name: str):
    """Verifica que el entorno virtual exista; si no, lo crea e instala el paquete necesario."""
    venv_path = os.path.join(os.getcwd(), "envs", venv_name)
    bin_path = os.path.join(venv_path, "bin")
    if not os.path.exists(venv_path):
        click.echo(f"Entorno virtual '{venv_name}' no encontrado. Creando...")
        os.system(f"python3 -m venv {venv_path}")
        click.echo(f"Instalando {package_name} en el entorno virtual...")
        os.system(f"{os.path.join(bin_path, 'pip')} install {package_name}")
    return bin_path

# -----------------------
# Subcomando: documentation
# -----------------------
@click.command()
@click.option('--input', '-i', default='.', help='Directorio raíz de entrada')
@click.option('--output', '-o', default='./doc', help='Directorio donde generar la documentación')
@click.option('--template', '-t', default=None, help='Plantilla markdown para documentación')
@click.option('--git-commit', is_flag=True, help='Hacer commit automático de cada fichero generado')
@click.option('--mode', default='incremental', help='Modo de generación: incremental o full')
@click.pass_context
def documentation(ctx, input, output, template, git_commit, mode):
    """Genera documentación automáticamente con Aider u otra IA."""

    # Mostrar ayuda si se ejecuta sin parámetros adicionales
    if len(sys.argv) == 2:  # solo "iasuite documentation"
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe
    ensure_venv("docaider-env", "aider")

    # Construir el comando
    cmd = f"aider --input {input} --output {output} --mode {mode}"
    if template:
        cmd += f" --template {template}"
    if git_commit:
        cmd += " --git-commit"

    # Ejecutar dentro del entorno virtual
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
@click.pass_context
def docrefactoring(ctx, input, output, template, git_commit, mode):
    """Genera documentación refactorizada automáticamente con Aider u otra IA."""

    # Mostrar ayuda si se ejecuta sin parámetros adicionales
    if len(sys.argv) == 2:
        click.echo(ctx.get_help())
        return

    # Asegurarse de que el entorno virtual existe
    ensure_venv("docaider-env", "aider-refactor")

    # Construir el comando
    cmd = f"aider-refactor --input {input} --output {output} --mode {mode}"
    if template:
        cmd += f" --template {template}"
    if git_commit:
        cmd += " --git-commit"

    # Ejecutar dentro del entorno virtual
    run_in_venv("docaider-env", cmd)

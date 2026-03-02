# commands/programming.py
import click
from iasuite.utils.system import run_in_venv

# -----------------------
# Subcomando: programming
# -----------------------
@click.command()
@click.option('--input', '-i', default='.', help='Directorio raíz del código')
@click.option('--output', '-o', default='./doc', help='Directorio donde generar código o tests')
@click.option('--git-commit', is_flag=True, help='Hacer commit automático de cada fichero generado')
@click.option('--mode', default='incremental', help='Modo de generación: incremental o full')
def programming(input, output, git_commit, mode):
    """Asiste en programación, generación de tests o análisis de código."""
    cmd = f"devaider --input {input} --output {output} --mode {mode}"
    if git_commit:
        cmd += " --git-commit"
    
    run_in_venv("devaider-env", cmd)


# -----------------------
# Subcomando: devrefactoring
# -----------------------
@click.command()
@click.option('--input', '-i', default='.', help='Directorio raíz del código legacy')
@click.option('--output', '-o', default='./doc', help='Directorio donde generar código refactorizado')
@click.option('--git-commit', is_flag=True, help='Hacer commit automático de cada fichero generado')
@click.option('--mode', default='incremental', help='Modo de refactorización: incremental o full')
def devrefactoring(input, output, git_commit, mode):
    """Genera código refactorizado automáticamente."""
    cmd = f"devaider-refactor --input {input} --output {output} --mode {mode}"
    if git_commit:
        cmd += " --git-commit"
    
    run_in_venv("devaider-env", cmd)

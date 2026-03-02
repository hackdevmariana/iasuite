#!/usr/bin/env python3
import click
import os
import subprocess

# -----------------------
# Helper para ejecutar en un venv específico
# -----------------------
def run_in_venv(venv_name, command):
    """
    Ejecuta un comando dentro de un entorno virtual específico.
    """
    base_path = os.path.dirname(__file__)
    venv_path = os.path.join(base_path, "envs", venv_name)
    activate_script = os.path.join(venv_path, "bin", "activate")

    if not os.path.exists(activate_script):
        click.echo(f"[ERROR] No existe el entorno virtual: {venv_path}")
        return

    full_command = f"source {activate_script} && {command}"
    subprocess.run(full_command, shell=True, executable="/bin/bash")

def detect_gpu():
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


# -----------------------
# CLI principal
# -----------------------
@click.group()
def cli():
    """iasuite - Suite de herramientas IA para desarrollo y creación de contenido."""
    pass

# -----------------------
# Subcomando: setup
# -----------------------
@cli.command()
def setup():
    """Crea todos los entornos virtuales necesarios e instala dependencias."""
    import sys
    
    MIN_VERSION = (3, 10)

    if sys.version_info < MIN_VERSION:
        click.echo("❌ Python 3.10+ is required.")
        sys.exit(1)

    click.echo(f"✔ Python version: {sys.version.split()[0]}")

    if detect_gpu():
        click.echo("🚀 NVIDIA GPU detected.")
    else:
        click.echo("⚠ No NVIDIA GPU detected. Image/video generation may be slow.")

    base_path = os.path.dirname(os.path.dirname(__file__))
    envs_path = os.path.join(base_path, "envs")

    os.makedirs(envs_path, exist_ok=True)

    environments = {
        "docaider-env": ["click", "aider", "ollama"],
        "devaider-env": ["click"],
        "makeimages-env": ["click"],
        "makevideos-env": ["click"],
        "createcontents-env": ["click", "ollama"],
    }

    for env_name, packages in environments.items():
        env_path = os.path.join(envs_path, env_name)

        if not os.path.exists(env_path):
            click.echo(f"[+] Creating virtual environment: {env_name}")
            subprocess.run([sys.executable, "-m", "venv", env_path])
        else:
            click.echo(f"[=] Environment already exists: {env_name}")

        pip_path = os.path.join(env_path, "bin", "pip")

        click.echo(f"[+] Installing packages in {env_name}...")
        subprocess.run([pip_path, "install", "--upgrade", "pip"])
        subprocess.run([pip_path, "install"] + packages)

    click.echo("\n✅ Setup completed successfully.")

# -----------------------
# Subcomando: documentation
# -----------------------
@cli.command()
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
@cli.command()
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

# -----------------------
# Subcomando: programming
# -----------------------
@cli.command()
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
@cli.command()
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

# -----------------------
# Subcomando: images
# -----------------------
@cli.command()
@click.option('--output', '-o', default='./images', help='Directorio donde guardar imágenes generadas.')
def images(output):
    """Genera imágenes con IA según parámetros y personajes."""
    cmd = f"makeimages --output {output}"
    run_in_venv("makeimages-env", cmd)

# -----------------------
# Subcomando: videos
# -----------------------
@cli.command()
@click.option('--output', '-o', default='./videos', help='Directorio donde guardar vídeos generados.')
def videos(output):
    """Genera vídeos con IA (avatares, lip-sync, etc.)."""
    cmd = f"makevideos --output {output}"
    run_in_venv("makevideos-env", cmd)

# -----------------------
# Subcomando: content
# -----------------------
@cli.command()
@click.option('--profile', '-p', default=None, help='Perfil de influencer para generar contenido.')
def content(profile):
    """Genera contenido textual para influencers IA."""
    cmd = f"createcontents --profile {profile or ''}"
    run_in_venv("createcontents-env", cmd)

# -----------------------
# Subcomando: characters
# -----------------------
@cli.command()
@click.option('--name', '-n', default=None, help='Nombre del personaje IA a crear.')
def characters(name):
    """Crea un personaje IA consistente con personalidad, intereses y voz."""
    cmd = f"createcharacter --name {name or ''}"
    run_in_venv("createcontents-env", cmd)

# -----------------------
# Subcomando: lora
# -----------------------
@cli.command()
@click.option('--character', '-c', default=None, help='Personaje IA para entrenar LoRA.')
def lora(character):
    """Genera LoRA para un personaje IA específico."""
    cmd = f"createlora --character {character or ''}"
    run_in_venv("createcontents-env", cmd)

# -----------------------
if __name__ == "__main__":
    cli()

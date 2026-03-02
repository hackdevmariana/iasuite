import click
import os
import subprocess
import sys

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.system import detect_gpu, detect_ollama

@click.command()
def setup():
    """Crea todos los entornos virtuales necesarios e instala dependencias."""
    MIN_VERSION = (3, 10)
    if sys.version_info < MIN_VERSION:
        click.echo("❌ Python 3.10+ is required.")
        sys.exit(1)

    click.echo(f"✔ Python version: {sys.version.split()[0]}")
    click.echo("🚀 NVIDIA GPU detected." if detect_gpu() else "⚠ No NVIDIA GPU detected. Generation may be slow.")
    click.echo("✔ Ollama detected." if detect_ollama() else "⚠ Ollama not found. Install from https://ollama.com")

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

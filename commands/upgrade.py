# commands/upgrade.py
import click
import subprocess

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.system import run_in_venv

@click.command()
def upgrade():
    """Actualiza iasuite y todos los entornos virtuales a la última versión."""
    click.echo("=== iasuite upgrade ===")

    # 1️⃣ Actualizar repositorio principal (asumiendo Git)
    click.echo("[+] Updating iasuite repository...")
    try:
        subprocess.run(["git", "pull", "--rebase"], check=True)
        click.echo("✔ Repository updated")
    except subprocess.CalledProcessError:
        click.echo("⚠ Failed to update repository via git")

    # 2️⃣ Actualizar entornos virtuales
    envs = [
        "docaider-env",
        "devaider-env",
        "makeimages-env",
        "makevideos-env",
        "createcontents-env",
    ]

    for env in envs:
        click.echo(f"[+] Upgrading packages in {env}...")
        # run_in_venv se ejecuta en bash, así que podemos usar pip list --outdated y pip install -U
        cmd = "pip install --upgrade pip && pip list --outdated --format=freeze | cut -d = -f 1 | xargs -n1 pip install -U"
        run_in_venv(env, cmd)

    click.echo("\n✅ Upgrade completed successfully.")

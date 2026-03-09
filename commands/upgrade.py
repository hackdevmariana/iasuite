# commands/upgrade.py
import click
from utils.system import run_in_venv
import sys
import os
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

@click.command()
def upgrade():
    """Actualiza iasuite y todos los entornos virtuales a la última versión."""
    click.echo("=== iasuite upgrade ===")

    # 1️⃣ Actualizar repositorio principal
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
        # Comando compatible pip >= 21
        cmd = (
            "pip install --upgrade pip && "
            "pip list --outdated --format=columns | tail -n +3 | awk '{print $1}' | xargs -r pip install -U"
        )
        run_in_venv(env, cmd)

    click.echo("\n✅ Upgrade completed successfully.")

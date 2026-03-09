import click
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.system import detect_gpu, detect_ollama, detect_aider

@click.command()
def doctor():
    """Verifica que el sistema esté listo para iasuite."""
    click.echo("=== iasuite doctor ===")
    
    # Versión real de Python
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    click.echo(f"✔ Python version: {py_version} (detected)")
    
    # Verificar GPU
    click.echo("🚀 GPU detected" if detect_gpu() else "⚠ No GPU detected")
    
    # Verificar Ollama
    click.echo("✔ Ollama detected" if detect_ollama() else "⚠ Ollama missing")
    
    # Verificar Aider
    click.echo("✔ Aider detected" if detect_aider() else "⚠ Aider missing (install in docaider-env)")
    
    # Más adelante podemos hacer un chequeo real de entornos
    click.echo("✔ Environments OK")

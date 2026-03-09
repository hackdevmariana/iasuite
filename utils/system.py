import subprocess
import os
import sys

def run_in_venv(venv_name, command):
    """
    Ejecuta un comando dentro de un entorno virtual específico.
    """
    current_file = os.path.abspath(__file__)
    iasuite_root = os.path.dirname(os.path.dirname(current_file))
    envs_root = os.path.join(iasuite_root, "envs")
    venv_path = os.path.join(envs_root, venv_name)
    bin_path = os.path.join(venv_path, "bin")

    # Intentamos localizar el ejecutable absoluto
    cmd_name = command.split()[0]
    cmd_rest = " ".join(command.split()[1:])
    cmd_path = os.path.join(bin_path, cmd_name)

    if not os.path.exists(cmd_path):
        raise FileNotFoundError(f"{cmd_name} no encontrado en {bin_path}")

    full_command = f"{cmd_path} {cmd_rest}"
    subprocess.run(full_command, shell=True, executable="/bin/bash")

def detect_gpu():
    """
    Detecta si el sistema tiene una GPU NVIDIA.
    """
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False

def detect_ollama():
    """
    Detecta si Ollama está instalado en el PATH del sistema.
    """
    try:
        result = subprocess.run(
            ["ollama", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False

def detect_aider(venv_name="docaider-env"):
    """
    Comprueba si Aider está instalado en el entorno virtual dado.
    """
    current_file = os.path.abspath(__file__)
    iasuite_root = os.path.dirname(os.path.dirname(current_file))
    venv_path = os.path.join(iasuite_root, "envs", venv_name)
    aider_path = os.path.join(venv_path, "bin", "aider")

    return os.path.exists(aider_path)

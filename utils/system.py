import subprocess
import os

def run_in_venv(venv_path, command):
    activate_script = os.path.join(venv_path, "bin", "activate")
    full_command = f"source {activate_script} && {command}"
    subprocess.run(full_command, shell=True, executable="/bin/bash")

def detect_gpu():
    try:
        result = subprocess.run(["nvidia-smi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def detect_ollama():
    try:
        result = subprocess.run(["ollama", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except FileNotFoundError:
        return False

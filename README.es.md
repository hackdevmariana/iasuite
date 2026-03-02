# iasuite

**Command-line interface para generar código, documentación, contenido, imágenes y vídeos usando IA.**

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/myuser/iasuite.git
cd iasuite
```

2. Crear los entornos virtuales para cada subcomando:

```bash
# Documentación
python3 -m venv envs/docaider-env
source envs/docaider-env/bin/activate
pip install click aider ollama

# Programación
python3 -m venv envs/devaider-env
source envs/devaider-env/bin/activate
pip install click devaider

# Imágenes
python3 -m venv envs/makeimages-env
source envs/makeimages-env/bin/activate
pip install click stable-diffusion

# Vídeos
python3 -m venv envs/makevideos-env
source envs/makevideos-env/bin/activate
pip install click video-generator

# Contenidos / personajes / LoRA
python3 -m venv envs/createcontents-env
source envs/createcontents-env/bin/activate
pip install click ollama
```

> Puedes ajustar los paquetes según las necesidades de cada subcomando.

3. Crear un alias o script en tu PATH para lanzar iasuite fácilmente:

Por, ejemplo, en ~/.local/bin/iasuite:

```bash
#!/usr/bin/env bash
python3 /ruta/a/iasuite/iasuite/cli.py "$@"
chmod +x ~/.local/bin/iasuite
```

## Uso

```bash
iasuite --help
```

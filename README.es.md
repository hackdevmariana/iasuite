# iasuite

**Command-line interface para generar código, documentación, contenido, imágenes y vídeos usando IA.**

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/hackdevmariana/iasuite.git
cd iasuite
```

2. a) Crear los entornos virtuales para cada subcomando:

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

2. b) Puedes usar el comando `iasuite setup` para crear automáticamente todos los entornos y paquetes necesarios.

```sh 
iasuite setup
```

3. a) Crear un alias o script en tu PATH para lanzar iasuite fácilmente:

Por, ejemplo, en ~/.local/bin/iasuite:

```bash
#!/usr/bin/env bash
python3 /ruta/a/iasuite/iasuite/cli.py "$@"
chmod +x ~/.local/bin/iasuite
```

3. b) Agregar un alias en tu `.bashrc` o `.zshrc`:

```bash
alias iasuite="python3 /ruta/a/iasuite/iasuite/cli.py"
```

## Uso

```bash
iasuite --help
```

Subcomandos disponibles:

- `setup` → Crea automáticamente todos los entornos virtuales necesarios.
- `documentation` → Genera documentación automáticamente.
- `docrefactoring` → Refactoriza documentación existente.
- `programming` → Asiste en programación, tests, análisis de código.
- `devrefactoring` → Refactoriza código legacy.
- `images` → Genera imágenes con IA.
- `videos` → Genera vídeos con IA.
- `content` → Genera contenido para perfiles.
- `characters` → Crea personajes IA consistentes.
- `lora` → Genera LoRA para personajes IA.

Cada subcomando tiene su propio entorno virtual y se ejecuta automáticamente dentro de él.

## Ejemplos prácticos

```bash
iasuite documentation -i ./mi_proyecto -o ./docs
iasuite programming -i ./mi_proyecto -o ./tests --mode full
iasuite images -o ./assets/images
```

## Visión

`iasuite` ayuda a automatizar tareas repetitivas en desarrollo:

- Documentación automática
- Refactorización de código y docs
- Generación de tests consistentes
- Transformar proyectos desordenados en sistemas estructurados

## Contribuir

Clona el repositorio.

Crea tus entornos virtuales.

Añade nuevas funcionalidades o mejoras en subcomandos.

Abre pull requests para revisión.

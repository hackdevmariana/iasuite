# iasuite

**Command-line interface for generating code, documentation, content, images, and videos using AI models such as Ollama and Stable Diffusion.**

`iasuite` is designed to automate what developers usually avoid:

- Documentation in messy projects

- Refactoring legacy codebases

- Generating consistent tests

- Structuring chaotic software into clean architecture

Each subcommand runs in its own isolated virtual environment to avoid dependency conflicts.

## Installation

1. Clone the repository

```bash
git clone https://github.com/hackdevmariana/iasuite.git
cd iasuite
```

2. Create virtual environments for each subcommand:

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

> Adjust installed packages depending on your AI stack and tools.

3. Add iasuite to your PATH

For example, create: 

`~/.local/bin/iasuite`:

```bash
#!/usr/bin/env bash
python3 /ruta/a/iasuite/iasuite/cli.py "$@"
```

Then:

```bash
chmod +x ~/.local/bin/iasuite
```

Make sure ~/.local/bin is in your PATH.

## Usage

```bash
iasuite --help
```

Available commands:

- `documentation` → Generate automatic project documentation

- `docrefactoring` → Refactor legacy documentation

- `programming` → Assist with code generation, analysis, and tests

- `devrefactoring` → Refactor legacy code

- `images` → Generate AI images

- `videos` → Generate AI videos

- `content` → Generate AI influencer content

- `characters` → Create consistent AI characters

- `lora` → Generate LoRA models for characters

Each command automatically runs inside its dedicated virtual environment.

## Vision

`iasuite` aims to solve a real problem in software development:

> Most projects work — but are chaotic, undocumented, inconsistent, and fragile.

`iasuite` enables:

1. Automatic documentation extraction

2. Documentation refactoring into structured architecture (DDD-style)

3. Clean re-generation of consistent, test-covered codebases

> From Frankenstein projects → to structured systems.

## Contributing

Fork the repository

Create feature branches

Improve subcommands

Open pull requests

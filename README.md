insight-ai-api

Setup instructions
- See Makefile command table below

| Command                     | Purpose                        | Dependencies        |
|-----------------------------|--------------------------------|---------------------|
| `make venv`                 | Create/update venv             |                     |
| `make requirements.txt`     | PRD dependencies               | requirements.in     |
| `make dev-requirements.txt` | DEV dependencies               | dev-requirements.in |
| `make clean`                | remove venv and compiled files |                     |
| `make compile && make sync` | Pull in latest packages        |                     |


Python environment
- Pyenv (.python-version)
  - `pyenv local 3.11.4`

- Virtualenv (venv/)
  - `pip install pip-tools`

Dependency management with pip-tools
- `pip-compile requirements.in` will generate a requirments.txt file with all the dependencies in requirements.in
  - `pip-compile dev-requirements.in` will generate a dev-requirments.txt file with dependencies in dev-requirements.in
- `pip-sync requirements.txt` will install all the package listed in the requirments.txt file
  - `pip-sync dev-requirements.txt` will install all the package listed in the dev-requirments.txt file

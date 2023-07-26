# insight-ai-api

## About
This is a simplistic FastAPI app that uses AI features to enhance api service.

Set Python version using pyenv

`pyenv local 3.11.4`
- writes to `.python-version`

### Create virtualenv

From repository root:
1. `python -m venv .venv`
2. `pip install pip-tools`
3. `make venv`

### Dependency management

#### pip-tools

- `pip-compile requirements.in` will generate a requirments.txt file with all the dependencies in requirements.in
  - `pip-compile dev-requirements.in` will generate a dev-requirments.txt file with dependencies in dev-requirements.in
- `pip-sync requirements.txt` will install all the package listed in the requirments.txt file
  - `pip-sync dev-requirements.txt` will install all the package listed in the dev-requirments.txt file

#### Makefile

See Makefile command table below

| Command                     | Purpose                        | Dependencies        |
|-----------------------------|--------------------------------|---------------------|
| `make requirements.txt`     | PRD dependencies               | requirements.in     |
| `make dev-requirements.txt` | DEV dependencies               | dev-requirements.in |
| `make venv`                 | Update .venv/                  | .venv/              |
| `make clean`                | remove venv and compiled files |                     |
| `make compile && make sync` | Pull in latest packages        |                     |

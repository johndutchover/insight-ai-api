# insight-ai-api

[![pipeline status](https://gitlab.com/johndutchover/insight-ai-api/badges/main/pipeline.svg)](https://gitlab.com/johndutchover/insight-ai-api/-/commits/main)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Latest Release](https://gitlab.com/johndutchover/insight-ai-api/-/badges/release.svg)](https://gitlab.com/johndutchover/insight-ai-api/-/releases)

## About
This is a simplistic FastAPI app that uses AI features to enhance api service.

Focus areas:
- [FastAPI](https://github.com/tiangolo/fastapi)
- Pydantic
  - Data validation
- [Marvin](https://github.com/prefecthq/marvin)
  - AI engineering framework
- Pytest
- [pre-commit](https://github.com/pre-commit/pre-commit)
  - pre-commit hooks
- GitLab
  - for career reasons

Set Python version using pyenv

`pyenv local 3.11.4`
- writes to `.python-version`

### Create virtualenv

From repository root:
1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install pip-tools`
4. `pip install --upgrade pip`
5. `make venv`

### Dependency management

#### pip-tools

- `pip-compile requirements.in` will generate a requirments.txt file with all the dependencies in requirements.in
  - `pip-compile dev-requirements.in` will generate a dev-requirments.txt file with dependencies in dev-requirements.in
- `pip-sync requirements.txt` will install all the package listed in the requirments.txt file
  - `pip-sync dev-requirements.txt` will install all the package listed in the dev-requirments.txt file

#### Makefile

See Makefile command table below

| Make command                    | Purpose                                                                                 |
|---------------------------------|-----------------------------------------------------------------------------------------|
| `make venv`                     | Target to create and activate the virtual environment                                   |
| `make clean`                    | Destructive. Used to remove .venv/                                                      |
| `make deploy`                   | Deploy app to fly.io                                                                    |
| `make .venv/bin/activate`       | Create a Python virtual environment and install required packages"                      |
| `make requirements.txt`         | Generate "requirements.txt" by compiling "requirements.in"                              |
| `make dev-requirements.txt`     | Generate "dev-requirements.txt" by compiling "dev-requirements.in"                      |
| `make compile-requirements`     | Regenerate "requirements.txt" using "pip-compile"                                       |
| `make compile-dev-requirements` | Regenerate "dev-requirements.txt" using "pip-compile"                                   |
| `make compile`                  | Regenerate both "requirements.txt" and "dev-requirements.txt"                           |
| `make sync`                     | Sync virtual environment with "requirements.txt" and "dev-requirements.txt"             |
| `make update`                   | Regenerate .in and .txt files and sync virtual environment with the latest dependencies |

### GitLab CI

#### Settings

##### CI/CD

##### Variables

- MARVIN_OPENAI_API_KEY
  - attributes: masked, expanded
- FLY_API_TOKEN
    - attributes: masked, expanded

#### .gitlab-ci.yml
- stages
  - install
  - test
  - code_quality
  - deploy
    - uses `flyctl`

#### .pre-commit-config.yaml
- pre-commit-hooks
- black
  - `pyproject.toml`
- flake8
- bandit
  - excludes B104 check

##### .flake8
- configuration for flake8

### Fly
- app/fly.toml

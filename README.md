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

### Initialize virtualenv

From repository root:

1. `make venv`
2. `source .venv/bin/activate`

### Dependency management

#### Makefile

Makefile command table

| Make command                    | Purpose                                                                     |
|---------------------------------|-----------------------------------------------------------------------------|
| `make venv`                     | Target to create and activate the backend virtual environment               |
| `make fe-venv`                  | Target to create and activate the frontend virtual environment              |
| `make clean`                    | Remove Python file artifacts and the virtual environment                    |
| `make deploy`                   | Deploy app using flyctl                                                     |
| `make app/requirements.txt`     | Generate "app/requirements.txt" by compiling "requirements.in"              |
| `make app/dev-requirements.txt` | Generate "app/dev-requirements.txt" by compiling "dev-requirements.in"      |
| `make compile-requirements`     | Regenerate "app/requirements.txt" using "pip-compile"                       |
| `make compile-dev-requirements` | Regenerate "app/dev-requirements.txt" using "pip-compile"                   |
| `make compile`                  | Regenerate both "app/requirements.txt" and "app/dev-requirements.txt"       |
| `make sync`                     | Synchronize the virtual environment with the packages listed                |
| `make update`                   | Update both files and sync the virtual environment with latest dependencies |

### GitLab CI

#### Settings

##### CI/CD

##### Variables

- MARVIN_OPENAI_API_KEY
    - attributes: masked, expanded
- FLY_API_TOKEN
    - attributes: masked, expanded
- GITLAB_ACCESS_TOKEN_MEGALINTER
  - attributes: masked

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
  - `.flake8`
- bandit
  - excludes B104 check
- local
  - commit-msg
- checkmake
  - configured in `.gitlab-ci.yml`
  - run by MegaLinter

### Fly

- app/fly.toml

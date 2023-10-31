# insight-ai-api

[![MegaLinter](https://github.com/johndutchover/insight-ai-api/actions/workflows/mega-linter.yml/badge.svg)](https://github.com/johndutchover/insight-ai-api/actions/workflows/mega-linter.yml)

## About

This is a simplistic FastAPI app that uses AI features to enhance api service.

### Focus areas

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

`pyenv local 3.11.6`

- writes to `.python-version`

### Initialize virtualenv

From repository root:

1. `make venv`
2. `source .venv/bin/activate`

### Dependency management

#### Makefile

Makefile command table

| Command                         | Purpose                                                                            |
|---------------------------------|------------------------------------------------------------------------------------|
| `make venv`                     | Target to create and activate the app virtual environment                          |
| `make venv-fe`                  | Target to create and activate the frontend virtual environment                     |
| `make app/requirements`         | Generate "app/requirements.txt" by compiling "requirements.in"                     |
| `make app/requirements_dev`     | Generate "app/requirements_dev.txt" by compiling "requirements-dev.in"             |
| `make app-requirements`         | Generate "app/requirements.txt" and "app/requirements_dev.txt"                     |
| `make frontend-requirements`    | Generate "frontend/requirements_fe.txt" by compiling "requirements-fe.in"          |
| `make cli-requirements`         | Generate "cli/requirements_fe.txt" by compiling "requirements-cli.in"              |
| `make compile-requirements`     | Regenerate both "app/requirements.txt" and "app/requirements_dev.txt"              |
| `make compile-requirements-dev` | Regenerate "app/requirements_dev.txt" using "pip-compile"                          |
| `make deploy-api`               | Deploy app (api) using flyctl                                                      |
| `make deploy-fe`                | Deploy frontend using flyctl                                                       |
| `make sync-requirements-app`    | Synchronize .venv/ with the packages in requirements.txt  and requirements_dev.txt |
| `make sync-requirements-cli`    | Synchronize cli/venv-cli/ with the packages in requirements_cli.txt                |
| `make sync-requirements-fe`     | Synchronize frontend/venv-fe/ with the packages in requirements_frontend.txt       |

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

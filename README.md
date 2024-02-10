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

`pyenv local 3.11.7`

- writes to `.python-version`

### Initialize for development

From repository root:

1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `python -m pip install -Ur local.in`

### Dependency management

#### Makefile

Makefile command table

| Command            | Purpose                                  |
|--------------------|------------------------------------------|
| `make init`        | Initialize Python environment            |
| `make update`      | Update and Initialize Python environment |
| `make update-deps` | Update Python dependencies               |

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

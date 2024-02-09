update-deps:
	pre-commit autoupdate
	python -m pip install --upgrade pip-tools pip wheel
	python -m piptools compile --upgrade -o requirements/requirements.txt pyproject.toml
	python -m piptools compile --extra dev --upgrade -o requirements/requirements-dev.txt pyproject.toml


init:
	rm -rf .tox
	python -m pip install --upgrade pip wheel
	python -m pip install --upgrade -r requirements/requirements.txt -r requirements/requirements-dev.txt -e .
	python -m pip check

update: update-deps init

.PHONY: update-deps init update all clean test

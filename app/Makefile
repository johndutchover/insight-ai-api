update-deps:
	pre-commit autoupdate
	python -m pip install --upgrade pip-tools pip wheel
	python -m piptools compile --upgrade -o requirements/requirements.txt requirements/requirements.in
	python -m piptools compile --upgrade -o requirements/requirements-dev.txt requirements/requirements-dev.in
	python -m pip install --upgrade --requirement=requirements/requirements.txt
	python -m pip install --upgrade --requirement=requirements/requirements-dev.txt

init:
	rm -rf .tox
	python -m pip install --upgrade pip wheel
	python -m pip install --upgrade -r requirements/requirements.txt -e .
	@python -m piptools compile -o requirements/requirements-dev.txt requirements/requirements-dev.in
	@if [ -e requirements/requirements-dev.txt ]; then \
		python -m pip install --upgrade --requirement=requirements/requirements-dev.txt; \
	fi
	python -m pip check

update: update-deps init

.PHONY: update-deps init update all clean test

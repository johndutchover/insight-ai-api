update-deps:
	uv pip install --upgrade pip-tools pip wheel
	uv pip compile --upgrade -o requirements/requirements.txt requirements/requirements.in
	uv pip compile --upgrade -o requirements/requirements-dev.txt requirements/requirements-dev.in
	uv pip install --upgrade --requirement=requirements/requirements.txt
	uv pip install --upgrade --requirement=requirements/requirements-dev.txt

update-precommit:
	pre-commit autoupdate

init:
	rm -rf .tox
	uv pip install --upgrade pip wheel
	uv pip install --upgrade -r requirements/requirements.txt -e .
	@uv pip compile -o requirements/requirements-dev.txt requirements/requirements-dev.in
	@if [ -e requirements/requirements-dev.txt ]; then \
		uv pip install --upgrade --requirement=requirements/requirements-dev.txt; \
	fi
	python -m pip check

update: update-deps init

.PHONY: update-deps init update all clean test update-precommit

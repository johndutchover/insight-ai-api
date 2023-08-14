.PHONY: clean venv update deploy compile-requirements compile-dev-requirements compile sync all test

# Target to create and activate the virtual environment.
venv: app/requirements.txt app/dev-requirements.txt
	test -d .venv || python3.11 -m venv .venv
	. .venv/bin/activate; pip install -U pip setuptools wheel
	. .venv/bin/activate; pip install -r app/requirements.txt; pip install -r app/dev-requirements.txt
	touch .venv/bin/activate

# Target to create and activate the virtual environment.
fe-venv: frontend/fe-requirements.txt
	test -d frontend/venv-fe || python3.11 -m venv frontend/venv-fe
	. frontend/venv-fe/bin/activate; pip install -U pip setuptools wheel
	. frontend/venv-fe/bin/activate; pip install -r frontend/fe-requirements.txt
	touch frontend/venv-fe/bin/activate

# Remove Python file artifacts and the virtual environment.
clean:
	rm -rf .venv
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# Deploy API using flyctl.
deploy-api:
	flyctl deploy --ha=false --config app/fly.toml

# Deploy frontend using flyctl.
deploy-fe:
	flyctl deploy --ha=false --config frontend/fly.toml

# Regenerate "app/requirements.txt" using "pip-compile".
app/requirements.txt: requirements.in
	pip-compile requirements.in -o app/requirements.txt

# Regenerate "app/dev-requirements.txt" using "pip-compile".
app/dev-requirements.txt: dev-requirements.in
	pip-compile dev-requirements.in -o app/dev-requirements.txt

# Regenerate both "app/requirements.txt" and "app/dev-requirements.txt".
compile: app/requirements.txt app/dev-requirements.txt

# Synchronize the virtual environment with the packages listed.
sync:
	@pip-sync app/requirements.txt app/dev-requirements.txt

# Update both files and sync the virtual environment with latest dependencies.
update: compile sync

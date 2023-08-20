.PHONY: clean venv update deploy compile-requirements compile-dev-requirements compile sync all test

# Target to create and activate the virtual environment.
venv: app/requirements.txt app/requirements_dev.txt
	test -d .venv || python3.11 -m venv .venv
	. .venv/bin/activate; pip install -U pip setuptools wheel
	. .venv/bin/activate; pip install -r app/requirements.txt; pip install -r app/requirements_dev.txt
	touch .venv/bin/activate

# Target to create and activate the virtual environment.
fe-venv: frontend/requirements_frontend.txt
	test -d frontend/venv-fe || python3.11 -m venv frontend/venv-fe
	. frontend/venv-fe/bin/activate; pip install -U pip setuptools wheel
	. frontend/venv-fe/bin/activate; pip install -r frontend/requirements_frontend.txt
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

# Regenerate "app/requirements_dev.txt" using "pip-compile".
app/requirements_dev.txt: requirements-dev.in
	pip-compile requirements-dev.in -o app/requirements_dev.txt

app-requirements: app/requirements.txt app/requirements_dev.txt

# Regenerate "frontend/fe-requirements" using "pip-compile"
frontend-requirements: requirements-frontend.in
	pip-compile requirements-frontend.in -o frontend/requirements_frontend.txt

# Regenerate "cli/cli-requirements" using "pip-compile"
cli-requirements: requirements-cli.in
	pip-compile requirements-cli.in -o cli/requirements_cli.txt

compile-requirements: cli-requirements frontend-requirements app/requirements.txt app/requirements_dev.txt

# Synchronize the virtual environment with the packages listed.
sync-app-requirements:
	@pip-sync app/requirements.txt app/requirements_dev.txt

sync-fe-requirements:
	@pip-sync frontend/requirements_frontend.txt

sync-cli-requirements:
	@pip-sync cli/requirements_cli.txt

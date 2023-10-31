.PHONY: clean venv venv-fe update deploy compile-requirements compile-dev-requirements compile sync all test

# Target to create and activate the virtual environment.
venv: app/requirements.txt app/requirements_dev.txt
	test -d .venv || python3.11 -m venv .venv
	. .venv/bin/activate; pip install -U pip setuptools wheel
	. .venv/bin/activate; pip install -r app/requirements.txt; pip install -r app/requirements_dev.txt
	touch .venv/bin/activate

# Target to create and activate the virtual environment.
venv-fe: frontend/requirements_frontend.txt
	test -d frontend/venv-fe || python3.11 -m venv frontend/venv-fe
	. frontend/venv-fe/bin/activate; pip install -U pip setuptools wheel
	. frontend/venv-fe/bin/activate; pip install -r frontend/requirements_frontend.txt
	touch frontend/venv-fe/bin/activate

# Regenerate "app/requirements.txt" using "pip-compile --strip-extras".
app/requirements: requirements.in
	pip-compile --strip-extras requirements.in -o app/requirements.txt

# Regenerate "app/requirements_dev.txt" using "pip-compile --strip-extras".
app/requirements_dev: requirements-dev.in
	pip-compile --strip-extras requirements-dev.in -o app/requirements_dev.txt

app-requirements: app/requirements.txt app/requirements_dev.txt

# Regenerate "frontend/fe-requirements" using "pip-compile --strip-extras"
frontend-requirements: requirements-frontend.in
	pip-compile --strip-extras requirements-frontend.in -o frontend/requirements_frontend.txt

# Regenerate "cli/cli-requirements" using "pip-compile --strip-extras"
cli-requirements: requirements-cli.in
	pip-compile --strip-extras requirements-cli.in -o cli/requirements_cli.txt

compile-requirements: app/requirements.txt app/requirements_dev.txt
compile-requirements-dev: app/requirements_dev.txt

# Deploy API using flyctl.
deploy-api:
	flyctl deploy --ha=false --config app/fly.toml

# Deploy frontend using flyctl.
deploy-fe:
	flyctl deploy --ha=false --config frontend/fly.toml

# Synchronize the virtual environment with the packages listed.
sync-requirements-app:
	@pip-sync app/requirements.txt app/requirements_dev.txt

sync-requirements-cli:
	@pip-sync cli/requirements_cli.txt

sync-requirements-fe:
	@pip-sync frontend/requirements_frontend.txt

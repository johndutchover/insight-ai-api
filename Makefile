.PHONY: clean venv update deploy compile-requirements compile-dev-requirements compile sync

# Target to create and activate the virtual environment.
venv: app/requirements.txt app/dev-requirements.txt
	test -d .venv || python -m venv .venv
	. .venv/bin/activate; pip install -U pip setuptools wheel
	. .venv/bin/activate; pip install -r app/requirements.txt; pip install -r app/dev-requirements.txt
	touch .venv/bin/activate

# Remove Python file artifacts and the virtual environment.
clean:
	rm -rf .venv
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# Deploy using flyctl.
deploy:
	flyctl deploy --ha=false --config app/fly.toml

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

.PHONY: clean .venv update

# venv: Target to create and activate the virtual environment.
venv: .venv/bin/activate

# clean: Remove the virtual environment directory ".venv" and its contents.
clean:
	rm -rf .venv

# .venv/bin/activate: Create a Python virtual environment and install required packages from "app/requirements.txt" and "app/dev-requirements.txt".
.venv/bin/activate: app/requirements.txt app/dev-requirements.txt
	test -d .venv || python3 -m venv .venv
	. .venv/bin/activate; pip install -U pip setuptools wheel
	. .venv/bin/activate; pip install -r app/dev-requirements.txt; pip install -r app/requirements.txt
	touch .venv/bin/activate

# dev-requirements.txt: Generate "app/dev-requirements.txt" by compiling "app/dev-requirements.in".
app/dev-requirements.txt: app/dev-requirements.in
	pip-compile app/dev-requirements.in

# requirements.txt: Generate "app/requirements.txt" by compiling "app/requirements.in".
app/requirements.txt: app/requirements.in
	pip-compile app/requirements.in

# compile-requirements: Regenerate "app/requirements.txt" using "pip-compile".
compile-requirements: app/requirements.txt

# compile-dev-requirements: Regenerate "app/dev-requirements.txt" using "pip-compile".
compile-dev-requirements: app/dev-requirements.txt

# compile: Regenerate both "app/requirements.txt" and "app/dev-requirements.txt".
compile: compile-requirements compile-dev-requirements

# sync: Synchronize the virtual environment with the packages listed in "app/requirements.txt" and "app/dev-requirements.txt".
sync:
	@pip-sync app/requirements.txt app/dev-requirements.txt

# update: Regenerate both files and sync the virtual environment with the latest dependencies.
update: compile sync

.PHONY: clean .venv update

# venv: Target to create and activate the virtual environment.
venv: .venv/bin/activate

# clean: Remove the virtual environment directory ".venv" and its contents.
clean:
	rm -rf .venv

# .venv/bin/activate: Create a Python virtual environment and install required packages from "requirements.txt" and "dev-requirements.txt".
.venv/bin/activate: requirements.txt dev-requirements.txt
	test -d .venv || python -m venv .venv
	. .venv/bin/activate; pip install -U pip setuptools wheel
	. .venv/bin/activate; pip install -r dev-requirements.txt; pip install -r requirements.txt
	touch .venv/bin/activate

# dev-requirements.txt: Generate "dev-requirements.txt" by compiling "dev-requirements.in".
dev-requirements.txt: dev-requirements.in
	pip-compile dev-requirements.in

# requirements.txt: Generate "requirements.txt" by compiling "requirements.in".
requirements.txt: requirements.in
	pip-compile requirements.in

# compile-requirements: Regenerate "requirements.txt" using "pip-compile".
compile-requirements: requirements.txt

# compile-dev-requirements: Regenerate "dev-requirements.txt" using "pip-compile".
compile-dev-requirements: dev-requirements.txt

# compile: Regenerate both "requirements.txt" and "dev-requirements.txt".
compile: compile-requirements compile-dev-requirements

# sync: Synchronize the virtual environment with the packages listed in "requirements.txt" and "dev-requirements.txt".
sync:
	@pip-sync requirements.txt dev-requirements.txt

# update: Regenerate both files and sync the virtual environment with the latest dependencies.
update: compile sync

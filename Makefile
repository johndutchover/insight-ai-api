.PHONY: clean .venv

venv: .venv/bin/activate

clean:
	rm -rf .venv

.venv/bin/activate: requirements.txt dev-requirements.txt
	test -d .venv || python3 -m venv .venv
	. .venv/bin/activate; pip install -r dev-requirements.txt; pip install -r requirements.txt
	touch .venv/bin/activate

dev-requirements.txt: dev-requirements.in
	pip-compile dev-requirements.in

requirements.txt: requirements.in
	pip-compile requirements.in

compile:
	@rm -f requirements*.txt
	@pip-compile requirements.in
	@pip-compile dev-requirements.in

sync:
	@pip-sync requirements*.txt

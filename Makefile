# tells make that clean and venv are not files
.PHONY: clean venv

venv: venv/bin/activate

venv/bin/activate: requirements.txt dev-requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -r dev-requirements.txt; pip install -r requirements.txt
	touch venv/bin/activate

dev-requirements.txt: dev-requirements.in
	pip-compile dev-requirements.in

requirements.txt: requirements.in
	pip-compile requirements.in

clean:
	rm -rf venv
	find -iname "*.pyc" -delete


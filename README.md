insight-ai-api

Setup

Python environment
- Virtualenv
  - Python 3.11.4
  - `pip install pip-tools`

Dependencies
- dev-requirements.in
- requirements.in

Requirements

pip-tools
- `pip-compile requirements.in` will generate a requirments.txt file with all the dependencies in requirements.in
  - `pip-compile dev-requirements.in` will generate a dev-requirments.txt file with dependencies in dev-requirements.in
- `pip-sync requirements.txt` will install all the package listed in the requirments.txt file
  - `pip-sync dev-requirements.txt` will install all the package listed in the dev-requirments.txt file

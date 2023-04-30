SHELL := /bin/bash
coverage:
	python3 test.py
	python -m coverage run -m unittest
	python -m coverage report -m

site:
	export PYTHONPATH="$PYTHONPATH:/home/baadalvm/.local/lib/python3.10/site-packages"
	export PYTHONPATH="$PYTHONPATH:/usr/lib/python3/dist-packages"
	source env/bin/activate && python3 app.py

create_env:
	source env/bin/activate

install:
	pip install -r requirements.txt
coverage:
	python3 test.py
	python -m coverage run -m unittest
	python -m coverage report -m

site:
	source env/bin/activate && python3 app.py

create_env:
	python3 -m venv env
	source env/bin/activate && pip install -r requirements.txt
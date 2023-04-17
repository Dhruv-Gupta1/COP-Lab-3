coverage:
	python3 test.py
	python -m coverage run -m unittest
	python -m coverage report -m

site:
	source env/bin/activate && python3 app.py

create_env:
	source env/bin/activate

install:
	pip install flask 
	pip install flask_mysqldb
	pip install pyyaml
	pip install requests
	pip install pytest
	pip install coverage
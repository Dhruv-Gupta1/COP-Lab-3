coverage:
	python3 test.py
	python -m coverage run -m unittest
	python -m coverage report -m
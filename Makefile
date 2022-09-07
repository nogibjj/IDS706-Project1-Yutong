install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv src/test_*.py

format:	
	black src/*.py

lint:
	pylint --disable=R,C --ignore-patterns=src/test_.*?py src/*.py 

all: install lint test
lint:
	@black .
	@flake8 .
	
test:
	python -m pytest tests/

install-reqs:
	@pip install -r requirements/requirements.txt
	@pip install -r requirements/requirements-dev.txt
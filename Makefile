lint:
	@black .
	@flake8 .
	
test:
	python -m pytest tests/
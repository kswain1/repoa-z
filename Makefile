.phony: test


test:
	pytest -v --reuse-db tests/

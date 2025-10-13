.PHONY: format
format:
	black ./*.py

.PHONY: format-check
format-check:
	- black --check ./*.py
	- flake8 ./*.py
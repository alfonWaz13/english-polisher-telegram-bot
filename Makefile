.PHONY: format
format:
	black ./*.py

.PHONY: format-check
format-check:
	- black --check ./*.py
	- flake8 ./*.py

.PHONY: generate-zip
generate-zip:
	rm -rf packages deployment_package deployment_package.zip
	mkdir packages
	uv pip install -r pyproject.toml --target packages
	cp *.py packages && \
	cd packages && \
	zip -r deployment_package.zip . && \
	mv deployment_package.zip ../
SHELL = bash

.PHONY: clean
clean:
	rm -rf dist/ build/ *.egg-info

.PHONY: build
build:
	python setup.py sdist bdist_wheel


.PHONY: release
release: clean build
	echo && echo && echo _____________________ \
	&& echo Check version: $(shell grep version serverify.py) vs $(shell curl -s https://pypi.python.org/pypi/serverify-pip/json | grep '"version"' | xargs)
	@read -p "Release? [yN]: " -n 1 -r; \
	if [ "$$REPLY" == "y" ]; then echo && twine upload -s dist/*; else echo "Aborted."; fi

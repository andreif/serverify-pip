SHELL = bash

.PHONY: help  # shows available commands
help: Makefile
	@echo "\nAvailable commands:\n"
	@sed -n 's/^.PHONY:\(.*\)/ *\1/p' $<
	@echo


.PHONY: clean  # removes build files
clean:
	rm -rf dist/ build/ *.egg-info


.PHONY: build  # builds wheel and tar
build:
	pip install twine wheel
	python setup.py sdist bdist_wheel


.PHONY: release  # runs clean, build, and then pushes to pypi
release: clean build
	@echo && echo && echo _____________________ \
	&& echo Check version: $(shell grep -e '^__version__' serverify.py) vs \
	$(shell curl -s https://pypi.org/pypi/serverify-pip/json | python -m json.tool | grep '"version"' | xargs)
	@read -p "Release? [yN]: " -n 1 -r; \
	if [ "$$REPLY" == "y" ]; then echo && twine upload -s dist/*; else echo "Aborted."; fi

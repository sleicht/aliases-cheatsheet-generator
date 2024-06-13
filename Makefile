# Variables
VENV_NAME=.venv
PYTHON=$(VENV_NAME)/bin/python
PIP=$(VENV_NAME)/bin/pip

# For Windows, use these paths
# PYTHON=$(VENV_NAME)/Scripts/python
# PIP=$(VENV_NAME)/Scripts/pip

# Check if a package is installed
define is_installed
	$(PYTHON) -c "import $1" >/dev/null 2>&1 || { echo >&2 "Installing $1..."; $(PIP) install $1; }
endef

# Targets
all: venv install_deps generate_files

venv:
	python3 -m venv $(VENV_NAME)

install_deps: venv
	$(PIP) install -r requirements.txt

generate_files:
	$(PYTHON) run.py

install_dev_deps: venv
	$(PIP) install -r requirements-dev.txt

format_deps: install_dev_deps
	$(call is_installed,isort)
	$(call is_installed,black)

lint_deps: install_dev_deps
	$(call is_installed,flake8)

format: format_deps
	$(VENV_NAME)/bin/isort .
	$(VENV_NAME)/bin/black .

lint: lint_deps
	$(VENV_NAME)/bin/flake8 .

clean:
	rm -rf $(VENV_NAME) aliases.md aliases.html aliases.pdf

.PHONY: all venv install_deps generate_files install_dev_deps format_deps lint_deps format lint clean

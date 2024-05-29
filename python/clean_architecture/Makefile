PROJECT_NAME := clean_arch
DATABASE_NAME := clean_arch_database
PYTHON_VERSION := 3.11.0
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

create-venv: ## install python, create virtualenv and set virtualenv to current
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)
	pip install -U pip pipenv

setup: ## install requirements
	pipenv install --deploy

setup-dev: ## install requirements
	pipenv install --deploy --dev

build: ## up all containers and building the project image
	docker-compose up -d --build

up: ## up all containers
	docker-compose --env-file docker-compose.env up -d --remove-orphans

down: ## down all containers
	docker-compose down
	docker-compose rm

test: ## running test
	pytest -s -v

ruff: ## run ruff
	ruff check src
	ruff format src

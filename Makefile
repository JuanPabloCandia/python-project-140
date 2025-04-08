ci:
	docker compose -f docker-compose.yml down -v --remove-orphans
	docker compose -f docker-compose.yml build
	docker compose -f docker-compose.yml run app make setup
	docker compose -f docker-compose.yml up --abort-on-container-exit

compose-setup: compose-build compose-app-setup

compose-build:
	docker compose build

compose-app-setup:
	docker compose run app make setup

compose-bash:
	docker compose run app bash

compose-lint:
	docker compose run app make lint

compose-test:
	docker compose -f docker-compose.yml up --abort-on-container-exit

setup:
	uv sync

test:
	rspec

lint:
	uv run ruff check --config=./ruff.toml code

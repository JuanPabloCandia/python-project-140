setup:
	uv sync

lint:
	uv run ruff check --config=./ruff.toml code
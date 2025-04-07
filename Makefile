setup:
	uv sync

test:
	rspec

lint:
	uv run ruff check --config=./ruff.toml code
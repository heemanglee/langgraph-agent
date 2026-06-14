.PHONY: dev test lint format sync

dev:
	uv run uvicorn main:app --reload --port 8001

test:
	uv run pytest -v

lint:
	uv run ruff check .

format:
	uv run ruff format .

sync:
	uv sync
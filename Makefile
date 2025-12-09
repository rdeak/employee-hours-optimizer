.PHONY: check format lint typecheck validate

check: format lint typecheck

format:
	uv run ruff format .

lint:
	uv run ruff check . --fix

typecheck:
	uv run mypy .

validate:
	uv run pre-commit run --all-files
run:
	poetry run uvicorn src.app:app --reload

fmt:
	ruff format .

lint list_strict:
	mypy .
	ruff check --fix --show-fixes --exit-non-zero-on-fix .

lint_fix: fmt lint

migrate:
	poetry run python -m yoyo apply -vvv --batch --database "postgresql+psycopg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB_NAME}" ./migrations

setup:
	@poetry install --no-root --sync
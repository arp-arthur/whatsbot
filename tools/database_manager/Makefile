.EXPORT_ALL_VARIABLES:
DB_USER:=xxxx
DB_PASS:=xxxx
DB_HOST:=xxxxx
DB_PORT:=xxxxx
DB_NAME:=xxxxx


init:
	@poetry install
	@poetry run pip install --force-reinstall --no-deps ../../database_models

migration:
	@poetry run pip install --force-reinstall --no-deps ../../database_models
	@poetry run alembic revision --autogenerate -m "$(m)"

apply-migration:
	@poetry run alembic upgrade head

apply-downgrade:
	@poetry run alembic downgrade -1
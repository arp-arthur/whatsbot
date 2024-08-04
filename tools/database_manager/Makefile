.EXPORT_ALL_VARIABLES:
DB_USER:=db_user
DB_PASS:=db_pass
DB_HOST:=db_host
DB_PORT:=db_port
DB_NAME:=db_name


init:
	@poetry install
	@poetry run pip install --force-reinstall --no-deps ../../database_models

migration:
	@poetry run pip install --force-reinstall --no-deps ../../database_models
	@poetry run alembic revision --autogenerate -m "$(m)"

apply-migration:
	@poetry run alembic upgrade head

apply-downgrade:
	@poetry run downgrade -1
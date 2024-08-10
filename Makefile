include .env
export $(shell sed 's/=.*//' .env)
START_NGROK_SCRIPT = scripts/start_tunnel.sh
END_TUNNEL_SCRIPT = scripts/end_tunnel.sh
.EXPORT_ALL_VARIABLES:
DATABASE_URL:=postgresql+pg8000://$(DB_USER):$(DB_PASS)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)

test:
	@poetry run pytest .

start_tunnel:
	@bash $(START_NGROK_SCRIPT)

end_tunnel:
	@bash $(END_TUNNEL_SCRIPT)

init:
	@poetry install

load-env:
	@export $(shell cat .env | xargs)

run: load-env
	@poetry run uvicorn main:app --port 8080 --reload
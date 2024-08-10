START_NGROK_SCRIPT = scripts/start_tunnel.sh
END_TUNNEL_SCRIPT = scripts/end_tunnel.sh
DB_USER = xxxxx
DB_PASS = xxxxxx
DB_HOST = xxxxxx
DB_PORT = xxxxxx
DB_NAME = xxxxx
.EXPORT_ALL_VARIABLES:
TWILIO_ACCOUNT_SID:=XXXXXXXXXXXXXXXXXXXX
TWILIO_AUTH_TOKEN:=xxxxxxxxxxxxxxxxxxxxxx
MY_NUMBER:=+14155238886
DATABASE_URL:=postgresql+pg8000://$(DB_USER):$(DB_PASS)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)


test:
	@poetry run pytest .

start_tunnel:
	@bash $(START_NGROK_SCRIPT)

end_tunnel:
	@bash $(END_TUNNEL_SCRIPT)

init:
	@poetry install

run:
	@poetry run uvicorn main:app --port 8080 --reload

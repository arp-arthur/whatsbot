START_NGROK_SCRIPT = scripts/start_tunnel.sh
.EXPORT_ALL_VARIABLES:
TWILIO_ACCOUNT_SID:="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_AUTH_TOKEN:="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
MY_NUMBER:="+xxxxxxxxxxxxxx"


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
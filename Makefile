START_NGROK_SCRIPT = scripts/start_tunnel.sh
END_TUNNEL_SCRIPT = scripts/end_tunnel.sh
.EXPORT_ALL_VARIABLES:
TWILIO_ACCOUNT_SID:="XXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_AUTH_TOKEN:="xxxxxxxxxxxxxxxxxxxxxxxxx"
MY_NUMBER:="+xxxxxxxxxxxxx"
env:=dev


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
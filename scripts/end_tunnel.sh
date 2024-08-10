set -a && source .env && set +a

kill $NGROK_PID

NGROK_HTTP="NGROK_HTTP_URL"
NGROK_HTTPS="NGROK_HTTPS_URL"
NGROK_PROCESS="NGROK_PID"

ENV_FILE=".env"

sed -i "/^$NGROK_HTTP=/d" $ENV_FILE
sed -i "/^$NGROK_HTTPS=/d" $ENV_FILE
sed -i "/^$NGROK_PROCESS=/d" $ENV_FILE
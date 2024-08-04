set -a && source .env && set +a

kill $NGROK_PID

rm .env
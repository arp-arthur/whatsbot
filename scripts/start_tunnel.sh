#!/bin/bash

NGROK_CONFIG_DIR="$HOME/.ngrok2"
NGROK_CONFIG_FILE="$NGROK_CONFIG_DIR/ngrok.yml"

if [ ! -f "$NGROK_CONFIG_DIR" ]; then
    mkdir -p "$NGROK_CONFIG_DIR"
fi

if [ ! -f "$NGROK_CONFIG_FILE" ]; then
    read -p "Put your ngrok token here: " NGROK_TOKEN
    ngrok authtoken $NGROK_TOKEN
else
    echo "Token already set."
fi

if ! command -v jq &> /dev/null; then
    echo "You have to install jq so the API can work properly."
    exit 1
fi

nohup ngrok http 8080 > /dev/null &
NGROK_PID=$!

sleep 2

NGROK_HTTPS_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

if [ -n "$NGROK_HTTPS_URL" ]; then
    NGROK_HTTP_URL=$(echo $NGROK_HTTPS_URL | sed 's/https:/http:/')
fi

echo "NGROK_HTTP_URL=$NGROK_HTTP_URL" > .env
echo "NGROK_HTTPS_URL=$NGROK_HTTPS_URL" >> .env
echo "NGROK_PID=$NGROK_PID" >> .env

echo $NGROK_HTTPS_URL
echo $NGROK_HTTP_URL

echo "Process $NGROK_PID started."

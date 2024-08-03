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

ngrok http 8080 > /dev/null &
NGROK_PID=$!

sleep 2

NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

export NGROK_URL

echo $NGROK_URL

wait $NGROK_PID
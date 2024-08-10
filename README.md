# Whastbot - A simple chatbot for whatsapp

The goal of this project is to have a fully functional chatbot to filter client info for later support.

## Contents
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Author](#author)

## Installation
1. Clone the repository
```bash
git clone git@github.com:arp-arthur/whatsbot.git
```

2. You need to install poetry

3. Install the dependencies
```bash
make init
```

## Setup

1. Install **ngrok**: I won't put instructions here 'cause it depends on your OS.

2. Create a twilio account.

3. Create a .env file (in the root directory) and put **TWILIO_ACCOUNT_SID** and **TWILIO_AUTH_TOKEN** from your twilio account

4. You have to setup your postgres server and create a database for the app.

5. Fill the both **.env files** (the one that you recently created and the other inside ./tools/database_manager folder) with your info (DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME)

6. Installing database manager dependencies (./tools/database_manager)
```bash
make init
```

7. Make the database migration (in ./tools/database_manager)
```bash
make migration
make apply-migration
```

## Usage

1. Start tunnel (ngrok)
```bash
make start_tunnel
```

2. Take note of the https address and go to your twilio account (in the website) and put inside the **When a message comes in** field with /whatsbot/receive_message at the end

3. The same thing for **Status callback URL** field with /whatsbot/status_callback at the end

4. Start the API
```bash
make run
```

5. In your twilio account, initiate a whatsapp conversation (by reading the qr-code)

6. In whatsapp, send some message and watch how the chatbot works.

7. To end ngrok process:
```bash
make end_tunnel
```

## Author
- **Arthur Pinheiro**  
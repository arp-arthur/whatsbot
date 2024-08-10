from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.twilio_config import TWILIO_SIGNATURE
from app.api.endpoints.whatsbot import wprouter
import os
from dotenv import load_dotenv

load_dotenv()

tunnel_url = os.getenv("NGROK_HTTPS_URL")

app = FastAPI(
    title="Whatsbot API",
    description="This is a whatsapp chatbot API custom made",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    tunnel_url,
]

allowed_headers = [
    "Content-Type",
    "User-Agent",
    TWILIO_SIGNATURE
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=allowed_headers
)

app.include_router(wprouter, prefix="/whatsbot")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.twilio_config import TWILIO_SIGNATURE
from app.api.endpoints.whatsbot import wprouter
import os
from dotenv import load_dotenv

load_dotenv()

tunnel_url = os.getenv("NGROK_HTTPS_URL")

app = FastAPI()

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
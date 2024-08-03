from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.validate import TWILIO_SIGNATURE
from app.api.endpoints.whatsbot import wprouter
import os

tunnel = os.getenv("NGROK_URL")
print(tunnel)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
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
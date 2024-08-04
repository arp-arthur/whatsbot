from fastapi import HTTPException
from twilio.request_validator import RequestValidator
from app.core.twilio_config import TWILIO_TOKEN

def validate_twilio(url: str, post_data: dict, twilio_sign: str) -> None:
    validator = RequestValidator(TWILIO_TOKEN)
    if not validator.validate(url, post_data, twilio_sign):
        raise HTTPException(status_code=400, detail="Bad Request.")
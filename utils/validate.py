from twilio.request_validator import RequestValidator
from exceptions.exceptions import CustomHTTPException
import os

TWILIO_SIGNATURE = "X-Twilio-Signature"
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")

def validate_twilio(url: str, post_data: dict, twilio_sign: str):
    validator = RequestValidator(TWILIO_TOKEN)
    if not validator.validate(url, post_data, twilio_sign):
        raise CustomHTTPException()
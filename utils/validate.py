from fastapi import HTTPException
from twilio.request_validator import RequestValidator
from app.core.twilio_config import TWILIO_TOKEN
import re

def validate_twilio(url: str, post_data: dict, twilio_sign: str) -> None:
    validator = RequestValidator(TWILIO_TOKEN)
    if not validator.validate(url, post_data, twilio_sign):
        raise HTTPException(status_code=400, detail="Bad Request.")
    
def is_message_received_valid(msg: str) -> bool:
    phone_pattern = r"[0-9]{10}$"
    name_pattern = r"[A-Za-z]$"
    cpf_pattern = r"[0-9]{11}$"
    cnpj_pattern = r"[0-9A-Z]{12}[0-9]{2}$"
    data_nasc_pattern = r"[0-9]{2}/[0-9]{2}/[0-9]{4}$"

    return (re.match(phone_pattern, msg) or 
            re.match(name_pattern, msg) or
            re.match(cpf_pattern, msg) or
            re.match(cnpj_pattern, msg) or
            re.match(data_nasc_pattern, msg))

def sanitize_message(msg: str) -> str:
    pattern = r"[./-]*(whatsapp:)*"
    return re.sub(pattern, "", msg)
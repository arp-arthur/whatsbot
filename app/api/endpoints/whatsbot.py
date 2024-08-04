from fastapi import APIRouter, Request
from utils.validate import validate_twilio
from app.core.twilio_config import TWILIO_SIGNATURE

wprouter = APIRouter()

@wprouter.post("/receive_message")
async def whatsbot(request: Request) -> dict:
    try:
        #url = str(request.url)

        form_ = await request.form()
        origin = form_.get("From")
        msg = form_.get("Body")

        #twilio_sign = request.headers.get(TWILIO_SIGNATURE)

        #validate_twilio(url, form_, twilio_sign)

        print(origin)
        print(msg)

        return {"msg": f"Message received from: {origin}: {msg}", "code": 200}
    
    except Exception as e:
        return {"msg": f"There's something wrong. Transaction could not be concluded.", "code": 400}
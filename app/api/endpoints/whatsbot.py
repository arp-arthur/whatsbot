from fastapi import APIRouter, Request
from utils.validate import TWILIO_SIGNATURE, validate_twilio

wprouter = APIRouter()

@wprouter.post("/whatsbot")
async def whatsbot(request: Request) -> dict:
    try:
        print("tá chegando aqui")

        url = request.url

        form = await request.form()
        origin = form.get("From")
        msg = form.get("Body")

        post_data = dict(form)

        twilio_sign = request.headers.get(TWILIO_SIGNATURE, "")

        validate_twilio(url, post_data, twilio_sign)

        print(origin)
        print(msg)

#        print(post_data)

#        from_number = post_data.get("From")
#        body = post_data.get("Body")

        return {"msg": f"Message received from: {origin}: {msg}", "code": 200}
    
    except Exception as e:
        return {"msg": f"There's something wrong. Transaction could not be concluded.", "code": 400}
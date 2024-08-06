from fastapi import APIRouter, Request, Depends
from utils.validate import validate_twilio
from app.core.twilio_config import TWILIO_SIGNATURE
from app.services.message_manager import Message
from app.db.db_operations import DatabaseOperations
from app.schemas.build_objects import BuildObjects
from app.core.log_config import logger

wprouter = APIRouter()

def get_db_operations() -> DatabaseOperations:
    return DatabaseOperations()

def get_build_objects() -> BuildObjects:
    return BuildObjects()

@wprouter.post("/receive_message")
async def whatsbot(request: Request, db: DatabaseOperations = Depends(get_db_operations), build_objects: BuildObjects = Depends(get_build_objects) ) -> dict:
    try:
        form_ = await request.form()
        origin = form_.get("From")
        msg = form_.get("Body")

        #twilio_sign = request.headers.get(TWILIO_SIGNATURE)

        #validate_twilio(url, form_, twilio_sign)

        # I need to know if this is the first time the user is sending message
        # to do this, I have to know if this number is in the database
        # but before I need to clean the origin variable
        message_manager = Message(origin, msg)
        msg, origin = message_manager.clean_origin_and_message()

        # Now I can search for this origin in the database
        client = db.get_client_by_phonenumber(origin)
        
        if client is not None:
            message_to_be_asked = db.get_message_from_client_id(client[0])
            print('CHEGANDO AQUIII')
            print(message_to_be_asked)
            if not message_to_be_asked:
                message_to_be_asked = db.get_first_message()
                client_session = build_objects.build_client_session(client_id=client[0], message_id=message_to_be_asked)
                db.insert_client_session(client=client_session)
            else:
                pass

        db.commit()
        return {"msg": f"Message received from: {origin}: {msg}", "code": 200}
    
    except Exception as e:
        print(e)
        return {"msg": f"There's something wrong. Transaction could not be concluded.", "code": 400}
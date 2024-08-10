from fastapi import APIRouter, Request, Depends
from app.utils.validate import validate_twilio
from app.config.twilio_config import TWILIO_SIGNATURE
from app.services.message_manager import Message
from app.db.db_operations import DatabaseOperations
from app.pydantic_models.build_objects import BuildObjects
from app.pydantic_models.pydantic_models import MessageModel, StatusCallback
from app.config.log_config import logger
import traceback

wprouter = APIRouter()

def get_db_operations() -> DatabaseOperations:
    return DatabaseOperations()

def get_build_objects() -> BuildObjects:
    return BuildObjects()

def parse_request(payload) -> tuple:
    origin = payload.get("From")
    if origin is None:
        logger.error("From is missing.")
        raise

    msg = payload.get("Body")
    if msg is None:
        logger.error("Body is missing.")
        raise

    return origin, msg

@wprouter.post("/status_callback", response_model=StatusCallback)
async def status_callback(request: Request):
    try:
        form_ = await request.form()
        message_sid = form_.get("MessageSid")
        message_status = form_.get("MessageStatus")

        return {"status": "received"}
    except Exception as e:
        logger.error({traceback.format_exc()})
        return {"msg": f"There's something wrong. Transaction could not be concluded.", "code": 400}
    

@wprouter.post("/receive_message", response_model=MessageModel)
async def whatsbot(request: Request, db: DatabaseOperations = Depends(get_db_operations), build_objects: BuildObjects = Depends(get_build_objects) ) -> dict:
    """
    The goal here is to receive a message and get the right response to be sent
    - **To**: a string containing your number (phone number)
    - **From**: a string containing the origin (phone number)
    - **Body**: a string with the message that was sent to us    
    """
    
    try:
        form_ = await request.form()
        origin, msg = parse_request(form_)
        
        #twilio_sign = request.headers.get(TWILIO_SIGNATURE)

        #validate_twilio(url, form_, twilio_sign) -- I think there's an incompatibility with python 3.12... to be tested

        message_manager = Message(origin, msg)
        msg, origin = message_manager.clean_origin_and_message()

        client_id = db.get_client_by_phonenumber(origin)

        if client_id is not None:
            message_to_insert_id, message_text_to_be_sent, message_type_to_insert = message_manager.process_client_message(db, client_id, msg)
        else:
            client = build_objects.build_new_client(origin)
            client_id = db.insert_new_client(client)
            message_to_insert_id, _, _ = db.get_first_message()
            message_to_insert_id += 1
        
        message_manager.send_message(message_text_to_be_sent)

        db.update_session(client_id)

        if message_type_to_insert != "final":
            client_session = build_objects.build_client_session(client_id=client_id, message_id=message_to_insert_id+1)
            db.insert_client_session(client_session=client_session)
        logger.info("commiting...")
        db.commit()
        logger.info("changes have been commited")
        return {"msg": f"Message received from: {origin}: {msg}", "code": 200}
    
    except Exception as e:
        db.rollback()
        logger.error({traceback.format_exc()})
        return {"msg": f"There's something wrong. Transaction could not be concluded.", "code": 400}
    finally:
        db.close()
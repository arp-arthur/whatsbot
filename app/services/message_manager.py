from twilio.rest import Client
from app.config.twilio_config import account_sid, auth_token, my_number
from app.utils.validate import is_message_received_valid, sanitize_message, is_date
from app.db.db_operations import DatabaseOperations
import datetime

class Message:
    def __init__(self, origin:str, msg: str) -> None:
        self.origin = origin
        self.msg = msg
        print(account_sid, auth_token)
        self.client = Client(account_sid, auth_token)


    def process_message(self) -> bool:
        # here I have to sanitize the message because some messages come with garbage (specially the phone number)
        msg = sanitize_message(self.msg)
        return is_message_received_valid(msg)
    

    def clean_origin_and_message(self) -> tuple:
        if is_date(self.msg):
            msg = datetime.datetime.strptime(self.msg, "%d/%m/%Y")
        else:
            msg = sanitize_message(self.msg)
        origin = sanitize_message(self.origin)

        return msg, origin
    
    def process_client_message(self, db: DatabaseOperations, client_id: int, msg: str) -> tuple:
        if db.is_session_active(client_id):
            message_to_insert_id, message_text_to_be_sent, message_type_to_insert = db.get_message_from_client_id(client_id)
            previous_message_type = db.get_message_type(message_to_insert_id-1)
            db.update_client(previous_message_type, client_id, msg)
        else:
            message_to_be_sent_id, message_text_to_be_sent, message_type_to_be_sent = db.get_first_message()
            message_to_insert_id, message_type_to_insert = message_to_be_sent_id, message_type_to_be_sent
        
        return message_to_insert_id, message_text_to_be_sent, message_type_to_insert

    def send_message(self, response: str) -> None:
        number = f"whatsapp:{my_number}"
        self.client.messages.create(
            from_=number,
            body=response,
            to=self.origin
        )
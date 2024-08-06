from twilio.rest import Client
from app.core.twilio_config import account_sid, auth_token, my_number
from utils.validate import is_message_received_valid, sanitize_message

class Message:
    def __init__(self, origin:str, msg: str) -> None:
        self.origin = origin
        self.msg = msg
        self.client = Client(account_sid, auth_token)


    def process_message(self) -> bool:
        # here I have to sanitize the message because some messages come with garbage (specially the phone number)
        msg = sanitize_message(self.msg)
        return is_message_received_valid(msg)
    

    def clean_origin_and_message(self) -> tuple:
        msg = sanitize_message(self.msg)
        origin = sanitize_message(self.origin)

        return msg, origin

    def process_response(self) -> None:
        self.response = "This is my response"

    def send_message(self) -> None:
        message = self.client.create(
            from_=my_number,
            body=self.response,
            to=self.origin
        )
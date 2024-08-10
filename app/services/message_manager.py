from twilio.rest import Client
from app.config.twilio_config import account_sid, auth_token, my_number
from app.utils.validate import is_message_received_valid, sanitize_message, is_date
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

    def send_message(self, response: str) -> None:
        number = f"whatsapp:{my_number}"
        print(number)
        print(response)
        print(self.origin)
        self.client.messages.create(
            from_=number,
            body=response,
            to=self.origin
        )
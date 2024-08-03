from twilio.rest import Client
from core.twilio_config import account_sid, auth_token, my_number

class Message:
    def __init__(self, origin:str, msg: str) -> None:
        self.origin = origin
        self.msg = msg
        self.client = Client(account_sid, auth_token)

    def receive_message(self) -> None:
        msg = self.msg

    def process_message(self) -> None:
        pass

    def process_response(self) -> None:
        self.response = "This is my response"

    def send_message(self) -> None:
        message = self.client.create(
            from_=my_number,
            body=self.response,
            to=self.origin
        )
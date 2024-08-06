from datetime import datetime
from pydantic import BaseModel

class Client(BaseModel):
    name: str
    phone_number: str
    cpf_cnpj: str
    birth_date: datetime

class Message(BaseModel):
    message_text: str

class ClientSession(BaseModel):
    client_id: int
    message_id: int

class ClientSessionCreate(ClientSession):
    client_id: int
    message_id: int
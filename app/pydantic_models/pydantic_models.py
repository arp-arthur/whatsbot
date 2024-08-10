from datetime import datetime
from pydantic import BaseModel

class Client(BaseModel):
    name: str | None
    phone_number: str
    cpf_cnpj: str | None
    birth_date: datetime | None

class Message(BaseModel):
    message_text: str

class ClientSession(BaseModel):
    client_id: int
    message_id: int

class ClientSessionCreate(ClientSession):
    client_id: int
    message_id: int
    
class ClientCreate(BaseModel):
    phone_number: str

    
class MessageModel(BaseModel):
    msg: str
    code: int

class StatusCallback(BaseModel):
    status: str

class PayloadModel(BaseModel):
    To: str
    From: str
    Body: str
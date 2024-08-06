from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String, TIMESTAMP, func, ForeignKey, Text, Boolean

Base = declarative_base()

class Clients(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    cpf_cnpj = Column(String(14), nullable=True, unique=True)
    birth_date = Column(Date, nullable=True)
    reference_date = Column(TIMESTAMP, nullable=False, server_default=func.now())

class Messages(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    message_text = Column(Text, nullable=False)

class ClientSessions(Base):
    __tablename__ = "client_sessions"

    client_session_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey(Clients.client_id), nullable=False)
    message_id = Column(Integer, ForeignKey(Messages.message_id), nullable=False)
    interaction_date = Column(TIMESTAMP, nullable=False, server_default=func.now())
    is_last_message = Column(Boolean, nullable=False, server_default="TRUE")
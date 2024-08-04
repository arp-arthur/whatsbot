from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String, TIMESTAMP, func

Base = declarative_base()

class Clients(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    cpf_cnpj = Column(String(14), nullable=True, unique=True)
    birth_date = Column(Date, nullable=True)
    reference_date = Column(TIMESTAMP, nullable=False, server_default=func.now())
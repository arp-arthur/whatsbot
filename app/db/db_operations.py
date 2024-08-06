from database_models import database_models as models
from .db_connect import BotDatabase
from app.schemas.pydantic_models import ClientSessionCreate
from sqlalchemy.exc import SQLAlchemyError
from app.core.log_config import logger

class DatabaseOperations(BotDatabase):
    def get_client_by_phonenumber(self, phone_number: str) -> tuple:
        try:    
            client = self.session.query(
                models.Clients.client_id,
                models.Clients.name,
                models.Clients.cpf_cnpj,
                models.Clients.birth_date,
                models.Clients.phone_number
            ).filter(
                models.Clients.phone_number == phone_number
            ).first()

            return client
        except SQLAlchemyError:
            logger.error("Couldn't get client")
            raise

    
    def get_message_from_client_id(self, client_id) -> str:    
        try:
            message = self.session.query(
                models.Messages.message_text
            ).select_from(
                models.ClientSessions
            ).join(
                models.Messages,
                models.ClientSessions.message_id == models.Messages.message_id
            ).filter(
                models.ClientSessions.client_id == client_id,
                models.ClientSessions.is_last_message.is_(True)
            ).first()

            if message is None:
                return None
            
            return message
        
        except SQLAlchemyError as e:
            print(e)
            logger.error("Coudn't get the message")
            raise

    def get_first_message(self) -> str:
        try:
            message = self.session.query(
                models.Messages.message_id
            ).order_by(
                models.Messages.message_id
            ).first()

            return message
        except SQLAlchemyError:
            logger.error("Couldn't get the first message")
            raise
        
    
    def insert_client_session(self, client_session: ClientSessionCreate) -> None:
        try:
            print('CHEGANDO AQUI')
            client_session = models.ClientSessions(**client_session.model_dump())
            self.session.add(client_session)
            print('CHEGANDO AQUI DE NOVO')
            logger('TAMBÉM IMPRIMINDO ISSO AQUI')
        except SQLAlchemyError:
            logger.error("Coundn't insert client session")
            raise
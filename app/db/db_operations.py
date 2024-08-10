from database_models import database_models as models
from .db_connect import BotDatabase
from app.pydantic_models.pydantic_models import ClientSessionCreate, ClientCreate
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from app.config.log_config import logger

class DatabaseOperations(BotDatabase):
    def get_client_by_phonenumber(self, phone_number: str) -> tuple:
        try:    
            client = self.session.query(
                models.Clients.client_id
            ).filter(
                models.Clients.phone_number == phone_number
            ).first()

            if client is None:
                return None

            return client.client_id
        except SQLAlchemyError:
            logger.error("Couldn't get client")
            raise

    def is_session_active(self, client_id: int) -> bool:
        try:
            active_session = self.session.query(
                models.ClientSessions.client_session_id
            ).filter(
                models.ClientSessions.client_id == client_id,
                models.ClientSessions.is_last_message.is_(True)
            ).first()


            return active_session != None
        except SQLAlchemyError:
            logger.error("Couldn't get client session")
            raise

    def get_message_type(self, message_id: int) -> tuple | None:
        try:
            message = self.session.query(
                models.Messages.message_type
            ).filter(
                models.Messages.message_id == message_id
            ).first()

            return message.message_type
        except SQLAlchemyError:
            logger.error("Couldn't get next message")
            raise



    
    def get_message_from_client_id(self, client_id: int) -> tuple | None:    
        try:
            message = self.session.query(
                models.Messages.message_id,
                models.Messages.message_text,
                models.Messages.message_type
            ).select_from(
                models.ClientSessions
            ).join(
                models.Messages,
                models.ClientSessions.message_id == models.Messages.message_id
            ).filter(
                models.ClientSessions.client_id == client_id,
                models.ClientSessions.is_last_message.is_(True)
            ).first()
            
            return message
        
        except SQLAlchemyError as e:
            print(e)
            logger.error("Coudn't get the message")
            raise

    def get_first_message(self) -> tuple:
        try:
            message = self.session.query(
                models.Messages.message_id,
                models.Messages.message_text,
                models.Messages.message_type
            ).order_by(
                models.Messages.message_id
            ).first()

            return message
        except SQLAlchemyError:
            logger.error("Couldn't get the first message")
            raise

    def update_session(self, client_id: int) -> None:
        try:
            logger.info("Updating session...")
            self.session.query(models.ClientSessions).filter(
                models.ClientSessions.client_id == client_id,
                models.ClientSessions.is_last_message.is_(True)
            ).update({"is_last_message": False}, synchronize_session=False)
            logger.info("Session has been updated")
        except SQLAlchemyError:
            logger.error("Couldn't update session")
            raise
    
    def update_client(self, message_type: str, client_id: int, incoming_message: str) -> None:
        try:
            logger.info("Updating client...")
            update_client = text(f"UPDATE clients set {message_type} = :incoming_message WHERE client_id = :client_id")
            logger.info(update_client)
            self.session.execute(update_client, {"incoming_message": incoming_message, "client_id": client_id})
        except SQLAlchemyError:
            logger.error("Couldn't update client")
            raise

    def insert_new_client(self, client: ClientCreate) -> int:
        try:
            logger.info("Inserting new client...")
            client = models.Clients(**client.model_dump())
            self.session.add(client)
            self.session.flush()
            logger.info("Client has been created")
            return client.client_id
        except SQLAlchemyError:
            logger.error("Couldn't insert new client")
            raise
    
    def insert_client_session(self, client_session: ClientSessionCreate) -> None:
        try:
            logger.info('Creating new session...')
            client_session = models.ClientSessions(**client_session.model_dump())
            self.session.add(client_session)
            logger.info('New session has been created')
        except SQLAlchemyError:
            logger.error("Coundn't insert client session")
            raise

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()
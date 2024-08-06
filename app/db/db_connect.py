from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.log_config import logger
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None

class BotDatabase:
    def __init__(self) -> None:
        global engine
        if engine is None:
            engine = create_engine(
                DATABASE_URL,
                pool_size=5,
                max_overflow=10,
                pool_timeout=30,
                pool_recycle=1800
            )
        self.session = sessionmaker(bind=engine)()
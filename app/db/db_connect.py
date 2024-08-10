from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.log_config import logger
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None

class BotDatabase:
    def __init__(self) -> None:
        global engine
        print(DATABASE_URL)
        if engine is None:
            engine = create_engine(
                DATABASE_URL,
                pool_size=5,
                max_overflow=10,
                pool_timeout=30,
                pool_recycle=1800
            )
        self.session = sessionmaker(bind=engine)()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import Config


class DBConnectionHandler:

    def __init__(self) -> None:
        self._connection_string = Config.SQLALCHEMY_DATABASE_URI
        self._engine = self._create_database_engine()
        self.session = None

    def _create_database_engine(self):
        return create_engine(self._connection_string)

    def get_engine(self):
        return self._engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self._engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

from sqlalchemy import create_engine
from src.config.settings import Config


class DBConnectionHandler:

    def __init__(self) -> None:
        self._connection_string = Config.SQLALCHEMY_DATABASE_URI
        self._engine = self._create_database_engine()

    def _create_database_engine(self):
        return create_engine(self._connection_string)

    def get_engine(self):
        return self._engine

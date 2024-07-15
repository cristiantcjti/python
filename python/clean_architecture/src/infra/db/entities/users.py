import uuid
from sqlalchemy import Column, String, Integer, Uuid
from src.infra.db.settings.base import base


class Users(base):
    __tablename__ = "users"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Users [id={self.id}, first_name={self.first_name}]"

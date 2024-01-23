from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi_db'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'N2fQsXlBY_CyRZkUJMhCtwexV06rk0kZRoHtJVCIkW4'
    '''
    import secrets

    token: str = secret.token_urlsafe(32)
    '''
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
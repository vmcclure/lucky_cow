from functools import cache

import pydantic
from pydantic_settings import BaseSettings


@cache
class Settings(BaseSettings):
    DB_USER: str = pydantic.Field(alias="POSTGRES_USER")
    DB_PASSWORD: str = pydantic.Field(alias="POSTGRES_PASSWORD")
    DB_SERVER: str = pydantic.Field(alias="POSTGRES_HOST")
    DB_PORT: int = pydantic.Field(alias="POSTGRES_PORT")
    DB_NAME: str = pydantic.Field(alias="POSTGRES_DB_NAME")

    CONN_TEMPLATE: str = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"

    @property
    def POSTGRE_DSN(self) -> str:
        # по хорошему бы избавиться от пачки параметров и заменить на postgres_dsn
        return self.CONN_TEMPLATE.format(
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            port=self.DB_PORT,
            host=self.DB_SERVER,
            name=self.DB_NAME,
        )

    class Config:
        env_file = ".env"

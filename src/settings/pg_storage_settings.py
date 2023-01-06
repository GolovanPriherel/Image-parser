import logging

from pydantic import Field, BaseSettings
from dotenv import load_dotenv

load_dotenv()


class PGStorageSetting(BaseSettings):

    # def __init__(self, test_host=None):
    #     self.test_host = test_host

    host: str = Field(env="PG_HOST", default="postgres_db")
    port: int = Field(env="PG_PORT", default=5432)
    username: str = Field(env="PG_USERNAME", default="postgres")
    password: str = Field(env="PG_PASSWORD", default="postgres")
    database: str = Field(env="PG_DATABASE", default="postgres")

    def geturl(self):
        return f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

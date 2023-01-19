import logging

from pydantic import Field, BaseSettings
from dotenv import load_dotenv

load_dotenv()


class PGStorageSetting(BaseSettings):
    # host: str = Field(env="PG_HOST", default="postgres_db")
    host: str = Field(env="TEST_URL", default="localhost")
    port: int = Field(env="PG_PORT", default=5432)
    username: str = Field(env="PG_USERNAME", default="postgres")
    password: str = Field(env="PG_PASSWORD", default="postgres")
    database: str = Field(env="PG_DATABASE", default="postgres")

    # Docker
    # def geturl(self):
    #     return f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'

    # No Docker
    def geturl(self):
        return f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

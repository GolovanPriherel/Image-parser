

from pydantic import BaseSettings, Field


class TestSettings(BaseSettings):
    test_url: str = Field(env="TEST_URL")



    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

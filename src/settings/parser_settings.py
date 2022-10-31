from pydantic import Field, BaseModel as BaseSchema


class ParserSettings(BaseSchema):
    website_url: str = Field(env="WEBSITE_URL", default="https://www.deviantart.com/")
    # driver_path: str = Field(default="data/chrome_driver/chromedriver_linux")
    test_website_url: str = Field(env="TEST_WEBSITE_URL", default="https://www.deviantart.com/")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
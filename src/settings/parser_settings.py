from pydantic import Field, BaseModel as BaseSchema

class ParserSettings(BaseSchema):
    website_url: str = Field(env="WEBSITE_URL", default="https://www.deviantart.com/")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
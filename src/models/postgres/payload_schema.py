import datetime

from pydantic import Field, BaseModel as BaseSchema

class PayloadSchema(BaseSchema):
    id: int
    image_title: str
    image_description: str
    image_path: str
    image_url: str
    inserted_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
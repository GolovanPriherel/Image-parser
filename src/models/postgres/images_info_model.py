import datetime

from pydantic import Field, BaseModel as BaseSchema
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime

from src.models.postgres.base_model import Base


class ImagesInfoModel(Base):
    __tablename__ = "images_info"

    id = Column("id", Integer, primary_key=True)
    image_title = Column("image_title", String, default="")
    image_description = Column("image_description", String, default="")
    image_path = Column("image_path", String, default="")
    image_url = Column("image_url", String, default="")
    inserted_at = Column("inserted_at", DateTime, default=str(datetime.datetime.now()))

    __table_args__ = {'extend_existing': True}


class ImagesInfoSchema(BaseSchema):
    id: int
    image_title: str
    image_description: str
    image_path: str
    image_url: str
    inserted_at: datetime.datetime = Field(default_factory=datetime.datetime.now())

import datetime
from typing import List, Optional

from pydantic import Field, BaseModel as BaseSchema
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime, ARRAY, Boolean

from src.models.postgres.base_model import Base


class ImagesInfoModel(Base):
    __tablename__ = "images_info"

    image_url = Column(String, nullable=True, primary_key=True)
    image_id = Column(String, nullable=True)
    author = Column(String, nullable=True)
    category = Column(String, nullable=True)
    image_title = Column(String, nullable=True)
    image_tags = Column(ARRAY(String), nullable=True)
    image_description = Column(String, nullable=True)
    image_path = Column(String, nullable=True)
    image_website = Column(String, nullable=True)
    published_at = Column(String, nullable=True)
    parsed = Column(Boolean, default=False)

    inserted_at = Column(DateTime, default_factory=datetime.datetime.now)

    __table_args__ = {'extend_existing': True}


class ImagesInfoSchema(BaseSchema):
    image_url: str = Field(default="")
    image_id: Optional[str]
    author: Optional[str]
    category: Optional[str]
    image_title: Optional[str]
    image_tags: Optional[List[str]]
    image_description: Optional[str]
    image_path: Optional[str]
    image_website: Optional[str]
    published_at: Optional[str] = Field(default="unknown")

    inserted_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class ImagesQueue(BaseSchema):
    image_name: str
    image_url: str

import datetime
from typing import List, Optional

from pydantic import Field, BaseModel as BaseSchema
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime, ARRAY, Boolean

from src.models.postgres.base_model import BaseModel


class Rule34ImagesInfoModel(BaseModel):
    __tablename__ = "rule34_images_info"

    image_url = Column(String, nullable=True, primary_key=True)
    image_id = Column(String, nullable=True)
    image_copyrights = Column(ARRAY(String), nullable=True)
    image_character_tag = Column(ARRAY(String), nullable=True)
    image_artists = Column(ARRAY(String), nullable=True)
    image_tags = Column(ARRAY(String), nullable=True)
    image_metadata = Column(ARRAY(String), nullable=True)
    image_path = Column(String, nullable=True)
    image_website = Column(String, nullable=True)
    image_rating = Column(Integer, nullable=True)
    published_at = Column(String, nullable=True)
    parsed = Column(Boolean, default=False)

    inserted_at = Column(DateTime, default_factory=datetime.datetime.now)


class Rule34ImagesInfoSchema(BaseSchema):
    image_url: str = Field(default="")
    image_id: Optional[str]
    image_copyrights: Optional[List[str]]
    image_character_tag: Optional[List[str]]
    image_artists: Optional[List[str]]
    image_tags: Optional[List[str]]
    image_metadata: Optional[List[str]]
    image_path: Optional[str]
    image_website: Optional[str]
    image_rating: Optional[int]
    parsed: bool = Field(default=False)

    published_at: Optional[str] = Field(default="unknown")
    inserted_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class Rule34ImagesInfoListSchema(BaseSchema):
    data: List[Rule34ImagesInfoSchema]


class InputURLs(BaseSchema):
    data: List[str]

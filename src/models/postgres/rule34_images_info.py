import datetime
from typing import List, Optional

from pydantic import Field, BaseModel as BaseSchema
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime, ARRAY, Boolean

from src.models.postgres.base_model import Base


class Rule34ImagesInfoModel(Base):
    __tablename__ = "images_info"

    image_url = Column(String, nullable=True, primary_key=True)
    image_id = Column(String, nullable=True)
    image_copyrights = Column(ARRAY(String), nullable=True)
    image_character_tag = Column(ARRAY(String), nullable=True)
    image_artists = Column(ARRAY(String), nullable=True)
    image_tags = Column(ARRAY(String), nullable=True)
    image_metadata = Column(ARRAY(String), nullable=True)
    image_path = Column(String, nullable=True)
    image_website = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=True)
    parsed = Column(Boolean, default=False)

    inserted_at = Column("inserted_at", DateTime, default=str(datetime.datetime.now()))

    __table_args__ = {'extend_existing': True}


class Rule34ImagesInfoSchema(BaseSchema):
    image_url: str = Field(default="")
    image_id: Optional[str]
    image_copyright: Optional[List[str]]
    image_character_tag: Optional[List[str]]
    image_artists: Optional[List[str]]
    image_tags: Optional[List[str]]
    image_metadata: Optional[List[str]]
    image_path: Optional[str]
    image_website: Optional[str]
    published_at: Optional[datetime.datetime] = Field(default_factory=datetime.datetime.now)
    inserted_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class ImagesQueue(BaseSchema):
    image_name: str
    image_url: str

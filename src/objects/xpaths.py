from typing import List

from pydantic import Field, BaseModel as BaseSchema

class XPaths(BaseSchema):
        image_title: str = Field(default="", alias="image_title_xpath")
        image_tags: List[str] = Field(default="", alias="image_tags_xpath")
        image_description: str = Field(default="", alias="image_description_xpath")
        # image_url: str = Field(default="", alias="image_url_xpath")
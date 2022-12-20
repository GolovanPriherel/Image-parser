from typing import List

from pydantic import Field, BaseModel as BaseSchema


class Rule34XPaths(BaseSchema):
    picture_profile: str = Field(default="//img[@class='preview']/parent::a/@href")
    image_copyrights: str = Field(default="//li[@class='tag-type-copyright tag']/a[2]/text()")
    image_character_tag: List[str] = Field(default="//li[@class='tag-type-character tag']/a[2]/text()")
    image_artist: List[str] = Field(default="//li[@class='tag-type-artist tag']/a[2]/text()")
    image_tags: List[str] = Field(default="//li[@class='tag-type-general tag']/a[2]/text()")
    image_metadata_tags: List[str] = Field(default="//li[@class='tag-type-metadata tag']/a[2]/text()")
    full_image_href: str = Field(default="//a[contains(text(), 'Original image')]/@href")

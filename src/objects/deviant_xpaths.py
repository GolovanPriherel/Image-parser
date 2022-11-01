from typing import List

from pydantic import Field, BaseModel as BaseSchema


class DeviantArtXPaths(BaseSchema):
    author: str = Field(default="//html/body/div[1]/main/div/div[3]/div/div[1]/div/div[2]/div[2]/div/div/a/span[1]/text()",
                        alias="author_xpath")
    image_title: str = Field(default="//html/body/div[1]/main/div/div[3]/div/div[1]/div/div[2]/div[1]/h1/text()",
                             alias="image_title_xpath")
    image_tags: List[str] = Field(default="//html/body/div[1]/main/div/div[3]/div/div[3]/div/a/span/text()",
                                  alias="image_tags_xpath")
    image_description: str = Field(default="//html/body/div[1]/main/div/div[3]/div/div[4]/div/div/text()",
                                   alias="image_description_xpath")
    more_arts_from: str = Field(default="//html/body/div[1]/main/div/div[2]/div[2]/div[2]",
                          alias="more_url_xpath")
    suggested_collections: str = Field(default="",
                               alias="suggested_collections_xpath")
    # image_url: str = Field(default="", alias="image_url_xpath")

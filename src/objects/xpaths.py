from typing import List

from pydantic import Field, BaseModel as BaseSchema


class XPaths(BaseSchema):
        author: str = Field(default="///main/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div/a/data_username", alias="author_xpath")
        image_title: str = Field(default="", alias="image_title_xpath")
        image_tags: List[str] = Field(default="/html/body/div[1]/main/div/div[2]/div/div[3]/div/a[1]/span/text()", alias="image_tags_xpath")
        image_description: str = Field(default="", alias="image_description_xpath")
        # image_url: str = Field(default="", alias="image_url_xpath")

from typing import List

from pydantic import Field, BaseModel as BaseSchema


class DeviantArtXPaths(BaseSchema):
    deviation_link_selenium: str = Field(default="//a[@data-hook='deviation_link']")
    deviation_link: str = Field(default="//a[@data-hook='deviation_link']/@href")

    author: str = Field(default="/html/body/div[1]/main/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/a",
                        alias="author_xpath")
    image_title: str = Field(default="//html/body/div[1]/main/div/div[2]/div/div[1]/div/div[2]/div[1]/h1/text()",
                             alias="image_title_xpath")
    image_tags: List[str] = Field(default="//html/body/div[1]/main/div/div[3]/div/div[3]/div/a/span/text()",
                                  alias="image_tags_xpath")
    image_description: str = Field(default="//html/body/div[1]/main/div/div[3]/div/div[4]/div/div/text()",
                                   alias="image_description_xpath")
    full_image_url: str = Field(default="/html/body/div[1]/main/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/img/@src")
    next_button: str = Field(default="/html/body/div[1]/div[1]/div/main/div[2]/div/div/div[3]/div/a")
    next_button_2: str = Field(default="/html/body/div[1]/div[1]/div/main/div[2]/div/div/div[3]/div/a[2]")

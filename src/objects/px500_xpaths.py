from typing import List

from pydantic import Field, BaseModel as BaseSchema


class PX500XPaths(BaseSchema):
    picture: str = Field(default="//html/body/div[1]/div[5]/div/div/div/div/div[1]/div/div[1]/a",
                         alias="picture_xpath")
    author: str = Field(
        default="//html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div/p/span/a/text()",
        alias="author_xpath")
    image_title: str = Field(default="//html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/h3/text()",
                             alias="image_title_xpath")
    image_tags: List[str] = Field(
        default="//html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[8]/div/a/div/p/text()",
        alias="image_tags_xpath")
    next_urls: str = Field(default="",
                           alias="suggested_collections_xpath")


class PX500AuthorizationXPaths(BaseSchema):
    login: str = Field(default="/html/body/div/div[3]/div/form/div[1]/input",
                       alias="login_xpath")
    password: str = Field(default="/html/body/div/div[3]/div/form/div[2]/input",
                          alias="password_xpath")
    log_in_button: str = Field(default="/html/body/div/div[3]/div/form/button",
                               alias="password_xpath")

from typing import List

from pydantic import Field, BaseModel as BaseSchema


class PX500XPaths(BaseSchema):
    # Нормальные икс пути не сделать
    site_name: str = Field(default="500PX")
    picture_profile: str = Field(default="//a[@role='link']")
    category: str = Field(default="/html/body/div/div[4]/div/div/div[1]/div/div[3]/div[6]/div/a/p/span/text()")
    author: str = Field(default="/html/body/div/div[4]/div/div/div[1]/div/div[2]/div[2]/div/p/span/a/text()")
    image_title: str = Field(default="/html/body/div/div[4]/div/div/div[1]/div/div[2]/div[2]/div/p/span/a/text()")
    image_tags: List[str] = Field(default="/html/body/div/div[4]/div/div/div[1]/div/div[3]/div[7]/div/a[1]/div/p/text()")
    image_description: str = Field(default="/html/body/div/div[4]/div/div/div[1]/div/div[3]/div[2]/p/text()")
    full_image_url: str = Field(default="/html/body/div/div[3]/div/img/@src")


class PX500AuthorizationXPaths(BaseSchema):
    login: str = Field(default="/html/body/div/div[3]/div/form/div[1]/input",
                       alias="login_xpath")
    password: str = Field(default="/html/body/div/div[3]/div/form/div[2]/input",
                          alias="password_xpath")
    log_in_button: str = Field(default="/html/body/div/div[3]/div/form/button",
                               alias="password_xpath")

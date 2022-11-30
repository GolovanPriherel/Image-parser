from typing import List

from pydantic import Field, BaseModel as BaseSchema


class ProxyXpath(BaseSchema):
    proxy_info: str = Field(default="/html/body/section[1]/div/div[2]/div/table/tbody/tr/td[1]/text()")
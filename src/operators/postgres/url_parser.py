import logging
from typing import List
import json

import requests
import sqlalchemy_mixins.session

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.rule34_images_info import Rule34ImagesInfoModel, Rule34ImagesInfoSchema
from src.settings import parser_settings


class URLParserOperator:
    def __init__(self, url):
        self.url = url

    def execute(self, urls: List[str]):
        try:
            self.processing(urls)
        except Exception as e:
            raise Exception(e)

    def processing(self, urls: List[str]):
        print(self.url)
        print(urls)
        requests.post(f"http://{self.url}:5001/insert_urls", data=json.dumps({"data": urls}))

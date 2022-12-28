import logging
from typing import List
import json

import requests
import sqlalchemy_mixins.session

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.rule34_images_info import Rule34ImagesInfoModel, Rule34ImagesInfoSchema, Rule34ImagesInfoListSchema
from src.settings import parser_settings


class Rule34SendData:
    def __init__(self, url):
        self.images_info_table = Rule34ImagesInfoModel
        self.url = url
        self._data = []

    def execute(self, data: List[Rule34ImagesInfoSchema]):
        self._data = data
        print(self._data)
        with get_pg_session() as pg_session:
            try:
                self.processing()
                pg_session.commit()
            except Exception as e:
                raise Exception(e)

    def processing(self):
        requests.post(f"http://{self.url}:5001/insert_data", data={"data": self._data})

import logging
from typing import List
import json

import requests
import sqlalchemy_mixins.session

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.rule34_images_info import Rule34ImagesInfoSchema, Rule34ImagesInfoListSchema


class Rule34SendData:
    def __init__(self, url):
        self.url = url
        self._data = []

    def execute(self, data: Rule34ImagesInfoSchema):
        self._data = data
        with get_pg_session() as pg_session:
            try:
                self.processing()
                pg_session.commit()
            except Exception as e:
                raise Exception(e)

    def processing(self):
        data1 = {"data": self._data}
        data1 = Rule34ImagesInfoListSchema.parse_obj(data1)
        requests.post(f"http://localhost:5001/insert_data", json=data1.dict())

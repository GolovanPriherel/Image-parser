import logging
from typing import List

import requests

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.rule34_images_info import Rule34ImagesInfoModel, Rule34ImagesInfoSchema


class Rule34InsertImagesInfo:
    def __init__(self):
        self.images_info_table = Rule34ImagesInfoModel.__table__
        self._data = []

    def execute(self, data: List[Rule34ImagesInfoSchema]):
        self._data = data
        try:
            self.processing()
        except Exception as e:
            raise Exception(e)

    def processing(self):
        # for element in self._data:
        requests.post("parser_backend_service:5001/insert_data", json=self._data)

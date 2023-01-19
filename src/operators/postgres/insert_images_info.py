import logging
from typing import List

import requests

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.images_info_model import ImagesInfoModel, ImagesInfoSchema
from src.models.postgres.rule34_images_info import Rule34ImagesInfoSchema


class InsertImagesInfo:
    def __init__(self):
        self.images_info_table = ImagesInfoModel.__table__
        self._data = []

    def execute(self, data: List[ImagesInfoSchema]):
        self._data = data
        try:
            self.processing()
        except Exception as e:
            raise Exception(e)

    def processing(self):
        requests.post("localhost:5001/insert_data", json=self._data)

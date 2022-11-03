import logging
from typing import List

import requests
from src.models.postgres.base_model import get_pg_session
from src.models.postgres.images_info_model import ImagesInfoModel, ImagesInfoSchema


class SendImagesInfo:
    def __init__(self):
        self.images_info_table = ImagesInfoModel.__table__

    def execute(self, data: List[ImagesInfoSchema]):
        self.data = data
        try:
            self.processing()
        except Exception as e:
            raise Exception(e)

    def processing(self):
        payload = []
        for element in self.data:
            # logging.warning(element)
            payload.append(dict(element))

        # TODO разобраться с датой (Object of type datetime is not JSON serializable)

        logging.warning(payload)

        request = requests.post("http://0.0.0.0:5001/insert_data", json=payload)

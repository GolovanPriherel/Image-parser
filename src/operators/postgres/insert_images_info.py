import logging
from typing import List

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.images_info_model import ImagesInfoModel, ImagesInfoSchema


class InsertImagesInfo:
    def __init__(self):
        self.images_info_table = ImagesInfoModel.__table__

    def execute(self, data: List[ImagesInfoSchema]):
        self.data = data
        self.pg_session = get_pg_session()

        try:
            self.processing()
            self.pg_session.commit()
        except Exception as e:
            raise Exception(e)
        finally:
            self.pg_session.close()

    def processing(self):
        for element in self.data:
            logging.warning(element)
            element = dict(element)
            self.pg_session.execute(
                self.images_info_table.insert().values(element)
            )
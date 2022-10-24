from typing import List

from sqlalchemy import select, func

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.images_info_model import ImagesInfoModel, ImagesInfoSchema


class InsertImagesInfo:
    def __init__(self, data: List[ImagesInfoSchema]):
        self.images_info_table = ImagesInfoModel.__table__

    def execute(self):
        self.pg_session = get_pg_session()

        try:
            self.processing()
            self.pg_session.commit()
        except Exception as e:
            raise Exception(e)
        finally:
            self.pg_session.close()

    def processing(self):
        query = select(
            func.max(ImagesInfoModel.id)
        )

        images_ids = self.pg_session.execute(query)



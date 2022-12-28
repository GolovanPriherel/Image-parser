import logging

import pydantic


def test_rule34_send_data():
    from sqlalchemy import select, tuple_, update

    from src.models.postgres.base_model import get_pg_session
    from src.operators.postgres.rule34_insert_images_info import Rule34SendData
    from src.models.postgres.rule34_images_info import Rule34ImagesInfoModel, Rule34ImagesInfoSchema, Rule34ImagesInfoListSchema
    from src.settings.test_settings import TestSettings

    test_settings = TestSettings()

    rule34_send_data = Rule34SendData(test_settings.test_url)

    data_list = []
    test_url = "test_url"

    for i in range(5):
        data = Rule34ImagesInfoSchema().dict()
        data["image_url"] = test_url
        # data = Rule34ImagesInfoSchema.parse_obj(data)
        data_list.append(data)

    payload = {"data": data_list}
    payload = Rule34ImagesInfoListSchema.parse_obj(payload)

    rule34_send_data.execute(payload)

    with get_pg_session() as pg_session:
        query = select(
            Rule34ImagesInfoModel.image_url
        ).where(
            Rule34ImagesInfoModel.image_url.like(test_url)
        )

        table_data = pg_session.execute(query).fetchall()
        print(table_data)

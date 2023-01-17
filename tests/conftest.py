import os

import pytest
from pytest_postgresql import factories

schema_files = ["migrations/airflow.sql", "migrations/schema.sql"]
db_conn = factories.postgresql("postgresql_noproc", load=schema_files)


def db_url(db_info):
    return f"postgresql+psycopg2://{db_info.user}:{db_info.password}@{db_info.host}:{db_info.port}/{db_info.dbname}"


@pytest.fixture(scope="session", autouse=True)
def set_sql_alchemy_conn(request, session_mocker):
    db_info = request.getfixturevalue("postgresql_noproc")

    session_mocker.patch.dict(
        os.environ,
        {"AIRFLOW__CORE__SQL_ALCHEMY_CONN": db_url(db_info)},
    )
    session_mocker.patch.dict(
        os.environ,
        {"CH_HOST": 'localhost',
         "CH_PORT": '5432',
         "CH_DATABASE": 'postgres',
         "CH_USERNAME": 'postgres',
         "CH_PASSWORD": 'postgres'},
    )
    session_mocker.patch.dict(
        os.environ,
        {"TEST_CASE": "true"},
    )

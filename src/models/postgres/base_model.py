from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres/images_info', echo=True, future=True)
metadata = MetaData(bind=engine)
Base = declarative_base(bind=engine)


def get_pg_session():
    pg_session = Session(
        bind=engine,
        autocommit=False,
    )

    return pg_session

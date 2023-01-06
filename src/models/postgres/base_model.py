from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, scoped_session, sessionmaker
from sqlalchemy_mixins import AllFeaturesMixin

from src.settings import pg_settings

Base = declarative_base()


class BaseModel(Base, AllFeaturesMixin):

    __abstract__ = True
    pass


@contextmanager
def get_pg_session():
    pg_session = Session(
        bind=create_engine(pg_settings.geturl(), echo=True, future=True),
        autocommit=False,
    )
    try:
        yield pg_session
    finally:
        pg_session.close()


def set_session():
    engine = create_engine(pg_settings.geturl(), echo=True, future=True)
    db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
    BaseModel.set_session(db_session)
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)

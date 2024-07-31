from contextlib import contextmanager
from sqlalchemy import create_engine
from settings.env_settings import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

engine = create_engine(
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

session_local = sessionmaker(bind=engine)

SqlAlchemyBaseEntity = declarative_base()


@contextmanager
def get_session():
    session = session_local()
    try:
        yield session
    except IntegrityError as e:
        session.rollback()
        raise e
    finally:
        session.close()
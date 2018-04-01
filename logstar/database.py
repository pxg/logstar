import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def _get_database_url():
    return os.environ.get('LOGSTAR_DB_URL', False)


def get_database_url():
    """
    Get the database URL. Show error message and exit if not set
    """
    database_url = _get_database_url()
    if database_url is False:
        sys.exit('LOGSTAR_DB_URL environment vairable is not set')
    return database_url


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from logstar.models import Request

    Base.metadata.create_all(bind=engine)


engine = create_engine(get_database_url(), convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

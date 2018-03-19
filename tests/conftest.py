import pytest
import sqlalchemy

from logstar import engine, Session, create_tables
from logstar.models import Request


@pytest.fixture(autouse=True, scope='session')
def recreate_tables():
    """
    Drop and create tables for a clean test run
    https://groups.google.com/forum/#!topic/sqlalchemy/UQUYpF3Wu3E
    """
    meta = sqlalchemy.MetaData(engine)
    meta.reflect()
    meta.drop_all()
    create_tables()


@pytest.fixture(autouse=True)
def empty_requests_table():
    session = Session()
    session.query(Request).delete()
    session.commit()

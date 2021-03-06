import subprocess
from time import sleep

import pytest
import sqlalchemy

from logstar.app import create_app
from logstar.database import db_session, engine, init_db
from logstar.models import Request


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture(autouse=True, scope='session')
def recreate_tables():
    """
    Drop and create tables for a clean test run
    https://groups.google.com/forum/#!topic/sqlalchemy/UQUYpF3Wu3E
    """
    meta = sqlalchemy.MetaData(engine)
    meta.reflect()
    meta.drop_all()
    init_db()


@pytest.fixture(autouse=True, scope='session')
def httpbin(request):
    """
    Start httpbin on http://127.0.0.1:8000/ so we can run fast tests which
    require http requests to an external server
    Adds about a second to test runs
    """
    p = subprocess.Popen(['gunicorn', 'httpbin:app'])
    sleep(1)  # Required to give gunicorn time to start-up
    yield

    p.kill()


@pytest.fixture(autouse=True)
def empty_requests_table():
    session = db_session()
    session.query(Request).delete()
    session.commit()


@pytest.fixture
def http_request():
    http_request = Request(
        method='GET', response_content='amazing content', url='http://petegraham.co.uk'
    )
    session = db_session()
    session.add(http_request)
    session.commit()
    return http_request

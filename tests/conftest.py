import pytest

from logstar import Session
from logstar.models import Request


@pytest.fixture(autouse=True)
def empty_requests_table():
    session = Session()
    session.query(Request).delete()
    session.commit()

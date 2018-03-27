import requests

from .db import engine
from .logger import get_and_log, post_and_log
from .models import Base


def create_tables():
    Base.metadata.create_all(engine)


def install():
    """
    Check the database connection by creating the tables
    """
    create_tables()


def test_request():
    """
    Swtich logstar on and make a test request to make sure everthing is working
    correctly
    """
    logstar_on()
    requests.get('http://httpbin.org/')


def logstar_on():
    """
    Switch logstar on so it's logs request and response data by monkey patching
    the requests get and post functions
    """
    requests.get = get_and_log
    requests.post = post_and_log

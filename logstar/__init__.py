import requests

from .db import engine
from .logger import get_and_log, post_and_log
from .models import Base


def create_tables():
    Base.metadata.create_all(engine)


def logstar_on():
    """
    Switch logstar on so it's logs request and response data by monkey patching
    the requests get and post functions
    """
    requests.get = get_and_log
    requests.post = post_and_log


# TODO: move this to a initial configuration command which has to be invoked
# exlicitly
create_tables()

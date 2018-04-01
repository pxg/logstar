import requests

from .logger import get_and_log, post_and_log


def get_pagination_num():
    """
    """
    pass


def test_request():
    """
    Swtich logstar on and make a test request to make sure everthing is working
    correctly
    """
    logstar_on()
    requests.get('http://petegraham.co.uk/')


def logstar_on():
    """
    Switch logstar on so it's logs request and response data by monkey patching
    the requests get and post functions
    """
    requests.get = get_and_log
    requests.post = post_and_log

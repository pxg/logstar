import os
import requests

from .logger import (
    delete_and_log, get_and_log, patch_and_log, post_and_log, put_and_log
)


def get_pagination_num():
    """
    Get the pagination number of the number of requests we limit each API call
    to
    """
    return os.environ.get('LOGSTAR_PAGINATION_NUMBER', 10)


def test_request():
    """
    Switch logstar on and make a test request to make sure everthing is working
    correctly
    """
    logstar_on()
    requests.post('https://httpbin.org/status/500')
    # requests.get('http://petegraham.co.uk/')


def logstar_on():
    """
    Switch logstar on so it's logs request and response data by monkey patching
    the requests get and post functions
    """
    requests.delete = delete_and_log
    requests.get = get_and_log
    requests.patch = patch_and_log
    requests.post = post_and_log
    requests.put = put_and_log

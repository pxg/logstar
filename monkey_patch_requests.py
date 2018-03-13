import requests
from pprint import pprint


old_boring_get = requests.get


def get_and_log(*args, **kwargs):
    """
    """
    response = old_boring_get(*args, **kwargs)
    print('log here')
    return response


requests.get = get_and_log


response = requests.get('http://127.0.0.1:8000/user-agent')
pprint(response)

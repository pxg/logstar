import requests
from weather import Weather


def call_api_get():
    """
    Simple get call with requests to a URL
    """
    requests.get(
        'http://127.0.0.1:8000/user-agent?name=pete',
        data={'key': 'value'})


def call_api_get_headers():
    """
    Simple get call with requests to a URL with headers
    """
    requests.get(
        'http://127.0.0.1:8000/user-agent?name=pete',
        data={'key': 'value'},
        headers={'user-agent': 'my-app/0.0.1'})


# TODO: call_api_get_data


def call_api_post():
    """
    Simple post call with requests to a URL with headers
    """
    requests.post(
        'http://127.0.0.1:8000/user-agent?name=pete',
        data={'key': 'value'})


def call_external_lib():
    """
    Call external API to text monkey patching
    """
    weather = Weather()
    lookup = weather.lookup(560743)
    condition = lookup.condition()
    print(condition.text())

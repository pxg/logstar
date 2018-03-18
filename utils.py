import requests


def call_api():
    requests.post(
        'http://127.0.0.1:8000/user-agent?name=pete',
        data={'key': 'value'},
        headers={'user-agent': 'my-app/0.0.1'})

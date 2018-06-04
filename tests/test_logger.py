import datetime
import requests
from decimal import Decimal

import pytest
from weather import Weather

from logstar import logstar_on
from logstar.models import get_all_requests


def test_api_call_get_logs_request():
    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent?name=pete')

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert request_items[0].url == 'http://127.0.0.1:8000/user-agent?name=pete'
    assert request_items[0].method == 'GET'
    assert request_items[
        0
    ].response_content == '{\n  "user-agent": "python-requests/2.18.4"\n}\n'
    assert request_items[0].response_status_code == 200
    assert type(request_items[0].created_at) == datetime.datetime
    assert request_items[0].headers is None
    assert request_items[0].payload is None
    assert "'Server': 'gunicorn/19.7.1'" in request_items[0].response_headers
    assert type(request_items[0].time) == Decimal


def test_api_call_post_logs_request():
    logstar_on()
    requests.post('http://127.0.0.1:8000/user-agent?name=pete')

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert request_items[0].url == 'http://127.0.0.1:8000/user-agent?name=pete'
    assert request_items[0].method == 'POST'
    assert '<h1>Method Not Allowed</h1>' in request_items[0].response_content
    assert request_items[0].response_status_code == 405
    assert type(request_items[0].created_at) == datetime.datetime


def test_api_call_put_logs_request():
    logstar_on()
    requests.put('http://127.0.0.1:8000/user-agent?name=pete')

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert request_items[0].method == 'PUT'


# def test_api_call_delete_logs_request():
#     logstar_on()
#     requests.delete('http://127.0.0.1:8000/user-agent?name=pete')

#     request_items = get_all_requests()
#     assert len(request_items) == 1
#     assert request_items[0].method == 'DELETE'


@pytest.mark.webtest
def test_api_call_external_library_get_logs_requests():
    logstar_on()
    weather = Weather()
    lookup = weather.lookup(560743)
    lookup.condition()

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert 'http://query.yahooapis.com/v1/public/yql?q=select' in request_items[0].url
    assert request_items[0].method == 'GET'
    assert 'Full Forecast at Yahoo! Weather' in request_items[0].response_content
    assert request_items[0].response_status_code == 200
    assert type(request_items[0].created_at) == datetime.datetime


def test_call_api_get_with_headers():
    logstar_on()
    requests.get(
        'http://127.0.0.1:8000/user-agent', headers={'user-agent': 'my-app/0.0.1'}
    )

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert request_items[0].headers == "{'user-agent': 'my-app/0.0.1'}"


def test_call_api_post_with_payload():
    """
    Simple post call with requests to a URL with headers
    """
    logstar_on()
    requests.post('http://127.0.0.1:8000/post', data={'key': 'value'})

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert request_items[0].payload == "{'key': 'value'}"

import json

import requests
from flask import url_for

from conftest import http_request
from logstar import logstar_on
from logstar.models import get_highest_request_id


def test_api_returns_200_ok(client):
    assert client.get(url_for('api_requests')).status_code == 200


def test_api_returns_json(client):
    response = client.get(url_for('api_requests'))

    # Raises an exception if not json
    json.loads(response.data)


def test_api_no_request_returns_empy_list(client):
    response = client.get(url_for('api_requests'))

    assert response.json == []


def test_api_request_returns_one_item(client):
    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent?name=pete')

    response = client.get(url_for('api_requests'))

    assert len(response.json) == 1


def test_api_request_returns_request_data(client):
    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent?name=asdf')

    response = client.get(url_for('api_requests'))

    assert response.json[0]['url'] == 'http://127.0.0.1:8000/user-agent?name=asdf'


def test_api_request_ordered_newest_first(client):
    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent?name=first')
    requests.get('http://127.0.0.1:8000/user-agent?name=second')

    response = client.get(url_for('api_requests'))

    assert response.json[0]['id'] > response.json[1]['id']


def test_api_no_items_higher_than_id(client):
    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent')
    request_id = get_highest_request_id()

    response = client.get(url_for('api_requests', above_id=request_id))

    assert response.json == []


def test_api_get_requests_newer_than_id(client):
    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent')
    request_id = get_highest_request_id()
    requests.get('http://127.0.0.1:8000/user-agent')

    response = client.get(url_for('api_requests', above_id=request_id))

    assert len(response.json) == 1
    assert response.json[0]['id'] == request_id + 1


def test_api_gets_requets_older_than_id(client):
    logstar_on()
    http_request()
    http_request()
    highest_id = http_request().id

    response = client.get(url_for('api_requests', below_id=highest_id))

    assert len(response.json) == 2
    # Check below highest ID
    assert response.json[0]['id'] < highest_id
    # Check ordering
    assert response.json[0]['id'] > response.json[1]['id']


def test_api_pagination_limit(client):
    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent?name=first')
    requests.get('http://127.0.0.1:8000/user-agent?name=second')
    requests.get('http://127.0.0.1:8000/user-agent?name=third')

    response = client.get(url_for('api_requests'))

    assert len(response.json) == 2
    assert response.json[0]['url'] == 'http://127.0.0.1:8000/user-agent?name=third'

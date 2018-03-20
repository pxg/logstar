import json

import pytest
import requests
from flask import url_for

from logstar import logstar_on


def test_api_returns_200_ok(client):
    assert client.get(url_for('api_requests')).status_code == 200


def test_api_returns_json(client):
    response = client.get(url_for('api_requests'))

    # Raises an exception if not json
    json.loads(response.data)


def test_api_no_request_returns_empy_list(client):
    response = client.get(url_for('api_requests'))

    assert response.json == []


@pytest.mark.xfail
def test_api_request_returns_one_item(client):
    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent?name=pete')

    response = client.get(url_for('api_requests'))

    assert len(response.json) == 1

# TOOD: Test actual data returned

# TODO: Test ordering

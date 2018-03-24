from flask import url_for


def test_home_return_200_ok(client):
    assert client.get(url_for('home')).status_code == 200


def test_home_returns_html(client):
    response = client.get(url_for('home'))

    assert '<h1>LogStar</h1>' in str(response.data)


def test_request_page_return_200_ok(client, http_request):
    response = client.get(url_for('request', request_id=http_request.id))

    assert response.status_code == 200


def test_request_page_returns_404_for_non_existent_request(client):
    assert client.get(url_for('request', request_id=999)).status_code == 404


def test_request_page_returns_data_about_request(client, http_request):
    response = client.get(url_for('request', request_id=http_request.id))

    assert http_request.response_content in str(response.data)

from flask import url_for


def test_home_return_200_ok(client):
    assert client.get(url_for('home')).status_code == 200


def test_home_returns_html(client):
    response = client.get(url_for('home'))

    assert '<h1>LogStar</h1>' in str(response.data)

import requests
from logstar import empty_requests_table, get_all_requests, logstar_on
from weather import Weather


def test_logstar_api_call_get_logs_request():
    # TODO: can I use a fixture to wipe the DB so tests are cleaner?
    empty_requests_table()

    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent?name=pete')

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert request_items[0].url == 'http://127.0.0.1:8000/user-agent?name=pete'
    assert request_items[0].method == 'GET'
    assert request_items[0].response_content == \
        '{\n  "user-agent": "python-requests/2.18.4"\n}\n'
    assert request_items[0].response_status_code == 200
    # assert rows[0]['response_time'] # Use freezegun?


def test_logstar_api_call_post_logs_request():
    empty_requests_table()

    logstar_on()
    requests.post('http://127.0.0.1:8000/user-agent?name=pete')

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert request_items[0].url == 'http://127.0.0.1:8000/user-agent?name=pete'
    assert request_items[0].method == 'POST'
    assert '<h1>Method Not Allowed</h1>' in request_items[0].response_content
    assert request_items[0].response_status_code == 405
    # assert rows[0]['response_time'] # Use freezegun?


# TODO: mark this test as it calls an external URL
def test_logstar_external_library_logs_requests():
    empty_requests_table()

    logstar_on()
    weather = Weather()
    lookup = weather.lookup(560743)
    lookup.condition()

    request_items = get_all_requests()
    assert len(request_items) == 1
    assert 'http://query.yahooapis.com/v1/public/yql?q=select' in \
        request_items[0].url
    assert request_items[0].method == 'GET'
    assert 'Full Forecast at Yahoo! Weather' in \
        request_items[0].response_content
    assert request_items[0].response_status_code == 200


# def call_api_get_headers():
#     """
#     Simple get call with requests to a URL with headers
#     """
#     requests.get(
#         'http://127.0.0.1:8000/user-agent?name=pete',
#         data={'key': 'value'},
#         headers={'user-agent': 'my-app/0.0.1'})


# def call_api_post():
#     """
#     Simple post call with requests to a URL with headers
#     """
#     requests.post(
#         'http://127.0.0.1:8000/user-agent?name=pete',
#         data={'key': 'value'})

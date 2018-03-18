import mock
import requests
from logstar import logstar_on
from weather import Weather


def test_logstar_api_call_get_logs_request():
    with mock.patch('logstar.log_request') as mocked_method:
        # Note due to how monkey patching works once it's called the library
        # remains monkey patched
        logstar_on()
        requests.get('http://127.0.0.1:8000/user-agent?name=pete')

        mocked_method.assert_called()


def test_logstar_api_call_get_logs_response():
    with mock.patch('logstar.log_response') as mocked_method:

        logstar_on()
        requests.get('http://127.0.0.1:8000/user-agent?name=pete')

        mocked_method.assert_called()


# TODO: mark this test as it calls an external URL
def test_logstar_external_library_logs_requests():
    with mock.patch('logstar.log_request') as mocked_method:

        logstar_on()
        weather = Weather()
        lookup = weather.lookup(560743)
        lookup.condition()

        mocked_method.assert_called()

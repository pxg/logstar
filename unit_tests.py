# TODO: move to test directory when proejct has been set-up as a python package
import mock
from monkey_patch import monkey_patch_requests
from utils import call_api_get, call_external_lib


def test_call_api_get_logs_no_request():
    with mock.patch('monkey_patch.log_request') as mocked_method:

        call_api_get()

        mocked_method.assert_not_called()


def test_call_api_get_logs_no_response():
    with mock.patch('monkey_patch.log_response') as mocked_method:

        call_api_get()

        mocked_method.assert_not_called()


def test_monkey_patch_api_call_get_logs_request():
    with mock.patch('monkey_patch.log_request') as mocked_method:

        # Note due to how monkey patching works once it's called the library
        # remains monkey patched
        monkey_patch_requests()
        call_api_get()

        mocked_method.assert_called()


def test_monkey_patch_api_call_get_logs_response():
    with mock.patch('monkey_patch.log_response') as mocked_method:

        monkey_patch_requests()
        call_api_get()

        mocked_method.assert_called()


# TODO: mark this test as it calls an external URL
def test_external_library_logs_requests():
    with mock.patch('monkey_patch.log_request') as mocked_method:

        monkey_patch_requests()
        call_external_lib()

        mocked_method.assert_called()

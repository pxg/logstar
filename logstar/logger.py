import requests

from .database import db_session
from .models import Request

# For Monkey Patching
old_boring_delete = requests.delete
old_boring_get = requests.get
old_boring_patch = requests.patch
old_boring_post = requests.post
old_boring_put = requests.put


def delete_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests get function
    """
    request_instance = log_request('DELETE', *args, **kwargs)
    session = db_session()
    session.add(request_instance)
    session.commit()

    response = old_boring_delete(*args, **kwargs)

    log_response(request_instance, response)
    session.commit()
    return response


def get_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests get function
    """
    request_instance = log_request('GET', *args, **kwargs)
    session = db_session()
    session.add(request_instance)
    session.commit()

    response = old_boring_get(*args, **kwargs)

    log_response(request_instance, response)
    session.commit()
    return response


def patch_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests patch function
    """
    request_instance = log_request('PATCH', *args, **kwargs)
    session = db_session()
    session.add(request_instance)
    session.commit()

    response = old_boring_patch(*args, **kwargs)

    log_response(request_instance, response)
    session.commit()
    return response


def post_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests post function
    """
    request_instance = log_request('POST', *args, **kwargs)
    session = db_session()
    session.add(request_instance)
    session.commit()

    response = old_boring_post(*args, **kwargs)

    log_response(request_instance, response)
    session.commit()
    return response


def put_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests put function
    """
    request_instance = log_request('PUT', *args, **kwargs)
    session = db_session()
    session.add(request_instance)
    session.commit()

    response = old_boring_put(*args, **kwargs)

    log_response(request_instance, response)
    session.commit()
    return response


def log_request(method, *args, **kwargs):
    """
    Log the details of the requests
    """
    payload = kwargs.get('data')
    if payload is not None:
        payload = str(payload)

    headers = kwargs.get('headers')
    if headers is not None:
        headers = str(headers)

    request_instance = Request(
        headers=headers, method=method, payload=payload, url=args[0]
    )
    return request_instance


def log_response(request_instance, response):
    """
    Log the details of the response
    """
    request_instance.response_content = response.text
    request_instance.response_status_code = response.status_code
    request_instance.response_headers = str(response.headers)
    request_instance.time = response.elapsed.total_seconds()

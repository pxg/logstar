from .models import Request


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
        headers=headers,
        method=method,
        payload=payload,
        url=args[0])
    return request_instance


def log_response(request_instance, response):
    """
    Log the details of the response
    """
    request_instance.response_content = response.text
    request_instance.response_status_code = response.status_code
    request_instance.response_headers = str(response.headers)
    request_instance.time = response.elapsed.total_seconds()

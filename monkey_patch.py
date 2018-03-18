import requests
old_boring_post = requests.post


def monkey_patch_requests():
    """
    Patch the requests post function
    """
    requests.post = post_and_log


def post_and_log(*args, **kwargs):
    """
    Save request and response data and call original requests get
    """
    log_request(*args, **kwargs)
    # should be post
    response = old_boring_post(*args, **kwargs)
    log_response(response)
    return response


# NOTE: when I add test seperate getting the values from writing the values to
# the database
# TODO: add method as a parameter
def log_request(*args, **kwargs):
    """
    Log the details of the requests to Postgres
    """
    print('Request url: {}'.format(args[0]))  # could use r.url instead?
    print('Request method: POST')
    print('Request headers: {}'.format(kwargs['headers']))
    print('Request data: {}'.format(kwargs['data']))


def log_response(response):
    """
    Log the details of the response to Postgres
    """
    print('Response status code: {}'.format(response.status_code))
    # Could try and get JSON here
    print('Response data: {}'.format(response.text))
    print('Response time: {}'.format(response.elapsed.total_seconds()))
    print('Response headers: {}'.format(response.headers))

import os
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, Request
# For Monky Patching
old_boring_post = requests.post
old_boring_get = requests.get


def create_tables():
    Base.metadata.create_all(engine)

# SQLAlchemy configuration
engine = create_engine(os.environ.get('LOGSTAR_DB_URL'))
Session = sessionmaker(bind=engine)
# TODO: move this to a initial configuration command?
create_tables()


def logstar_on():
    """
    Switch logstar on so it's logs request and response data
    Monkey patch the requests get and post functions
    """
    requests.get = get_and_log
    requests.post = post_and_log


def get_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests get function
    """
    request_instance = log_request('GET', *args, **kwargs)
    session = Session()
    session.add(request_instance)
    session.commit()

    response = old_boring_get(*args, **kwargs)

    log_response(request_instance, response)
    session.commit()
    return response


def post_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests post function
    """
    request_instance = log_request('POST', *args, **kwargs)
    session = Session()
    session.add(request_instance)
    session.commit()

    response = old_boring_post(*args, **kwargs)

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
    # TODO: save time response.elapsed.total_seconds()))

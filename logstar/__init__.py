import requests
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
old_boring_post = requests.post
old_boring_get = requests.get


# TOOD: find nicer plan to put this code
# TODO: pick up credentials from envvar
engine = create_engine('postgresql://petegraham@localhost/logstar')
metadata = MetaData()
requests_table = Table(
    'requests', metadata,
    Column('id', Integer, primary_key=True),
    Column('url', String),
    Column('method', String),
    # Column('headers', String),  # Should be JSON?
    # Column('data', String),  # Should be JSON?
    # TODO: add created_at time stamp
)
metadata.create_all(engine)


def logstar_on():
    """
    Switch logstar on so it's logs request and response data
    """
    # Monkey patch the requests get and post functions
    requests.get = get_and_log
    requests.post = post_and_log


def get_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests get function
    """
    log_request('GET', *args, **kwargs)
    response = old_boring_get(*args, **kwargs)
    log_response(response)
    return response


def post_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests post function
    """
    log_request('POST', *args, **kwargs)
    response = old_boring_post(*args, **kwargs)
    log_response(response)
    return response


def log_request(method, *args, **kwargs):
    """
    Log the details of the requests
    """
    # print('Request url: {}'.format(args[0]))  # could use r.url instead?
    # print('Request method: {}'.format(method))
    # print('Request headers: {}'.format(kwargs.get('headers')))
    # print('Request data: {}'.format(kwargs.get('data')))
    ins = requests_table.insert().values(
        url=args[0],
        method=method)
    conn = engine.connect()
    return conn.execute(ins)


def log_response(response):
    """
    Log the details of the response
    """
    # print('Response status code: {}'.format(response.status_code))
    # # TODO: see if response is JSON here
    # print('Response data: {}'.format(response.text))
    # print('Response time: {}'.format(response.elapsed.total_seconds()))
    # print('Response headers: {}'.format(response.headers))
    pass

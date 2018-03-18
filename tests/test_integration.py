import requests
from logstar import logstar_on
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from logstar import requests_table


# TODO: move to actual code
def get_conn():
    # TODO: allow optional setting to use test DB
    engine = create_engine('postgresql://petegraham@localhost/logstar')
    return engine.connect()


def empty_requests_table():
    get_conn().execute(requests_table.delete())


def requests_table_rows():
    s = select([requests_table])
    result = get_conn().execute(s)
    return [row for row in result]


def test_logstar_api_call_get_logs_request():
    # TODO: can I use a fixture to wipe the DB so tests are cleaner?
    empty_requests_table()

    logstar_on()
    requests.get('http://127.0.0.1:8000/user-agent?name=pete')

    assert len(requests_table_rows()) == 1
    # TODO: inspect the item to get the URL, status, data, response_time, etc

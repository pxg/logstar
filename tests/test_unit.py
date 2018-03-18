import os
from logstar import get_db_url


def test_db_url():
    # TODO: automatically run this for every test
    os.environ['LOGSTAR_DB_URL'] = \
        'postgresql://petegraham@localhost/logstar_test'
    assert get_db_url() == 'postgresql://petegraham@localhost/logstar_test'

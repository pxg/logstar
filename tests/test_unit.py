import os
import pytest
from logstar import get_db_url


@pytest.fixture(autouse=True)
def db_url():
    os.environ['LOGSTAR_DB_URL'] = \
        'postgresql://petegraham@localhost/logstar_test'


def test_db_url():
    assert get_db_url() == 'postgresql://petegraham@localhost/logstar_test'

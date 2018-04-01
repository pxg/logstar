import os


def test_db_url():
    assert os.environ.get(
        'LOGSTAR_DB_URL'
    ) == 'postgresql://petegraham@localhost/logstar_test'


def test_pagination_number():
    assert os.environ.get('LOGSTAR_PAGINATION_NUMBER') == '2'

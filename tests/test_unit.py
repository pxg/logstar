import os


def test_db_url():
    assert os.environ.get('LOGSTAR_DB_URL') == \
        'postgresql://petegraham@localhost/logstar_test'

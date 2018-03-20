# TODO: make imports relative
from logstar.models import Request
from logstar.db import Session

from flask import Flask
from flask import jsonify


# TODO: move me to serializers.py
# TODO: needs unit test
# TODO: do loop field and attempt to json serializer try catch
def serialize_request(r):
    """
    Format the request for return by the API
    """
    return {
        'id': r.id,
        'url': r.url,
        'method': r.method,
        'headers': r.headers,
        'payload': r.payload,
        'response_content': r.response_content,
        'response_status_code': r.response_status_code,
        'response_headers': r.response_headers,
        'time': str(r.time),  # Decimal TypeError: Object of type 'Decimal' is not JSON serializable
        'created_at': r.created_at,
    }


def create_app():
    """
    Based on https://www.python-boilerplate.com/py3+flask+pytest/
    Alternative structure http://pytest-flask.readthedocs.io/en/latest/features.html
    """
    app = Flask(__name__)

    @app.route('/')
    def api_requests():
        requests = Session().query(Request).all()
        return jsonify([serialize_request(r) for r in requests])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

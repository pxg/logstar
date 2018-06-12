import json
from flask import Flask
from flask import jsonify
from flask_cors import CORS

from . import get_pagination_num
from .database import db_session
from .models import Request


def serialize_request(r):
    """
    Format the request for return by the API
    TODO: needs unit test
    """
    # TODO: add json_content field and use property to decide which to return
    try:
        content = json.loads(r.response_content)
    except json.decoder.JSONDecodeError:
        content = r.response_content

    return {
        'id': r.id,
        'url': r.url,
        'method': r.method,
        'headers': r.headers,
        'payload': r.payload,
        'response_content': content,
        'response_status_code': r.response_status_code,
        'response_headers': r.response_headers,
        # Decimal TypeError: Object of type 'Decimal' is not JSON serializable
        'time': str(r.time),
        'created_at': r.created_at,
    }


def create_app():
    """
    Create app, configure and add routes and views
    """
    app = Flask(__name__)

    @app.route('/api/')
    @app.route('/api/above/<int:above_id>/')
    @app.route('/api/below/<int:below_id>/')
    def api_requests(above_id=None, below_id=None):
        requests = db_session().query(Request).order_by(Request.created_at.desc())
        if above_id is not None:
            requests = requests.filter(Request.id > above_id)
        elif below_id is not None:
            requests = requests.filter(Request.id < below_id)
        requests = requests.limit(get_pagination_num())
        return jsonify([serialize_request(r) for r in requests])

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        Needed to stop
        http://docs.sqlalchemy.org/en/latest/errors.html#connections-and-transactions
        Documentation on this technique
        http://flask.pocoo.org/docs/0.12/patterns/sqlalchemy/
        """
        db_session.remove()

    CORS(app)
    return app


# Needed here for Gunicorn
app = create_app()


def run_app():
    """
    Run the app threaded in debug mode for local development
    """
    app.debug = True
    app.run(threaded=True)

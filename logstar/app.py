from flask import abort, Flask
from flask import jsonify, render_template

from . import get_pagination_num
from .database import db_session
from .models import Request


def serialize_request(r):
    """
    Format the request for return by the API
    TODO: needs unit test
    TODO: do loop field and attempt to json serializer try catch
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
        # Decimal TypeError: Object of type 'Decimal' is not JSON serializable
        'time': str(r.time),
        'created_at': r.created_at,
    }


def create_app():
    """
    Create app, configure and add routes and views
    """
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/request/<int:request_id>/')
    def request(request_id):
        request = db_session().query(Request).get(request_id)
        if request is None:
            abort(404)
        return render_template('request.html', request=request)

    @app.route('/api/')
    @app.route('/api/<int:request_id>/')
    @app.route('/api/below/<int:below_id>/')
    def api_requests(request_id=None, below_id=None):
        # TODO: rename request_id to above_id
        requests = db_session().query(Request).order_by(Request.created_at.desc())
        if request_id is not None:
            requests = requests.filter(Request.id > request_id)
        if below_id is not None:
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

    return app


# Needed here for Gunicorn
app = create_app()


def run_app():
    """
    Run the app threaded in debug mode for local development
    """
    app.debug = True
    app.run(threaded=True)

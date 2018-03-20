from flask import Flask
from flask import jsonify


def create_app(config_filename=False):
    """
    Based on https://www.python-boilerplate.com/py3+flask+pytest/
    """
    app = Flask(__name__)

    @app.route('/')
    def api_requests():
        # Alternative method to return JSON
        # https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
        return jsonify([])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

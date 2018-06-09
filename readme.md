# LogStar

Tool to log and view metrics about external API requests.

## Installing the Logstar library

Install package from Github:
```
pip install -e git+https://github.com/pxg/logstar.git@master#egg=logstar
```

Create the database:
```
psql
create database logstar;
```

Set the follow environment variable:
```
export LOGSTAR_DB_URL='postgresql://petegraham@localhost/logstar'
```

Check your database connection and create your tables with:
```
logstar_install
```

Run the following command to make a request which should be logged to the DB:
```
logstar_test_request
```

You can test this has worked by looking directly in the requests table in the database, or alternatively you can run the webapp.

## Running the webapp
Run the API with:
```
gunicorn logstar.app:app -w 1 --threads 12 -b 0.0.0.0:8000
```
This will run the API on http://127.0.0.1:8000/ using Gunicorn.

Run the webapp with:
```
cd frontend
npm install -g serve
serve -s build
```
This will run the webapp on http://localhost:3000/.

## Developing the Logstar Python library
I recommend first creating a python3 virtual environment:
```
mkvirtualenv --python=`which python3` logstar
```

Then install requirements and the package:
```
pip install -r requirements.txt
pip install -e .
```

Create the databases:
```
psql
create database logstar;
create database logstar_test;
```

Set the follow environment variable:
```
export LOGSTAR_DB_URL='postgresql://petegraham@localhost/logstar'
```

Check your database connection and create your tables with:
```
logstar_install
```

Run the following command to make a request which should be logged to the DB:
```
logstar_test_request
```

For offline development you can run against a httpbin API:
```
gunicorn httpbin:app
```

## Running the Logstar Python library & API tests
```
py.test
```
The tests are configured to use a local DB called `logstar_test` the credentials are set in `pytest.ini`.

Running the tests automatically runs httpbin using gunicorn in the background.

To run the tests without connecting to external services run:
```
pytest -m "not webtest"
```

# Developing the webapp
```
cd frontend
npm install
npm start
```

# Building the webapp for production
```
npm run build
```
This will build the production webapp in `frontend/build/`.

# Developing the API
To run a development version of the API:
```
export FLASK_DEBUG=1
FLASK_APP=logstar/app.py flask run
```

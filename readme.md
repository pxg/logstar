# LogStar

Tool to log and view metrics about external API requests.

The motivation for this project is I wanted a non-intrusive way to log external (http) API requests in Python. I investigated solutions such as New Relic but I couldn't find an existing tool which would log all the request and response data I wanted to capture.

## Approach
I thought a clean way to capture http(s) requests would be by using the Python logging module. However this has the limitation that it doesn't show the data returned from the server # https://stackoverflow.com/questions/10588644/how-can-i-see-the-entire-http-request-thats-being-sent-by-my-python-application.

Other solutions:
- Monkey patch requests
- Use a proxy
- Use a packet logger, wireshark, etc
- Do something on the OS networking level
- Do something montioring networking between containers
- Do something on the AWS level

For the first version I've chosen to go with monkey patching the requests library, form experimenting I've found monkey patching the standard library is possible if required.

## Installation
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

# Webapp
There is a webapp which shows the requests Logstar is recording to run it:
```
gunicorn logstar.app:app -w 1 --threads 12
```

To run a development version of the webapp:
```
export FLASK_DEBUG=1
FLASK_APP=logstar/app.py flask run
```

## Running the tests
```
py.test
```
The tests are configured to use a local DB called `logstar_test` the credentials are set in `pytest.ini`.

Running the tests automatically runs httpbin using gunicorn in the background.

To run the tests without connecting to external services run:
```
pytest -m "not webtest"
```

## Production installation

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


Run the app on http://127.0.0.1:8000/ using Gunicorn:
```
gunicorn logstar.app:app -w 1 --threads 12
gunicorn logstar.app:app -w 1 --threads 12 -b 0.0.0.0:8000
```

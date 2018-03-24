# LogStar

Tool to log and view metrics about API requests.

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

Set the follow environment variable:
```
export LOGSTAR_DB_URL='postgresql://petegraham@localhost/logstar'
```

Create the databases:
```
psql
create database logstar;
create database logstar_test;
```

For offline development you can run against a httpbin API:
```
gunicorn httpbin:app
```

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

## Running the tests
First run httpbin as we require it to test against:
```
gunicorn httpbin:app
```

Next run:
```
py.test
```

To run the tests without connecting to external services run:
```
pytest -m "not webtest"
```

## Running the API
From the root of the repo:
```
export FLASK_DEBUG=1
python logstar/api.py
```

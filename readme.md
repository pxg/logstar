# LogStar

Tool to log and view metrics about API requests.

## Installation

For offline development you can run against a httpbin API:
```
gunicorn httpbin:app
```

## Approach

I thought a clean way to capture http(s) requests would be by using the Python logging module. However this has the limitation that it doesn't show the data returned from the server # https://stackoverflow.com/questions/10588644/how-can-i-see-the-entire-http-request-thats-being-sent-by-my-python-application.

Other solutions:
- Monkey patch requests
- Use a proxy
- Use a packet logger, wireshark, etc
- Do something on the OS networking level
- Do something montioring networking between containers
- Do something on the AWS level

For the first version I've chosen to go with monkey patching the requests library, form experimenting I've found monkey patching the standard library is possible if required.

## Running the tests

First run httpbin as we require it to test against:
```
gunicorn httpbin:app
```

Next run:
```
py.test unit_tests.py
```

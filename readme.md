# LogStar

Tool to log and view metrics about API requests.

## Installation

For offline development you can run agains a httpbin API:
```
gunicorn httpbin:app
```

## Aproach

I thought a clean way to capture http requests would be by using the Python logging module. However this has the limitation that it doesn't show the data returned from the server # https://stackoverflow.com/questions/10588644/how-can-i-see-the-entire-http-request-thats-being-sent-by-my-python-application.

Other solutions:
- Monkey patch requests
- Use a proxy
- Use a packet logger, wireshark, etc
- Do something on the OS networking level
- Do something montioring networking between containers
- Do something on the AWS level
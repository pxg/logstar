"""
Example of how to monkey patch urlib to get data about the request and response
"""
import urllib.request
import urllib.parse

old_boring_urlopen = urllib.request.urlopen


def urlopen_and_log(*args, **kwargs):
    """
    Log the request and response data and call the original function
    """
    print('Request url: {}'.format(args[0]))  # could use r.url instead?
    # print('Request method: {}'.format(f.method))
    # print('Request headers: {}'.format(kwargs.get('headers')))
    # print('Request data: {}'.format(kwargs.get('data')))
    f = old_boring_urlopen(*args, **kwargs)
    print('Response data: {}'.format(f.read().decode('utf-8')))
    print('Response status code: {}'.format(f.status))
    # print('Response data: {}'.format(response.decode('utf-8')))
    # print('Response time: {}'.format(response.elapsed.total_seconds()))
    # print('Response headers: {}'.format(response.headers))
    return f


urllib.request.urlopen = urlopen_and_log
# NOTE: SSL is a pain with urlib
# https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
# f = urllib.request.urlopen('https://httpbin.org/')
urllib.request.urlopen('http://127.0.0.1:8000/user-agent?name=pete')

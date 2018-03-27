"""
This simple script switches Logstar on. A request is then made with requests.
Request and response data for both API requests are logged by Logstar
"""
import requests
from random import randint
from logstar import logstar_on


logstar_on()
url = 'http://127.0.0.1:8000/user-agent?name={}'.format(randint(0, 1000))
requests.get(url, data={'key': 'value'})

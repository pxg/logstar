"""
This simple script swtiches Logstar on. A request is then made with requests
and an external python lib, weather, which uses requessts in it's underlying
code. Request and response data for both API requests are logged by Logstar
"""
import requests
from random import randint
from logstar import logstar_on
from weather import Weather


logstar_on()

# API call using requests
# TODO: add random value here
url = 'http://127.0.0.1:8000/user-agent?name={}'.format(randint(0, 1000))
requests.get(url, data={'key': 'value'})

# API call using external lib
# weather = Weather()
# lookup = weather.lookup(560743)
# condition = lookup.condition()

import requests
from logstar import logstar_on
from weather import Weather


logstar_on()

# API call using requests
requests.get(
    'http://127.0.0.1:8000/user-agent?name=pete',
    data={'key': 'value'})

# API call using extenral lib
weather = Weather()
lookup = weather.lookup(560743)
condition = lookup.condition()
print(condition.text())

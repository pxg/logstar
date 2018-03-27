"""
This simple script switches Logstar on. A request is then made with the
external library weather which uses requests behind the scene.
Request and response data for both API requests are logged by Logstar
"""
from logstar import logstar_on
from weather import Weather


logstar_on()
weather = Weather()
lookup = weather.lookup(560743)
condition = lookup.condition()

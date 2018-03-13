import logging
import requests
from pprint import pprint


# Configuration to Log network traffic
# logging.basicConfig(level=logging.DEBUG)
# http.client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# Custom logger for capturing this data
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)  # Not sure if this is needed again
requests_log.addHandler(fh)
logger.addHandler(fh)

# Make a request
response = requests.get('http://127.0.0.1:8000/user-agent')
pprint(response.json()['user-agent'])

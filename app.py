from monkey_patch import monkey_patch_requests
from utils import (
    call_api_get,
    call_api_get_headers,
    call_api_post,
    call_external_lib)


monkey_patch_requests()
# call_api_get()
# call_api_get_headers()
# call_api_post()
call_external_lib()

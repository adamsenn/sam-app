import os

CSOD_PORTAL = os.getenv('CSOD_PORTAL')
CSOD_OAUTH2_CLIENT_ID = os.getenv('CSOD_OAUTH2_CLIENT_ID')
CSOD_OAUTH2_CLIENT_SECRET = os.getenv('CSOD_OAUTH2_CLIENT_SECRET')

assert(CSOD_PORTAL)
assert(CSOD_OAUTH2_CLIENT_ID)
assert(CSOD_OAUTH2_CLIENT_SECRET)

# now build some helpful settings

CSOD_API_ROOT = f'https://{CSOD_PORTAL}.csod.com/services/api'
CSOD_OAUTH_ENDPOINT = f'{CSOD_API_ROOT}/oauth2/token'
DEFAULT_ODATA_PAGE_SIZE = os.getenv('DEFAULT_ODATA_PAGE_SIZE', 10000)

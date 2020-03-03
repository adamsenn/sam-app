import json
import logging
import requests

from config import settings


def get_token(endpoint: str = settings.CSOD_OAUTH_ENDPOINT,
              client_id: str = settings.CSOD_OAUTH2_CLIENT_ID,
              client_secret: str = settings.CSOD_OAUTH2_CLIENT_SECRET) -> str:
    # setup request
    body = json.dumps({
        'clientId': client_id,
        'clientSecret': client_secret,
        'grantType': 'client_credentials',
        'scope': 'all'
    })

    # POST to OAuth2 endpoint
    logging.debug('OAuth2 request to %s with %s and %s' %
                  (endpoint, client_id, client_secret[:13]))
    response = requests.post(endpoint, data=body)
    logging.debug('OAuth2 response %s' % response.content)

    # parse the response
    content = json.loads(response.content)
    token = content['access_token']

    logging.info('Successfully retrieved an auth token ({token}...) from {url}'.format(
        token=token[:13], url=endpoint))

    return token

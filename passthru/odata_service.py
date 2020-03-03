import logging
import json
import requests
import typing

from common.oauth2 import get_token
from config import settings


class ODataService(object):
    def __init__(self, bearer_token: str = None):
        if not bearer_token:
            bearer_token = get_token(endpoint=settings.CSOD_OAUTH_ENDPOINT,
                                     client_id=settings.CSOD_OAUTH2_CLIENT_ID,
                                     client_secret=settings.CSOD_OAUTH2_CLIENT_SECRET)

        self.bearer_token = bearer_token

    def get_pages_iterable(self, odata_url: str, page_size: int = settings.DEFAULT_ODATA_PAGE_SIZE) -> typing.Iterable[typing.List]:
        # setup variables for first page of data
        assert(odata_url)
        next_url = odata_url
        headers = {'Authorization': 'Bearer %s' % self.bearer_token,
                   'prefer': 'odata.maxpagesize=%s' % page_size}

        logging.info('Starting retrieval of data from %s...' % next_url)

        # loop thru pages of data until no nextLink is returned
        while next_url:
            # pull the data from the API
            response = requests.get(next_url, headers=headers)
            # parse the response
            content = response.json()
            # yield the page of results
            yield content['value']
            # if we have more data to pull, set URL for next page
            next_url = content['@odata.nextLink'] if '@odata.nextLink' in content else None

import json
import os
from xml.etree import ElementTree

import requests


def get_metadata():
    # get Reporting API meta from CSOD portal
    response = requests.get(
        "https://intelladonsandbox.csod.com/services/api/x/odata/api/views/$metadata")
    root = ElementTree.fromstring(response.content)

    # parse the data
    views_with_columns = {}
    for view in root.iter('{http://docs.oasis-open.org/odata/ns/edm}EntityType'):
        view_name = view.get('Name')
        columns = [col.attrib for col in view]
        views_with_columns.update({view_name: columns})

    # return the data
    return views_with_columns

import json
import os
from xml.etree import ElementTree

import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    response = requests.get(
        "https://intelladonsandbox.csod.com/services/api/x/odata/api/views/$metadata")
    root = ElementTree.fromstring(response.content)
    views = {}

    for view in root.iter('{http://docs.oasis-open.org/odata/ns/edm}EntityType'):
        view_name = view.get('Name')
        properties = [prop.attrib for prop in view]
        views.update({view_name: properties})

    return {
        "statusCode": 200,
        "body": json.dumps(views)
    }

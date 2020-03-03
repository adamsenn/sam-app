import json

from csod import get_metadata


def lambda_handler(event, context):
    meta_dict = get_metadata()
    return {
        "statusCode": 200,
        "body": json.dumps(meta_dict)
    }

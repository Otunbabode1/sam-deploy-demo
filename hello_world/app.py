import json
from urllib import request

# import requests


def lambda_handler(event, context):
    body = json.loads(event["body"])
    name = body["name"]


    try:
        ip = request.Request.get("http://checkip.amazonaws.com/")
    except request.RequestException as e:
        #Send some context about this error to Lambda Logs
        print(e)

        raise e
    #1223
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": name,
                # "location": ip.text.replace("\n", "")
            }
        ),
    }

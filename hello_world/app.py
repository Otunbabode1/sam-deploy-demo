import json
from urllib import request

# import requests


def lambda_handler(event, context):
    body = json.loads(event["body"])
    firstname = body["firstname"]
    lastname = body["lastname"]
    fullname = f"{firstname} {lastname}"
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
                "message": fullname,
                # "location": ip.text.replace("\n", "")
            }
        ),
    }

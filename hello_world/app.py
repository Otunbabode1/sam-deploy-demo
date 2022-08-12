import json
from urllib import request

# import requests


def lambda_handler(event, context):
   body = json.loads(event['body'])
   firstname = body["firstname"]
   lastname = body["lastname"]
   consultant = {
    "FirstName": firstname,
    "LastName": lastname,
    "Role": "Consultant"

   }


   return {
    'statusCode': 200,
    'body': json.dumps(consultant)
   } 

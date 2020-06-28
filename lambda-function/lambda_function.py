import os
import json
from classes.TwilioMessage import TwilioMessage


def lambda_handler(event, context):
    t = TwilioMessage(os.environ["TWILIO_RECIPIENT"], 'test')

    try:
        response = t.send_message()
        return dict(statusCode=200, body=json.dumps({'message': response.sid}))
    except Exception as e:
        return dict(statusCode=500, body=json.dumps({'message': str(e)}))

print(lambda_handler('test', 'test'))
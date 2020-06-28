import os
from twilio.rest import Client
from classes.MessageTransport import MessageTransport


class TwilioMessage(MessageTransport):

    def __init__(self, recipient, message):
        super().__init__(message)

        # init params dict
        self.params = {
            "sender": os.environ["TWILIO_SENDER"],
            "recipient": recipient,
            "sid": os.environ['TWILIO_SID'],
            "token": os.environ['TWILIO_TOKEN']
        }

    def send_message(self):
        # create Twilio client
        client = Client(self.params['sid'], self.params['token'])

        # send message
        response = client.messages.create(
            to=self.params['recipient'],
            from_=self.params['sender'],
            body=self.get_message()
        )

        return response

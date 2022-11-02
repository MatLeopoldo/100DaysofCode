from twilio.rest import Client


class SMSHandler:

    def __init__(self, account_id: str, token: str, from_phone_number: str) -> None:
        self.account_id = account_id
        self.auth_token = token
        self.from_phone_number = from_phone_number
        self.client = Client(self.account_id, self.auth_token)

    
    def send_message(self, dest_phone_number: str, text: str) -> None:
        message = self.client.messages.create(to=dest_phone_number, from_=self.from_phone_number, body=text)
        print(message.sid)
        
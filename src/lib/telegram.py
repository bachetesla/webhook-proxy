from .Base import ClientBase, ClientError

import requests


class Telegram(ClientBase):
    """
    Telegram client
    """

    def send(self, msg):

        api_url = f'https://api.telegram.org/bot{self.token}/sendMessage'

        try:
            response = requests.post(api_url, json={'chat_id': self.to, 'text': f"{msg}"})
            print(response.text)
        except Exception as e:
            raise ClientError(e)

    def __str__(self):
        return "TELEGRAM"

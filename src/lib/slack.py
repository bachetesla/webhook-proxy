from .Base import ClientBase, ClientError

import requests


class Slack(ClientBase):
    """
    Telegram client
    """
    def send(self, msg):

        api_url = f'https://slack.com/api/chat.postMessage'
        headers = {
            "Authorization": "Bearer " + self.token
        }

        try:
            response = requests.post(api_url, json={'channel': self.chatId, 'text': f"{msg}"}, headers=headers)
            if response.status_code != 200 or not response.json()['ok']:
                raise ClientError(response.text)
        except Exception as e:
            raise ClientError(e)

    def __str__(self):
        return "SLACK"

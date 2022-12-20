from .Base import ClientBase, ClientError

import requests


class Smsator(ClientBase):
    """
    Telegram client
    """
    def send(self, msg):
        api_url = f'https://smsator.snapp.express/api/grafana-alert?number={self.to}&message={msg}'
        headers = {
            "Authorization": "Basic " + self.token,
            "Accept": "application/json"
        }
        try:
            response = requests.post(api_url, headers=headers, json={
            })
            print(response.json())
            if response.status_code != 200:
                raise ClientError(response.text)
        except Exception as e:
            raise ClientError(e)

    def __str__(self):
        return "SMASATOR"


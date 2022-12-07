import requests

from .Base import ClientBase, ClientError


class Msteams(ClientBase):
    """
    Microsoft teams webhook message sender
    """

    def send(self, msg):
        """
        Send message
        :param msg:
        :return:
        """
        api_url = f"https://snappexpressoutlook.webhook.office.com/webhookb2/{self.token}"
        try:
            response = requests.post(api_url, json={'text': f"{msg}"})
            if response.text != "1":
                raise ClientError("Request is not valid")
        except Exception as e:
            raise ClientError(e)

    def __str__(self):
        return "MSTEAMS"

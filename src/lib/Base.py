import os

from dotenv import load_dotenv


class ClientError(Exception):
    pass


class ClientBase:
    """
    Client Base
    """

    def _validate_token(self):
        """
        Validate token
        :return:
        """
        if self.token is None or not self.token or self.token == "":
            raise ClientError("Can't find Token")

    def __init__(self, to, token=None):
        """
        Initial the object
        :param token:
        :param to:
        """
        self.to = to
        if token:
            self.token = token
        else:
            load_dotenv()
            print(self.__str__().upper() + "_TOKEN")
            os.environ.get(self.__str__().upper() + "_TOKEN", None)
            self.token = os.environ.get(self.__str__().upper() + "_TOKEN", None)
            self._validate_token()

    def send(self, msg):
        """
        Send message
        :param msg:
        :return:
        """
        raise NotImplementedError

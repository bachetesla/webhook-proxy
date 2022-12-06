class ClientError(Exception):
    pass


class ClientBase:
    """
    Client Base
    """

    def __init__(self, token, chatId):
        self.token = token
        self.chatId = chatId

    def send(self, msg):
        raise NotImplementedError

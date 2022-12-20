from enum import Enum
from .Base import ClientBase


class Clients(str, Enum):
    TELEGRAM = "Telegram"
    SLACK = "Slack"
    MSTEAMS = "Msteams"
    SMSATOR = "Smsator"

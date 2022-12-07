from pydantic import BaseModel
from src.lib import Clients


class InMessage(BaseModel):
    msg: str
    type: Clients
    chatId: str
    # token: str  #Handled by env, but if you want to get from request uncomment

from fastapi import APIRouter
from datetime import datetime
from src.lib.schema import InMessage
from src.lib.telegram import Telegram
from src.out_gateway import trigger


in_gateway = APIRouter(prefix="/in")


@in_gateway.get("/ping")
def ping():
    return {"msg": "pong", "time": datetime.now()}


@in_gateway.post("/send")
def send(data: InMessage):
    try:
        trigger(
           data
        )
        return {"msg": "Success"}
    except Exception as e:
        return {"msg": "Error", "body": str(e)}

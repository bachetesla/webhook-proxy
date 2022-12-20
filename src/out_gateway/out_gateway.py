from fastapi import APIRouter
from datetime import datetime
from src.lib.Base import ClientBase
from src.lib.schema import InMessage
out_gateway = APIRouter()


@out_gateway.get("/ping")
def ping():
    return {"msg": "pong", "time": datetime.now()}


def trigger(in_message: InMessage):
    mod = __import__(f'src.lib.{in_message.type.lower()}', fromlist=[in_message.type])
    klass = getattr(mod, in_message.type)
    klass(
        to=in_message.to
    ).send(
        in_message.msg
    )

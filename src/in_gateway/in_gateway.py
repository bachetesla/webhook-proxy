from fastapi import APIRouter
from datetime import datetime

in_gateway = APIRouter(prefix="/in")


@in_gateway.get("/ping")
def ping():
    return {"msg": "pong", "time": datetime.now()}


@in_gateway.post("/send")
def send(data):
    return {"data": data}

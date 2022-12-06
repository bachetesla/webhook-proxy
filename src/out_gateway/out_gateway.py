from fastapi import APIRouter
from datetime import datetime

out_gateway = APIRouter()


@out_gateway.get("/ping")
def ping():
    return {"msg": "pong", "time": datetime.now()}

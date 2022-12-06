from fastapi import FastAPI
from src import in_gateway

app = FastAPI()

app.include_router(in_gateway)

@app.get("/")
def root():
    return {"msg": "Hi!"}

from fastapi import FastAPI
from typing import Dict
from time import sleep

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "fastAPI says hello"}


@app.get("/short_request")
async def short_request() -> Dict[str, str]:
    return {
        "from": "fastAPI",
        "message": "short request processed"
    }


@app.get("/long_request")
async def long_request() -> Dict[str, str]:
    sleep(3.5)
    return {
        "from": "fastAPI",
        "message": "long request processed"
    }



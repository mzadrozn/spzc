from fastapi import FastAPI
from typing import Dict
from time import sleep

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, str]:
    return {
        "message": "fastAPI says hello"
    }


@app.get("/short")
async def short() -> Dict[str, str]:
    return {
        "from": "fastAPI",
        "message": "short request processed"
    }


@app.get("/long")
async def long() -> Dict[str, str]:
    sleep(3.5)
    return {
        "from": "fastAPI",
        "message": "long request processed"
    }



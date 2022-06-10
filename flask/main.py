import flask

from typing import Dict
from time import sleep


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home() -> Dict[str, str]:
    return {"message": "flask says hello"}


@app.route('/short_request', methods=['GET'])
def short_request() -> Dict[str, str]:
    return {
        "from": "flask",
        "message": "short request processed"
    }


@app.route('//long_request', methods=['GET'])
def long_request() -> Dict[str, str]:
    sleep(3.5)
    return {
        "from": "flask",
        "message": "long request processed"
    }


app.run()

import flask

from typing import Dict
from time import sleep


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home() -> Dict[str, str]:
    return {
        "message": "flask says hello"
    }


@app.route('/short', methods=['GET'])
def short() -> Dict[str, str]:
    return {
        "from": "flask",
        "message": "short request processed"
    }


@app.route('/long', methods=['GET'])
def long() -> Dict[str, str]:
    sleep(3.5)
    return {
        "from": "flask",
        "message": "long request processed"
    }


app.run(host="0.0.0.0", port=80)

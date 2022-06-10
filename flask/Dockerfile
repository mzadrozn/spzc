FROM python:3.9

WORKDIR /code/flask/app

COPY ./requirements.txt /code/flask/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/flask/requirements.txt

COPY ./app /code/flask/app

CMD ["python", "main.py"]

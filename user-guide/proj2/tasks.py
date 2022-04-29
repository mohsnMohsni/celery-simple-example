import time

from proj2.celery import app


@app.task
def say_hello_world():
    return 'Hello world.'


@app.task
def run_in_async_mode():
    time.sleep(5)
    return 'Done.'

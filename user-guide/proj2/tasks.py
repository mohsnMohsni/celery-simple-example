from proj2.celery import app


@app.task
def say_hello_world():
    return 'Hello world.'

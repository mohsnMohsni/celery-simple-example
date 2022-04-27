from celery import Celery


app = Celery('tasks')
app.config_from_object('celeryconfig')

"""
WARNING: Backends use resources to store and transmit results.
To ensure that resources are released,
you must eventually call get() or forget() on EVERY AsyncResult
instance returned after calling a task.
"""


@app.task
def add(x, y):
    return x + y


@app.task
def divide(x, y):
    return x / y

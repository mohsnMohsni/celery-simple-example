import time
from functools import wraps

from celery import shared_task

from proj2.celery import app


def decorator1(func):
    @wraps(func)  # do like pure handle meta data in bottom code
    def wrapper(*args, **kwargs):
        print('decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print('decorator 2')
        return func(*args, **kwargs)
    # pass meta data of function to wrapper, because celery use meta data to declear address of func.
    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper


@app.task
@decorator1
@decorator2
def say_hello_world():
    return 'Hello world.'


@app.task(bind=True)
def say_welcome(self):
    '''
    bind=True pass `self` argument to function, it includes task information.
    '''
    return 'Welcome.'


@shared_task
def run_in_async_mode():
    '''
    `shared_task` decorator is a task share with all app, but app.task is a decorator that
    create task just can use with specefic task.
    '''
    time.sleep(5)
    return 'Done.'

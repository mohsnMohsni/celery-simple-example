from __future__ import absolute_import, unicode_literals

from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def divide(x, y):
    return x // y


@app.task
def average(l):
    return sum(l) / len(l)

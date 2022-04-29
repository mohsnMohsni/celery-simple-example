from celery import Celery
from .task_class import MyTask


app = Celery('proj2')
app.config_from_object('proj2.celeryconfig')
app.Task = MyTask

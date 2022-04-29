from celery import Celery


app = Celery('proj2')
app.config_from_object('celeryconfig')

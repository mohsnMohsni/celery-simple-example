from celery import Celery


app = Celery('proj')
app.config_from_object('celeryconfig')

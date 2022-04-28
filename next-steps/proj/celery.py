from __future__ import absolute_import, unicode_literals

from celery import Celery


app = Celery('proj')
app.config_from_object('celeryconfig')


if __name__ == '__main__':
    app.start()

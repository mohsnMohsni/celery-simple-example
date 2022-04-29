from celery import Task


class MyTask(Task):

    def __call__(self, *args, **kwargs):
        print('TASK RUN: {0.name} {0.request.id}'.format(self))
        return self.run(*args, **kwargs)

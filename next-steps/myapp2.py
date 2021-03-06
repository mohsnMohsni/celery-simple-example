import queue
from proj.tasks import add
from proj.celery import app

# get result by id
add_result = add.apply_async(args=[4, 2], countdown=15)
add_result_id = add_result.id

res = app.AsyncResult(add_result_id)
print(res.state)


'''
default queue is celery and it's create by celery, worker lissten to this queue,
for define new queue we should define and create new queue on celery run syntax.
* now it's don't have effect on our test (default is celery)
'''
add_result2 = add.apply_async(args=[4, 2], queue='celery')
add_result2_id = add_result2.id

res = app.AsyncResult(add_result2_id)
res.get()
print(res.state)
print(res.successful())


# use signature
func_sync_to_signature = add.signature(args=[18, 2], countdown=10)
func_sync_to_signature.delay()

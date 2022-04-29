broker_url = 'redis://localhost:6379'
result_backend = 'redis://localhost:6379'

include = ['proj.tasks',]

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Tehran'
enable_utc = True


# command shell: celery -A appName worker -Q celery,queue1,queue2,queue3 -l info
task_routes = {
    'proj.tasks.add': {'queue': 'queue1'}, # name of queue pass in command shell
    'proj.tasks.divide': {'queue': 'queue2'},
    'proj.tasks.average': {'queue': 'queue3'},
}

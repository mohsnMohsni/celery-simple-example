broker_url = 'redis://localhost:6379'
result_backend = 'redis://localhost:6379'

include = ['proj.tasks', ]

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Tehran'
enable_utc = True

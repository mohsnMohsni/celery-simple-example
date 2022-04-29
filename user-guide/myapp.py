import time
from timeit import timeit

from proj2.tasks import say_hello_world, run_in_async_mode


say_hello_world.delay()


# use async mode to handle to work parallel
def check_():
    async_res = run_in_async_mode.delay()
    time.sleep(3)
    async_res.get()


print(timeit(check_, number=1))

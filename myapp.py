from tasks import add, divide




x = add.delay(10, 20)
# x = add.apply_async(args=[10, 20]) # can run task by schedule
# print(type(x)) # return an async instance for result
print(x.get()) # get result


z = add.delay(10, 20)
z.forget()


y = divide.delay(10, 0)
print(y.get(propagate=False)) # get result and handle error if an exception raised
print(y.traceback) # get exception message

print('finished.') # it's show code not sttoped and continue if an exception raised

from proj.tasks import add, divide


add_result = add.delay(4, 2)
print(add_result.get())


divide_result = divide.delay(4, 2)
print(divide_result.get())

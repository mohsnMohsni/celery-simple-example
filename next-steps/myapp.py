from proj.tasks import add, divide


add_result = add.delay(4, 2)
print(add_result.get())


divide_result = divide.delay(4, 2)
print(divide_result.get())


# async mode
add_result1 = add.apply_async(args=[4, 2], countdown=15)
add_result1.forget()


divide_result1 = add.apply_async(args=[999, 3], countdown=5)
divide_result1.forget()


# sync mode
add_result1 = add.apply_async(args=[4, 2], countdown=15)
add_result1.get()


divide_result1 = add.apply_async(args=[999, 3], countdown=5)
divide_result1.get()


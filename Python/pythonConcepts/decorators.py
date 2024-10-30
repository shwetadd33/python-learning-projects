"""
Decorators: Decorators allow you to wrap a function within another function. So you can calculate execution time of a particular fucntion
or logging certain lines at the beginning and end of the function

Note : Functions are first class objects in python. Means they can be treated just like any other variable and can pass them
as an argument to another function or even return them as a return value.
"""
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + " mil sec")
        #return result
    return wrapper

@time_it
def cal_square(numbers):
    result = []
    for i in numbers:
        result.append(i*i)
    return result

@time_it
def cal_cube(numbers):
    result = []
    for i in numbers:
        result.append(i*i*i)
    return result

array = range(1, 100000)

square = cal_square(array)
cube = cal_cube(array)




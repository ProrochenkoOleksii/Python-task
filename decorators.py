# Task 1
# Write a decorator that prints the function with the arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

from functools import wraps

def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args):
        print(f"Our data: {args}")
        return func().lower()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'heLLO there'

args=("HeY!", "Ya!")
print(say_hi(args))


# 2. Write a decorator that outputs the execution time of the function.
import time
def time_fun_decorator(func):
    @wraps(func)
    def wrapper(*args):
        start=time.time()
        result=func(*args)
        end=time.time()
        time_=(end-start)*1000
        print(f"час виконання: {time_} мс")
        return result
    return wrapper

@time_fun_decorator
def my_fun(*values):
    res=0
    for n in values:
        res+=n
    return res

print(my_fun(10,7,56,8,709))

time.perf_counter()


# 3. Create a decorator that checks the arguments passed to the function,
# and prints an error message if the arguments do not satisfy certain ones
# conditions

def my_decorator(func):
    @wraps(func)
    def wrapper(str1, str2):
        if isinstance(str1, str) and isinstance(str2, str):
            return func(str1, str2)
        else:
            print("Type of data is not string :-( ")

    return wrapper

@my_decorator
def my_func(str_1, str_2):
    str1_new = str_1 * 2
    str2_new = str_2 * 2
    str_new = str1_new + str2_new
    return str_new

str_1 = "aaaa"
str_2 = "bbb"
print(my_func(str_1, str_2))

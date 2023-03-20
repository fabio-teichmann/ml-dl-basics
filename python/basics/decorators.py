# Decorators use the @ sign to be introduced. There are:
# - @classmethod
# - @staticmethod
#
# Functions in Python can act like variables (passed in functions, etc.).
#
# Decorators provide extra features to functions.

# Higher Order Function (HOC):
# - accepts another function as an argument, or
# - returns a function

def my_decorator(func):
    # decorators use a wrapper function;
    # parameters can be passed down into wrapper
    def wrap_func(*args, **kwargs):
        # can add content before and/or after internal function
        print('*****')
        func(*args, **kwargs)
        print('*****')

    # returns the wrapper
    return wrap_func


# to use a decorator for a function, use @decorator_name
@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


hello('hii', ':)')

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()

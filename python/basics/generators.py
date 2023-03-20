# Examples
range(100)


# creates values in memory one by one. This makes generators extremely
# efficient.
def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


# the list actually takes up all the space in memory and can only be used
# once the list is done (calculated/built).
# my_list = make_list(100)
# print(my_list)


# define generator
def generator_func(num):
    for i in range(num):
        # yield pauses the function and comes back to it once 'next()' is called
        yield i * 2


g = generator_func(100)
print(g)  # generator object
print(next(g))
print(g.__next__())  # alternative way of calling next on the generator
print(next(g))

# if values in the generator are exhausted, a StopIteration Error is created

# Let's evaluate performance through our @performance decorator
# write performance decorator from memory...
import time


def performance2(fn):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f'Time elapsed: {t2 - t1}')
        return result

    return wrapper


@performance2
def long_time():
    print('1')
    for i in range(10000000):
        i * 5


@performance2
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i * 5


long_time()
long_time2()


# performance of generator is much faster than the iterable list

# ------------------------------------------------

# generators under the hood
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            # print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)

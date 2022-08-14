from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Time elapsed: {t2 - t1}')
        return result

    return wrapper


class FibGen():
    current = 0
    f1 = 0
    f2 = 1

    def __init__(self, steps):
        self.steps = steps

    def __iter__(self):
        return self

    def __next__(self):
        if FibGen.current == 0:
            FibGen.current += 1
            return FibGen.f1
        elif FibGen.current == 1:
            FibGen.current += 1
            return FibGen.f2
        # all cases with index > 1
        elif FibGen.current <= self.steps:
            temp = FibGen.f1
            FibGen.f1 = FibGen.f2
            FibGen.f2 += temp
            FibGen.current += 1
            return FibGen.f2
        raise StopIteration


@performance
def fib(num):
    gen = FibGen(num)
    for i in gen:
        print(i)


# using the class  keeps the values static -> FibGen.current will be the value
# where the previous function call left it off
fib(20)


# -------------------------------------------------------------------------
@performance
def fib2(num):
    a = 0
    b = 1
    for i in range(num + 1):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib2(20):
    print(x)

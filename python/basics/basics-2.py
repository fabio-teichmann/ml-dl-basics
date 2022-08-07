# *args and **kwargs
# kwargs is a dictionary of arguments
# rule of order: params, *args, default params, **kwargs

def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum([item for item in kwargs.values()])


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))


# Walruss operator ":="
a = 'helloooooooooooo'
if (n := len(a)) > 10:
    print('too long:', n)

# global keyword
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())

# nonlocal keyword


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'non-local'
        print('inner:', x)
    inner()
    print('outer:', x)


outer()

num = 1

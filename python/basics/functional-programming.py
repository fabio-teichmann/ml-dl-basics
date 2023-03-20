# Code is separating methods and attributes.
# Uses the concept of "Pure Functions"

# Rules of pure functions:
# 1. given the same input, it will return always the same output
# 2. should not produce any side-effects (that affects the outside world)
#   - one example is print

def multiply_by_2(li):
    # fulfills the 2 rules of pure functions
    new_list = []
    for item in li:
        new_list.append(2 * item)
    return new_list


print(multiply_by_2([1, 2, 3]))
# ------------------------------------------------------------------
my_list = [1, 2, 3]


def multiply_by_2_map(item):
    return item * 2


# map, filter, zip, reduce
# map automatically iterates over all elements and applies function to each individually
print(list(map(multiply_by_2_map, my_list)))
# original list is not affected!
print(my_list)


# filter keeps all entries where the function results in True
def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, my_list)))
# original list is not affected
print(my_list)

# zip 'zips' together items into pairs/tuples
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))
# original lists are unaffected
print(my_list, your_list)

# reduce
from functools import reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))

# --------------------------------------------------------
# lambda expressions
# multiply by 2
print(list(map(lambda item: item * 2, my_list)))
# filter
print(list(filter(lambda item: item % 2 != 0, my_list)))
# reduce
print(reduce(lambda acc, item: acc + item, my_list))

li = [5, 4, 3]
print(list(map(lambda item: item ** 2, li)))

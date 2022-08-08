# list comprehensions
my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num * 2 for num in range(100)]
print(my_list2)

my_list3 = [num ** 2 for num in range(100) if num % 2 == 0]
print(my_list3)

# dict comprehensions
keys = ['a', 'b']
values = [2, 7]
my_dict = {key: value ** 2 for key, value in zip(keys, values)}
print(my_dict)

my_dict2 = {num: num * 2 for num in values}
print(my_dict2)

# set comprehensions
my_set = {char for char in 'hello'}
print(my_set)

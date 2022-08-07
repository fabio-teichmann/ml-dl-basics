# python data types
int = 1
float = 2.4
complex
# math functions (in-built)
print(round(2.4))
print(abs(-2.4))
print(bin(5))


bool = True


str = 'hi'
long_string = '''
WOW
O O
---
'''
print(long_string)
# string concatenation
print('hello' + 'world')
# formatted strings
print('Hi {name}, you are {age} years old.'.format(name='sally', age=40))
# string indexing [start:end:stepover]
nums = '0123456789'
print('indexed string, with stepover 2:', nums[2::2])
# strings are immutable -> can concatenate but not re-assign through indexing for example


list = []
# ordered sequence of objects


tuple = ()


set = {}
# unordered collection of unique objects
my_set = {1,2,3,4,4,5}
set_2 = {6,7,8,4,5,9}
# removes duplicates
print(my_set)
print( 2 in my_set)
# methods
print(my_set.difference(set_2))
#print(my_set.discard(5), my_set)
print(my_set.difference_update())
print(my_set.intersection(set_2))
print(my_set.isdisjoint(set_2))
print(my_set.union(set_2))
print(my_set | set_2)


dict = {'key': 'value'}

# Classes -> custom types

# Specialised data types
# Modules, extensions

None # absence of value
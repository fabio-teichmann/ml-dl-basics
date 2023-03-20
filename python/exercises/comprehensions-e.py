my_list = ['a', 'b', 'c', 'b', 'n', 'r', 'n']

duplicates = list({i for i in my_list if my_list.count(i) > 1})
print(duplicates)

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('basket' in user)
print(20 in user.values())
print()

user2 = user.copy()

user.clear()
print(user)
print(user2)

print(user2.pop('age'))
print(user2.popitem())
print(user2.update({'ages': 55}))  # add new key
print(user2.update({'basket': None}))  # update existing key
print(user2)

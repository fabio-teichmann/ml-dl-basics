# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = { 'name': 'Sorna', 'valid': True #changing this will either run or not run the message_friends function. }

user1 = {
    'name': 'Sorna',
    'valid': False  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        for kw in kwargs:
            print(kw)
        if kwargs['valid']:
            fn(*args, **kwargs)
            print('logged in!')
        else:
            name = kwargs['name']
            print(f'User {name} is not authenticated!')

    return wrapper


@authenticated
def log_in(**user):
    print('logging in...')


log_in(**user1)

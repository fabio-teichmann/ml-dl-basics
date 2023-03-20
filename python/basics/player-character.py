class PlayerCharacter:
    # class object attribute = static, i.e. does not change across instances
    membership = True

    def __init__(self, name='anonymous', age=0):
        if self.membership:
            # class attributes change across instances
            self.name = name  # attributes of the class
            self._age = age  # by convention: _ means "private"

    @classmethod
    def adding_things(cls, num1, num2):  # cls refers to the class
        return cls('Ted', num1 + num2)  # instantiates a class object

    @staticmethod
    # does not care about a class object state
    def adding_things2(num1, num2):  # does not have access to class attributes
        return num1 + num2

    def run(self):
        print('run!')
        # return True  # if return is missing, the return value will be zero

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Zindi', 44)
print(player1)
print(player1.name)
print(player1.shout())

# help(player1)
print(player1.__dict__)

# class methods can be used without instantiating the class itself before
print(PlayerCharacter.adding_things(2, 3))

# can overwrite class attributes and funcs
player1.shout = 'Boo'
print(player1.shout)

player1.age = 10
print(player1.age)

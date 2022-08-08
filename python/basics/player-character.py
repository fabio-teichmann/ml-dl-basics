class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes of the class
        self.age = age

    def run(self):
        print('run!')
        # return True  # if return is missing, the return value will be zero


player1 = PlayerCharacter('Zindi', 44)
print(player1)
print(player1.name)
print(player1.run())

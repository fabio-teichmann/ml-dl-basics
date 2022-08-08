class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):  # inherits from User
    def __init__(self, name, power, email):
        # 2 ways of calling the top-level constructor
        User.__init__(self, email)
        super().__init__(email)  # does not require self
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power: {self.power}')


class Archer(User):  # inherits from User
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: {self.num_arrows}')


wizard1 = Wizard('Merlin', 15, 'merlin@gmail.com')
wizard1.sign_in()

archer1 = Archer('Robin', 100)
archer1.sign_in()

wizard1.attack()
archer1.attack()

# check for instance type
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))

# get attribute from super class
print(wizard1.email)

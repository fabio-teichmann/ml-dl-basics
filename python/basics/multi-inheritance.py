class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):  # inherits from User
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power: {self.power}')


class Archer(User):  # inherits from User
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'remaining arrows: {self.num_arrows}')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
        User


hb1 = HybridBorg('name', 50, 100)
print(hb1.run())
print(hb1.attack())

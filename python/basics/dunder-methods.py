class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        # modifies the in-built dunder method
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'yes?'

    def __getitem__(self, item):
        # enables us to access values through [] notation
        return self.my_dict[item]


action_figure = Toy('red', 2)

# __str__ enables us to use str()
print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))

# defining the __call__ function allows to use syntax below
print(action_figure())

print(action_figure['name'])

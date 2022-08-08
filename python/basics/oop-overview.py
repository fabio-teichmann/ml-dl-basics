# OOP is a tool to break up a real-world scenario into separate object.
# These objects can be given functionalities (methods) to achieve whatever
# that class of objects need to fulfill.

# Naming convention: class keyword + CamelToeNaming
class BigObject:
    # Dunder method = __method__ are built-in methods
    def __init__(self):
        pass

    pass


# instantiate: create a new instance of class BigObject
bo = BigObject()
print(type(bo))

# 4 pillars of oop:
#
# 1. Encapsulation: all desired functionality is bundle within one class object
#   (attributes, functions,...). This encapsulation acts as a blueprint to create
#   several (different) instances of the class.
#
# 2. Abstraction: hiding of information, giving access to only what is necessary.
#
# 3. Inheritance: allows classes to inherit attributes/methods from other classes.
#
# 4. Polymorphism: different object classes can share names (albeit, the
#   functionality may differ).


# Python allows for Introspection. dir() lists all available methods and attributes.
print(dir(bo))

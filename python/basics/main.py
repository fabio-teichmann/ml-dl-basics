# use import to access other python files
import modules
import shopping.shopping_cart  # access module within package


# all imports will be cached in __pycache__ for use

# print(modules)
# use functions from different files
# print(modules.divide(10, 2))
# print(modules.multiply(2, 10))
# print(shopping.shopping_cart.buy('apple'))

def do_stuff(num=0):
    try:
        if num is None:
            return 'please enter number'
        else:
            return int(num) + 5
    except ValueError as err:
        return err

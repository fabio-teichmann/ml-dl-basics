# use import to access other python files
import modules
import shopping.shopping_cart  # access module within package

# all imports will be cached in __pycache__ for use

# print(modules)
# use functions from different files
print(modules.divide(10, 2))
print(modules.multiply(2, 10))
print(shopping.shopping_cart.buy('apple'))

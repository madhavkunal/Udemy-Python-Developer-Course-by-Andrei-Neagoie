# shopping cart module located in shopping folder package
# a folder is a package which contains multiple files (modules)

print(__name__)  # prints __main__ when running this file - shopping_cart.py file
# prints shopping.shopping_cart when running main.py file


def buy(item):
    cart = []
    cart.append(item)
    return cart

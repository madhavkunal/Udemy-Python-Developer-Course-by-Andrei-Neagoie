# Module - File that stores functionality and that can be imported into the main program file. Modules make classes and functions modular or reusable. You can make custom modules or import modules from pre-existing Python Libraries. Modules make code more organized, easier to read and simplify as well as clean up our main program files. # python contains built-in-modules in its root directory (aka Python Standard Library)

# importing modules within same directory

print(__name__)  # prints __main__ when running this file

# print(__name__) will always print __main__ whenever a file that contains the statement is run (since the file being run is now the main file)

import shopping.shopping_cart as shopping_cart  # same as - import shopping_cart from shopping
import utility

# will also print shopping.shopping_cart and utility when running this file because those files have been imported in this file and both also contain a print(__name__) statement

print(
    utility
)  # prints:  <module 'utility' from '/home/runner/Section11ModulesInPython/utility.py'>
print(
    shopping_cart
)  # prints:  <module 'shopping.shopping_cart' from '/home/runner/Section11ModulesInPython/shopping/shopping_cart.py'>

print(utility.multiply(5, 5))  # prints 25
print(utility.divide(25, 5))  # prints 5

print(shopping_cart.buy("controller"))  # prints ['controller']

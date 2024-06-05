# python contains built-in-modules in its root directory (aka Python Standard Library)

import random  # import random built-in-module
import sys  # import sys (system) built-in-module

# help(random)

print(random)
print(dir(random))
print(random.random())
print(random.choice([1, 2, 3, 4, 5]))

list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

print(sys)
sys.argv  # gives terminal ability to accept paramaters on system files

# prints <module 'random' from 'C:\\Users\\Madhav\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\random.py'>

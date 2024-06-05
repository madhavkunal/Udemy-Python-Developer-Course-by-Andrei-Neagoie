# Decorators
"""
In python, functions are first class citizens:
- they can be passed like variables
- they can be an argument inside of a function
- they act like variables

def hello():
  print('helllloooo');

greet = hello
hello()
del hello
print(greet())

# hello is deleted, but greet is saved in memory as a seperate function

def hello(func):
  func()

def greet():
  print('still here')

a = hello(greet)  # a runs the hello function with the greet argument (running a function within a function)
print(a)

# hello is deleted, but greet is saved in memory as a seperate function


# Higher Order Function (HOF)

# HOF 1 -> A function that accepts another function as a parameter

def greet(func):
  func()

# HOF 2 -> A function that returns a function

def greet2():
  def func():
    return 5
  return func


# map(), reduce(), filter() are HOFs

# Decorator -> A function that wraps another function

def my_decorator(func):  # Accepting the wrapped     function as a parameter of the decorator function
  def wrap_func(*args, **kwargs):       # Having a wrapper function
    print('***')          
    func(*args, **kwargs)               # Calling the wrapped function
    print('***')         
  return wrap_func       # Returning the wrapper function

@my_decorator     
def hello(greeting, emoji=':('):
  print(greeting, emoji)

@my_decorator
def bye():
    print("see ya later")


hello('hiiiii')
bye()


# Args and Kwargs Review

# Python Crash Course - Exercises

# Sandwiches

# def swtoppings(*toppings):
#   print(f'You ordered a {toppings} sandwich')

# swtoppings('jalapenos', 'red peppers', 'pepperoni')
# swtoppings('turkey', 'egg', 'provolone')
# swtoppings('buffalo chicken', 'lettuce', 'tomatoes')


# User Profile

def build_profile(first, last, **user_info):
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('Madhav', 'Kunal', location = 'Warren', job = 'data annotator')

print(user_profile)


# Cars

def make_car(manufacturer, model, **features):
    features['manufacturer'] = manufacturer
    features['model'] = model
    return features
    print(manufacturer, model ,**kwargs)

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)



# Decorator

#import time module from python
from time import time    

def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()  #check time
    result = fn(*args, **kwargs)
    t2 = time()  #check time after running function
    print(f'function took {t2-t1} ms to run') 
    # print difference in time or runtime for function
    return result
  return wrapper

@performance   #creating custom decorator
def long_time():
  for i in range(10000):  #the more complex the variables and arguments passed in the function, the longer it takes to run the code
    i*5


long_time()


"""

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        t2 = time()
        result = fn(*args, **kwargs)

        print(f"function took {t2-t1} ms to run")
        return result

    return wrapper


@performance
def long_time():
    for i in range(10000):
        i * 5


long_time()

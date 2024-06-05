# Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. Errors that crash our programs can be prevented by writing built-in special objects called exceptions.

# Error Handling- -> Proper error handling allows programs to continue to run regardless of any potential errors. If exceptions are not handled, the progam will halt and show a traceback which includes a report of the exception that was raised.

# Error Type/Exception Object Examples

"""
print('123)  # Syntax Error: unterminated string literal (detected at line 6)

def hooohooo()
  pass        # SyntaxError: expected ':'

print(1+'hello')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
  
def hooo():
  1 + name  
hooo()  # NameError: name 'name' is not defined

def hooo():
  li = [1,2,3]
  li[5]
hooo()  # IndexError: list index out of range


def hooo():
 di = {'a1': 1}
 di ['b']
hooo()   # KeyError: 'b'


def hooo():
  5/0
hooo()  # ZeroDivisionError: division by zero

# Exception Objects - > ZeroDivisionError, IndexError, NameError, SyntaxError, etc.

# Error Handling- -> Proper error handling allows programs to continue to run regardless of any potential errors. 

Exceptions are handled with try-except blocks which ask Python to do something and also tell Python what to do if an exception is raised. Writing exceptions allows programs to continue running despite errors and instead of receiving tracebacks the user will see more readable-friendly error messages.

# Input Handling

while True:
  try: 
    age = int(input('what is your age?'))
    print(age)
  except: 
    print('please enter a number')
  else: 
    print('thank you')
    break

# Err Variable

def sum(num1, num2):
  try:
    return num1 + num2
  except TypeError as err:
    print(f'Please enter numbers {err}')

print(sum('1', 2))

# The except statement catches my error and the print statement prints descriptive error information:
# Please enter numbers can only concatenate str (not "int") to str
# None
# err is a built in python error object which shows error information returned from catch ('except' statements). We can handle multiple errors by stating their types after except ->
# except ErrorType as err
 

# Python Crash Course - Exceptions

# Example -> Addition

while True:
  try:
    num1 = int(input('enter first number: '))
    num2 = int(input('enter second number: '))
  except ValueError:
    print("Please enter numbers only")
  else: 
    print(num1 + num2)

    
"""

# finally statement

while True:
    try:  # runcode
        age = int(input("what is your age?"))
        if age == 0:
            print("please enter a valid age")
        else:
            print(f"You are {age} years old")
    except NameError:
        print("please enter a number")
    except ValueError:  # exception
        print("please enter a number")

    # finally:
    #  print('Thank you')
    #   break
    # #finally:


"""
what is your age?12
12
Thank you
Finally Done :)

what is your age?0
please enter a valid age
what is your age?


what is your age?fef
please enter a number
what is your age?
"""

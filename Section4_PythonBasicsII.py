# Conditional Logic and Control Flow in Python

"""
# If then else statements

# if condition: is the same as if condition is true then do something

old = True
licensed = True 

if old: #if the variable old is true
    print("You are old enough to drive") #then this will be printed
if licensed: #if the variable licensed is true
    print("You are licensed to drive") #then this will be printed
else: #else if the first two if statements are not true
    print("You are not old enough to drive") #this will not be printed
    print("You are not licensed to drive") #this will not be printed
# The above code will print "You are old enough to drive" and "You are licensed to drive" because the first if statement is true and the second if statement is false.


old = False
licensed = True

if old: #if the variable old is true
    print("You are old enough to drive") #then this will be printed
if licensed: #if the variable licensed is true
    print("You are licensed to drive") #then this will be printed
else: #else if the first two if statements are not true
    print("You are not old enough to drive") #this will not be printed
    print("You are not licensed to drive") #this will not be printed
# The above code will print "You are licensed to drive" because the first if statement is false and the second if statement is true. 


#If else if statements ; elif is short for else if

old = False
licensed = True 

if old: #if the variable old is true
    print("You are old enough to drive") #then this will be printed
elif licensed: # else if the variable licensed is true
    print("You are licensed to drive") #then this will be printed
else: #else if the first two if statements are not true
    print("You are not old enough to drive") #this will not be printed
    print("You are not licensed to drive") #this will not be printed
# The above code will print "You are licensed to drive" because the first if statement is false and the second if statement is true.


#If and else statements 

old = True
licensed = True 

if old and licensed: #if the variable licensed is true and the variable old is true
    print("You are able to drive") #then this will be printed
else: #else if the first two if statements are not true
    print("You are not old enough to drive") # then this will be printed

# The above code will print "You are able to drive" because the first if statement is true and the second if statement is true.



# Indentation is used in Python to define a block of code. If the indentation is not correct, the code will not run. It is used to define the scope of the code and to separate the code into blocks. It is used for loops, functions, and conditional statements.


# Truthy and Falsy values in Python

# In Python, a truthy value is a value that is considered true when evaluated in a Boolean context. All values are considered true unless they are defined as false. A falsy value is a value that is considered false when evaluated in a Boolean context.

print(bool(1)) #True. 1 is considered true.
print(bool(True)) #True. True is considered true.
print(bool("True")) #True
print(bool("False")) #True. "False" is considered true.
print(bool("Hello")) #True
print(bool(" ")) #True
print(bool("0")) #True
print(bool("None")) #True. "None" is considered true.
print(bool("[]")) #True
print(bool("{}")) #True. An empty dictionary is considered true.
print(bool("()")) #True
print(bool("0.0")) #True
print(bool("0")) #True. "0" is considered true.

# The above statements are all true because they are not empty or equal to 0.0 or None.

print(bool(0)) #False. 0 is considered false.
print(bool(False)) #False . False is considered false.
print(bool(None)) #False. None is considered false.
print(bool("")) #False
print(bool([])) #False. An empty list is considered false.
print(bool({})) #False
print(bool(())) #False
print(bool(0.0)) #False. 0.0 is considered false.

# The above statements are all false because they are empty or equal to 0.0 or None.


username = 'john'
password = '123'

if password and username:
    print("You are logged in")
else:
    print("You are not logged in")


# Ternary Operator in Python

# The ternary operator is a conditional expression that evaluates a condition and returns a value based on the condition. It is a one-liner if-else statement. It is used to assign a value to a variable based on a condition.


# condition1 if condition else condition2

isFriend = True
canMessage = "message allowed" if isFriend else "message not allowed"
print(canMessage) #message allowed

isFriend = False
canMessage = "message allowed" if isFriend else "message not allowed"
print(canMessage) #message not allowed


# Short Circuiting in Python. Short circuiting is a concept in Python that allows the interpreter to stop evaluating an expression as soon as the result is known. It is used in logical operators such as and and or.

is_Friend = False
is_User = True

#print(is_Friend and is_User) #True. The interpreter stops evaluating the expression as soon as it knows the result is true.

if is_Friend and is_User:
    print("Best Friends Forever") # Does not print anything because is_Friend is false.

if is_Friend or is_User:    #True. The interpreter stops evaluating the expression as soon as it knows the result is true.
    print("Best Friends Forever") #Best Friends Forever. The interpreter stops evaluating the expression as soon as it knows the result is true.    
# Or operator is efficient when the first condition is true. It is efficient because the interpreter stops evaluating the expression as soon as it knows the result is true. This is an example of short circuiting.


# Logical operators in Python < > <= >= == != and or not They are used to combine conditional statements. 

print(4<5) #True
print(4>5) #False
print(4<=5) #True
print(4>=5) #False
print(4==5) #False | == is used to compare two values. It returns True if the values are equal and False if the values are not equal.
print(4!=5) #True
print(not 4<5) #False
print(not 4>5) #True
#print(4=5) #SyntaxError: cannot assign to literal. = is used to assign a value to a variable. == is used to compare two values.

print('a'=='a') #True 
print('2'==2) #False. The first value is a string and the second value is an integer. They are not equal.
print('2'=='2') #True. The first value is a string and the second value is a string. They are equal.

#ASCII values are used to compare strings. The ASCII value of a is 97 and the ASCII value of A is 65. The ASCII value of b is 98 and the ASCII value of B is 66. The ASCII value of 1 is 49 and the ASCII value of 2 is 50.

print('2'>'1') #True. The first value is greater than the second value
print('b'>'a') #True. The first value is greater than the second value
print('a' > 'A') #True. The first value is greater than the second value
print('a' > 'B') #False. The first value is not greater than the second value


print(1<2<3<4) #True. 1 is less than 2, 2 is less than 3, and 3 is less than 4.
print(1<2>3<4) #False. 2 is not greater than 3

print(0<1 and 1<2) #True. Both conditions are true.
print(0<1 and 1>2) #False. The second condition is false.
print(0==0 or 3<2) #True. The first condition is true.
print(0 != 1) #True. The values are not equal.
print(4>=2) #True. The first value is greater than or equal to the second value.
print(4<=2) #False. The first value is not less than or equal to the second value.

# not keyword in Python is used to reverse the result of a condition. It returns True if the condition is false and False if the condition is true.

print(not 1<2) #False. The condition is true so we do "not" print true
print(not 1>2) #True. The condition is false so we do "not" print false



# Exercise: Logical Operators in Python

is_magician = False
is_expert = True

# Exercise: Logical Operators in Python

is_magician = False
is_expert = True

if is_magician and is_expert:
  print("You are a master magician")
elif is_magician and not is_expert:
  print("at least you're getting there")
elif not is_magician:
  print("You need magic powers")


# Readability is important!!!


print(True == 1) #True. True is equal to 1.
print('' == 1) #False. An empty string is not equal to 1.
print([] == 1) #False. An empty list is not equal to 1.
print(10 == 10.0) #True. 10 is equal to 10.0.
print([] == []) #True. An empty list is equal to an empty list.


a = [1,2,3]
b = [1,2,3]
a == b #True. These values are equal


# is vs == in Python. is is used to compare the memory location of two objects. == is used to compare the VALUES of two objects (equality). is tends to be stricter.


#print(True is 1) #False
#print('' is 1) #False
#print([] is 1) #False
#print(10 is 10.0) #False
#print([] is []) #False

# Data structures always created in new locations in memory

print(True is True) #True
print('' is '') #True
print([] is []) #False, two seperate data structures
print(10 is 10) #True
print([1,2,3] is [1,2,3]) #False


# For Loops in Python. A for loop is used to iterate over a sequence or an iterable - object that contains a collection of items (list, tuple, string, dictionary, set, range). It is used to execute a block of code multiple times. It is used to iterate over a sequence of elements. An ierable is something that gets looped over. 

# for something in Iterable:

for item in 'Zero to Mastery':   # Iterable - String
  print(item)

for item in [1,2,3,4,5]:  # Iterable - Array
  print(item)

for item in {1,2,3,4,5}:  # Iterable - Set
  print(item)

for item in (1,2,3,4,5):  # Iterable - Tuple
  print(item)

#loop over each item in tuple 3 times
for item in (1,2,3,4,5): 
  print(item)
  print(item)
  print(item)
#at the end of the loop (not indented), print('hi')
print('hi')


#loop over each item in tuple 3 times
for item in (1,2,3,4,5): 
  print(item)
  print(item)
  print(item)
#at the end of the loop (not indented), print the last value in the loop (5)
print(item)
# 1-4 will each get printed three times while 5 will get printed 4 times


# Nested Loops

# x : a variable name that represents the current element during each iteration. It is initialized to the first element of the iterable, and its value is updated sequentially to the next element after each iteration

for x in (1,2,3,4,5):
  print(x)

# the inner loop runs its entire course for each value of item in the outer loop. the item from the outer loop gets printed once for each iteration of the inner loop

for item in (1,2,3,4,5):  #outer loop
  for x in ['a','b','c']:  #inner loop
    print(item, x)

# Iterables

user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}


# .items() gets each key-value pair in a tuple


for item in user.items(): #print entire items
  print(item)

for item in user: #print each key in each item
  print(item)

for item in user.keys(): #print each key in each item  
  print(item)

for item in user.values(): #print each value in each item
  print(item)



for key, value in user.items():
  print(key, value)

for key, value in user.items():
  print(key, value)


# Exercise: Tricky Counter
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for value in my_list:
  counter += value
print(counter)


# range


print(range(100))
print(range(0,100))

for value in range(10):
  print(value)

# 0-9 is printed (10 is excluded)


# Exercise: Range

   # range is a generator. It is a special type of function that will generate information and not store it in memory. It is used to generate a sequence of numbers. 


# Use a for loop to print the numbers 1-100

for number in range(0,10):
  print('email email list') #prints 'email email list' 10 times


# _ is a common convention for a throwaway variable. It is used when the variable is not used in the loop. It is used to iterate over a sequence of numbers.

for _ in range(0,10):
   print(_)   # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for _ in range(0,10,2):   # range(start, stop, step) 
   print(_)    # 0, 2, 4, 6, 8

for _ in range(0,10,-1):   # range(start, stop, step) 
   print(_)    # nothing is printed because the start is less than the stop

for _ in range(10,0,-1):   # range(start, stop, step)
    print(_)    # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

for _ in range(10,0,-2):   # range(start, stop, step)
    print(_)    # 10, 8, 6, 4, 2

for _ in range(10,0):   # range(start, stop, step)
    print(_)    # nothing is printed because the start is greater than the stop


for _ in range(2):
    print(list(range(10)))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is printed twice

          #print(range(10)) = range(0, 10)
          # print(list(range(10))) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Enumeration
# enumerate() is a built-in function in Python. It is used to add a counter to an iterable and return it in a form of an enumerate object. It is used to loop over something and have an automatic counter. It returns a tuple containing a count for each iteration and the values obtained from iterating over a sequence.

for char in enumerate('Hello'):
  print(char)  # (0, 'H') (1, 'e') (2, 'l') (3, 'l') (4, 'o')

for char in enumerate(list(range(100))):
    print(char)



for index,char in enumerate(list(range(100))):
    print(index, char)
    if char == 50:
        print(f'Index of {char} is {index}')  # 50



# While Loops. 

i = 0
while i < 50: # while the condition is true, the loop will continue to run
  print(i)  # This is an infinite loop because the condition is always true. It will print 0 forever.


i = 0
while i < 50: # while the condition is true, the loop will continue to run
    print(i) 
    i += 1  # This will print 0-49. It will not print 50 because the condition is false. i += 1 is used to increment the value of i by 1. It is the same as i = i + 1.
else:
    print('done with all the work')  # done with all the work. This will be printed when the condition is false. When i - 50, the loop will stop running and this will be printed.



# While Loops vs For Loops. 
# For loops are simpler. While loops are more flexible but more complex. While loops are better for when you don't know how many times you want to loop. For loops are better for when you know how many times you want to loop.

list = [1,2,3]

for item in list:
    print(item)

i = 0
while i < len(list):
    print(list[i])
    i += 1


while True:
    response = input('say something: ')
    if (response == 'bye'):
        break


# Break, Continue, Pass

# Break is used to exit the loop. It is used to stop the loop before it has completed all its iterations. It is used to stop the loop when a certain condition is met. It is used to break out of the loop.

# Continue is used to skip the current iteration and continue with the next iteration. It is used to skip the current iteration when a certain condition is met. It is used to continue with the next iteration of the loop.

# Pass is used as a placeholder. It is used when the statement is required syntactically but the program requires no action. It is used to do nothing

list = [1,2,3]

for item in list:
    print(item)
    continue

i = 0
while i < len(list):
    print(list[i])
    i += 1
    continue


list = [1,2,3]

for item in list:
    print(item)
    pass

i = 0
while i < len(list):
    print(list[i])
    i += 1
    pass


# Remove the unnecessary string statement


# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

#       [           outer list      outer list contains inner lists
#   [p, p, p]    inner list -> contain pixels (single values)
#   [p, p, p]    inner list     p = pixel
#   [p, p, p]    inner list
# ]           outer list


for row in picture:         #iterate over each row in the picture
  for pixel in row:         #iterate over each pixel in each row
    if pixel:               #if a pixel exists 
      print('*', end='')    #print a star
    else:                   #else if a pixel does not exist
      print(' ', end='')    #print a space
  print()                   #print a new line after each row

# a pixel represents a value in the picture. If the value is 1, it is a pixel because it is true.If the value is 0, it is not a pixel because it is false. The picture is a 2D array and a list of lists. The outer list contains the rows and the inner lists contain the pixels. The outer loop iterates over each row in the picture. The inner loop iterates over each pixel in each row. If a pixel (or 1) exists, a star ('*') is printed. If a pixel does not exist (or 0), a space ('') is printed. A new line is printed after each row.


for row in picture:        #iterate over each row in the picture
    for pixel in row:       #iterate over each pixel in each row
        if pixel == 1:          #if a pixel == 1
            print('*', end='')  #print a star
        else:                   #else if a pixel == 0
            print(' ', end='')  #print a space
    print()                 #print a new line after each row    


# Clean Code - Readability is important! 
# Comments are important! 
# Use descriptive variable names!
# Break code into functions!
# Use whitespace properly!
# Use proper indentation!
# Predctable code is better than clever code!
# DRY - Don't Repeat Yourself!



# Exercise: Check for duplicates in a list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []             #empty list to store duplicates
for value in some_list:     #iterate over each value in some_list
    if some_list.count(value) > 1:  #if the count of the value is > 1
        duplicates.append(value)   #append value to the duplicates []
print(f'The duplicates are {duplicates}')  #print the duplicates list




# Functions in Python. 
# Functions are used to perform a specific task and used to group code together. They are used to make code reusable, readable,  modular and scalable. Functions allow us to keep our code DRY. They are used to define a block of code that can be executed when called from other:

functions
classes
modules
libraries 
packages

# We initialize or define a function with the def keyword. We then give the function a name and then parameters. We then give the function a block of code to execute. We then call (or invoke, execute) the function by using the function name and passing in the parameters. We call a function with the function name and parentheses (). Functions are stored in memory and can be called at any time.


def say_hello():
  print('hello')

say_hello()  # prints hello
print(say_hello) # prints <function say_hello at 0x7f8e3c0e3d30>   which is the memory location of the function


# Parameters in Functions. Paramaters are the variables that are used in the function definition. They are used to pass data (arguments) to the function. 

# Default Parameters in Functions. Default parameters are used to set a default value for a parameter. If no value is passed to the parameter, the default value is used.

def say_hello(name='Devil', emoji='😈'):
  print(f'Hello {name} {emoji}')

# Prints the default parameters
say_hello()  # Prints Hello Darth Vader 😊 

# Arguments in Functions. Arguments are custom data values that are passed to the function paramaters when the function is called.

# Keyword arguments are arguments that are passed to the function parameters by using the parameter name. The order of the arguments does not matter when using keyword arguments.)
say_hello(emoji = '👻' , name = 'Boo')  # Prints Hello Boo 👻 since order does not matter with keyword arguments
say_hello(name = '🤡' , emoji = 'Joker') # Prints Hello 🤡 Joker 

# Default parameters are used when no value is passed to the parameter. If a value is passed to the parameter, the default value is not used.
say_hello(name = 'Tim') #Prints Hello Tim 😈 b/c default emoji is 😈 
say_hello(emoji = '🤡') #Prints Hello Devil 🤡 b/c default name is Devil

# Positional arguments are arguments that are passed to the function parameters by position. The order of the arguments matters when using positional arguments.)
say_hello('Bob', '😊')   # Prints Hello Bob 😊
say_hello('Sally', '😊')  # Prints Hello Sally 😊
say_hello('Emily', '😊')  # Prints Hello Emily 😊

say_hello('😊', 'Bob')  # Prints Hello 😊 Bob since order matters with positional arguments


# Print vs Return in Functions. Print is used to display the value of the variable. Return is used to return a value from a function and store it in a variable.

def sum(num1, num2):
  print(num1 + num2)  

total = sum(10, 5)  # Prints 15
print(total)   # Prints None because the function does not return a value. It only prints the value.

sum(9, 8)  # Prints 17
sum(12, 5) # Prints 17


# Return in Functions. Return is used to return a value from a function. It is used to return a value from a function and store it in a variable.

def sum(num1, num2):
  return num1 + num2    

total = sum(10, 5)  # total = 15

print(total)  # Prints 15
print(sum(9, 8))  # Prints 17
print(sum(12, 5)) # Prints 17

print(sum(10, total)) # Prints 25   10 + 15 = 25



def checkDriverAge():

    age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge()

# 1. Wrap the code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.

# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?


def checkDriverAge(age=0):

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge(40)
checkDriverAge()

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.



# Methods vs Functions in Python

# Objects are instances of classes. They are data types used to store data and methods. Examples of objects are lists, strings, dictionaries, sets, tuples, and integers.

# Methods are functions that are associated with an object. They are used to:
-perform operations on the object 
-modify the object
-access the object's data, attributes, properties, methods,  functions. 

# Functions are used to perform a specific task. They are used to group code together. They are used to make code reusable, readable,  modular and scalable. They are used to define a block of code that can be executed when called from other.


# Built-in functions in Python

list()
print()
max()
min()
input()
len()

# Custom functions in Python


def my_function():
    print("Hello")


# Built-in methods in Python. Methods are functions that are associated with an object. They are used to perform operations on the object, modify the object, and access the object's data, attributes, properties, methods,  functions. Methods are initiated with dot notation and are called with parentheses.

"hello".capitalize()
"hello".replace()
"hello".isalpha()
"hello".isdigit()

# Custom methods in Python.

# Docstrings

def test(a):
    """
#    Info: this function tests and prints param a
#   """
#  print(a)


# test("!!!")  # Prints !!!

# help(test)  # help(test) is used to print the docstring for the function test.
# It prints Info: this function tests and prints param a

# Magic Methods.
# print(
#  test.__doc__
# )  # test.__doc__ is used to print the docstring for the function test.

"""

# Clean Code - Readability is important!

def isOddorEven(num):
    if num % 2 == 0: # if the number is divisible by 2 and the  remainder is 0 (even number)  
        return "Even" # then the number is even
        return "Odd"  # else the number is odd
print(isOddorEven(50))  # Even
print(isOddorEven(51))  # Odd

def isEven(num):
  if num % 2 == 0: # if the number is divisible by 2 and the  remainder is 0 (even number)  
    return True # then the number is even
  return False  # else the number is odd
print(isEven(50))  # True - it is even
print(isEven(51))  # False - it is odd

def isEven(num):
  return num % 2 == 0 # if the number is divisible by 2 and the  remainder is 0 then the function evaluates to true because it is an even number else the function evaluates to false because it is an odd number  
print(isEven(50))  # True - it is even
print(isEven(51))  # False - it is odd

# Arguments in Functions. Arguments are custom data values that are passed to the function paramaters when the function is called.

# Keyword arguments are arguments that are passed to the function parameters by using the parameter name. The order of the arguments does not matter when using keyword arguments.


# args and kwargs in Python. 

# args is a tuple of arguments given inside a function
# kwargs is a dictionary of arguments given inside a function
# *args and **kwargs. *args is used to pass a variable number of non-keyword arguments to a function. **kwargs is used to pass a variable number of keyword arguments to a function.

def super_func(*args, **kwargs):  # *args and **kwargs are used to pass a variable number of arguments to a function.
  return sum(args) + sum(kwargs.values()) # return the sum of the args plus the sum of the kwargs

print(super_func(1,2,3,4,5, num1 = 5, num2=10))  # 30 (1+2+3+4+5+5+10)
# 15 + 15 = 30


# Rule: params, *args, default parameters, **kwargs

def super_func(name, *args, i='hi', **kwargs):  # *args and **kwargs are used to pass a variable number of arguments to a function.  
  return sum(args) + sum(kwargs.values()) # return the sum of the args plus the sum of the kwargs

print(super_func('Andy', 1,2,3,4,5, num1 = 5, num2=10))  # 30 (1+2+3+4+5+5+10)


# Exercise: Print Highest Even Num Function

def highest_even(li):
  highestEven = None  #Initialize highestEven, variable representing the highese Even Number
  for num in li:  #Iterate over each number in list
      if num % 2 == 0:  # Check if the number is even
          if highestEven is None or num > highestEven:  # Check if it's higher than the current highest
              highestEven = num  #Reset highest variable to current highest even number
  if highestEven is None:
      return "No even numbers found"
  else:
      return highestEven
print(highest_even([10,2,3,4,8,11]))  # 10


def highest_even(li):
  evens = []  
  for num in li:  #Iterate over each number in list
      if num % 2 == 0:  # Check if the number is even
          evens.append(num)
  return max(evens)
print(highest_even([10,2,3,4,8,11]))  # 10


a = 'helloooooooooooo'

if len(a) > 10:
  print(f'too long {len(a)} elements')
  # print(f'too long {len(a)} elements') is used to print the length of the string a. It prints too long 16 elements because the length of the string a is 16
  
# Walrus Operator in Python. The walrus operator is used to assign a value to a variable as part of an expression and return the value. 

  
a = 'helloooooooooooo'

if ((n := len(a) > 10)):
  print(f'too long {n} elements')
  # print(f'too long {len(a)} elements') is used to print the length of the string a. It prints too long 16 elements because the length of the string a is 16
  
while ((n := len(a)) > 1):
  print(n)
  a = a[:-1]
  
print(a)


# Scope - where a variable is accessible in your code.
# LEGB Rule - Local, Enclosing, Global, Built-in
 
# Local Scope - variables that are defined inside of a function.
# Enclosing Scope - variables that are defined in the local scope of any and all enclosing functions (def or lambda), from inner to outer
# Global Scope - variables that are defined outside of a function.
# Built-in Scope - variables that are preassigned in the built-in names module: open, range, SyntaxError, etc
# Nonlocal Scope - keyword used to declare a variable in the enclosing scope


total = 100 # Global Scope

def my_func():
  total = 10  # Enclosing Scope
  print(total)
  
my_func()  # 10


def my_func():
  total = 10  # Local Scope
  print(total)


a = 1 # Global Scope. a is defined outside of the function. a can be accessed inside and outside of the function.

def confusion():  # Enclosing Scope. def confusion() is the enclosing function.
  a = 5 # Local Scope.  a is defined inside of the function and is local to the function so it cannot be accessed outside of the function.
  # Difference between enclosing and local scope is that the enclosing scope is the scope of the enclosing function and the local scope is the scope of the local function.
  return a  

print(a)  #1  # Global Scope
print(confusion())  #5  # Local Scope
print(a)  #1  # Global Scope

a = 1 # Global Scope. a is defined outside of the function. a can be accessed inside and outside of the function.

def parent(): # Enclosing Scope. def parent() is the enclosing function.
  a = 10 # Local Scope.  a is defined inside of the function and is local to the function so it cannot be accessed outside of the function.
  def confusion(): # def confusion() is the local function. It is the local scope of the local function.
    return sum  # sum is a built-in function. It is the built-in scope. It is preassigned in the built-in names module.
    return a  
  return confusion() 

print(parent())  #10  Local Scope
print(a)   #1  Global Scope

"""
"""
# LEGB Rule - Local, Enclosing, Global, Built-in
1. Start with local scope
2. Go to enclosing scope
3. Go to global scope
4. Go to built-in scope


a = 10 
def confusion(b): # parameter b is local to the function, it is a local variable
  print(b) 
a = 90

confusion(300)


# global keyword in Python. The global keyword is used to access the global variable inside of a function.

total = 0 # Global Scope

def count():
  global total  # global total is used to access the global variable total inside of the function which is 0
  total += 1
  return total


count()
count()
count()
print(count())

a = 10 
def confusion():
  print(b)
a = 90

# nonlocal keyword in Python. The nonlocal keyword is used to declare a variable in the enclosing scope.

def outer():
  x = "local"
  def inner():
    nonlocal x  # nonlocal is used to declare a variable in the enclosing scope
    x = "nonlocal"
    print("inner:", x)  # inner: nonlocal
    
  inner()
  print("outer:", x)  # outer: nonlocal
outer()

def outer():
  x = "local"
  def inner():
    x = "nonlocal"
    print("inner:", x)  # inner: nonlocal
    
  inner()
  print("outer:", x)  # outer: nonlocal
outer()

# functions and print statements need to be indented properly in line with the scope of the function


# Imposter Syndrome. Imposter syndrome is the feeling of:
# being a fraud and not deserving of success. 
# not being good enough and not being able to do the job. 
# not being as good as others. 
# not being able to live up to expectations.



x = int(5)

print(x)
print(type(x))

x = "Hello"[0]

print(x)

uppercase = "Hello".upper()
print(uppercase)

"""

fav_pizza_toppings = [
    "pepperoni and red peppers",
    "jalapeno and banana peppers",
    "chicken and yellow peppers",
]
for fav_pizza_topping in fav_pizza_toppings:
    print(f"I like {fav_pizza_topping} on my pizza")
print("I really love pizza!")

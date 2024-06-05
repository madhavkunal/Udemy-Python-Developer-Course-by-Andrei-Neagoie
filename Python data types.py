''' 
# Section 3: Python Basics

#Fundamental Data Types

int #integer ; whole number (not fractional) [Examples 3, 4, 5]
int = 5
print(int)

print(2+4) 
print(2-4)
print(2*4)
print(9.9+1.1) 

#  ** is the exponentiation operator
#  ** means to the power (or exponent) of 
print(2**3) # (2**3) = 2 to the power of 3 = 2*2*2 = 8

#  // is the integer division operator
# (always rounds any decimals down to the nearest integer)
print(2//4) # (2//4) = 2/4 = 0.5 -> rounded down to 0
print(5//4) # (5//4) = 5/4 = 1.25 -> rounded down to 1
print(4//4) # (4/4) = 1 

#  % is the modulo operator -> returns the remainder after division
print(6%4) # (6%4) = 2 -> 2 is the remainder of 6/4. 
print(5%4) # (5%4) = 1 -> 1 is the remainder of 5/4
print(2%5) # (2%5) = 2 -> 2 is the remainder since 2/5 is not evenly divisible

print(type(2+4)) # (2+4) = 6 -> 6 is an integer type
print(type(2-4)) # (2-4) = -2 -> -2 is an integer type
print(type(2//4)) # Integer Division .5 becomes rounded down to 0 which is an integer
print(type(5//4)) # (5//4) = 5/4 = 1.25 rounded down to 1 which is an integer


float # floating point number ; fractional ; decimal point number
float = 3.2
print(float)
float += 2
print(float)
print(round(float))

print(2/4)
print(5.5%2) # 2 fits into 5.5 2 times. The remainder is 1.5.

print(type(5.5%2)) ## 2 fits into 5.5 2 times. The remainder is 1.5 which is a float
print(type(2/4)) # (2/4) = 0.5 is a float type ; Not an int
print(type(5.0001))
print(type(20+1.1))

# # any time decimals are added the result will always be a float
# # even a number that ends in a .0 is considered a float
# print(type(9.9+1.1)) # (9.9+1.1) = 11.0 which is a floating point number
print(round(3.1)) # rounds down to 3
print(round(3.49)) # rounds down to 3
print(round(3.5)) # rounds up to 4
print(round(3.9)) # rounds up to 4

Operator Precedence [PEMDAS (Order of Operations) -> # Parenthesis; Exponents; Multiplication & Division; Addition & Subtraction]
PEMDAS -> () ; ** ; * ; / ; + ; -
print(20 - 3 * 4) # = 20-(12) = 8
print((20-3) * 4) # = 17 * 4 = 68

bin #binary number
print(bin(5))
print(int('0b101', 2))

Variables: 
- Store information that can be used in programs
- are custom Names or labels that reference objects in memory
- start with lowercase or underscore
- can have letters, numbers or underscores
- variables are case sensitive 
- name variables well


user_iq = 190 
a = user_iq
print(user_iq)
print(a)

#rapidly assign variables
a,b,c = 1,2,3
print(a,b,c)

# Constants -> values that never change in a program
# Convention for naming constants is to use all Caps (Capitals/Uppercase Letters)

PI = 3.14
print(PI)

# Statement -> Entire Line of Code
user_age = user_iq/5    # the statement
# user_age is the variable
# user_iq/5 is the expression in the statement
# Expression -> Piece of code that produces a value


# Augmented Assignment Operator
#   +=  -=  *=  /=

some_value = 5 # variable some_value has been assigned the value 5
some_value += 2 # variable some_value has been augmented +2
print(some_value) #7
some_value -= 2 # variable some_value has been augmented -2
print(some_value) #5
some_value = 5 + 2
print(some_value)  #7
some_value = some_value + 2 
print(some_value) #9
some_value *= 2 # variable some_value has been augmented *2
print(some_value) #18
some_value /= 2 # variable some_value has been augmented /2
print(some_value) #9
int = 5
print(int)
int += 2
print(int)

float = 3.2
print(float)
float += 2
print(float)
print(round(float))



str # string ['' or ""] ; piece of text (word, phrase, sentence, etc)
# strings can include any character types (letters, numbers, spec. characters, etc) 

'hi hello there'
"hi hello there"
'hi gimme a hi5'
print(type("High5!"))

username = 'supercoder'
password = 'supersecret'

#sting concatenation -> concatenate or add strings together
account_info = 'Account [' + 'Username: ' + username + ' | ' + 'Password: ' + password + ']' 
print(account_info)

# long string [''' ''' or """ """] allows us to string multiple lines together
long_string = """    
WOW
0 0
---
"""
print(long_string)


# Type Conversion -> Converting data from one type to another
print(str(100)) # -> 100 [Integer has been converted into a string]
print(type(str(100))) # -> type is string 
print(type(int(str(100)))) # -> type is integer [String has been converted back to an integer]

a = str(100) # -> 100 [Integer (original type) has been converted into a string]
b = int(a) # -> [String has been converted back to an integer]
c = (type(b)) # -> type is integer 

print(a)
print(type(a))
print(c)

# Escape Sequence
weather = "It\'s \"kind of\" sunny"
print(weather)

# weather = "It\\'s \"kind of\" sunny"
print(weather)

# \t will add a Tab to spacing
weather = "\t It\'s \"kind of\" sunny"
print(weather)

# \ will add a new line
weather = "\n It\\'s \"kind of\" sunny"
print(weather)


# Formatted Strings -> f strings [python3 feature]

name = 'Johnny'
age = 55

print('hi ' +  name + '. You are ' + str(age) + ' years old.')
# Can't concatenate integers; only can concatenate strings | Type convert integers to strings
# age - an integer (55) is type converted into a string

print(f'hi {name}. You are {age} years old.')
# f -> creates formatted string format ; a python 3 feature
# allows us to simplify inclusion of variables in strings


# String Indexes

'me me me'  #   me me me is stored in an (8-digit) index [0,7]
            #  [01234567] including the spaces, the string me me me is 8 digits

selfish = 'me me me'

# [index]
print(selfish[0]) #prints m
print(selfish[5]) #prints    (empty because of space)
print(selfish[7]) #prints e

# [start:stop]
print(selfish)  # prints me me me
print(selfish[0:7])     # [start:stop] will print out everything except 7th index
print(selfish[0:8])             #      will print out everything in an 8-digit index

# [start:stop:stepover]
print(selfish[0:8:1])   # [start:stop:stepover]  will stepover 1 digit
print(selfish[0:8:2])   # will stepover 2 indexes

# [start:]
print(selfish[0:]) # does not stop; default will go to the end(prints everything)

# [:stop]
print(selfish[:8]) # starts at default 0 (prints everything)

# [::stepover] aka String Splicing
print(selfish[::1]) # default starts at 0: runs till end by default: iterates over each index
    # will print out everything in order from first to last index me me me
print(selfish[::-1]) # # default starts at the end index: runs till end by default: iterates over each index
    # will print out everything backwards from last to first index em em em

# Negative Indexes
print(selfish[-1]) # -1 will make sequence start at the end index (prints e)
print(selfish[-2]) # -2 will make sequence start at the 2nd to last index (prints m)
print(selfish[-3]) # -3 will make sequence start at the 3rd to last index (prints )
print(selfish[-8]) # -8 will make sequence start at the 1st index of an 8-digit index (prints m
print(selfish[::-1]) # # default starts at the end index: runs till end by default: iterates over each index
    # will print out everything backwards me me me


# Immutability - objects (strings, integers, floats, tuples) in python are immutable (unchangeable)
# we can override their data, but we cannot change it

selfish = 100
print(selfish)

# selfish[0] = 8 # will output "TypeError: 'int' object does not support item assignment"
# print(selfish) # objects are immutable -> selfish cannot be altered
# selfish = 800   # selfish cannot be redefined (it is immutable)
# print(selfish)

selfish += 700  # selfish can be redefined but not reassigned
print(selfish)
print(type(selfish)) # selfish is an integer type


# Built-In Functions (highlighted in yellow) syntax -> function()
# [show up as purple boxes in VS code]
# functions perform actions on data
# https://docs.python.org/3/library/functions.html

# str()
# int()
# len()
# print()
# len()

greet = 'helloooo'  # 8 digit index [0,7]
    #   [01234567]

print(greet[0:5])   # includes everything from [0:4] or hello (first 4 letters)
print(greet[0:8])   # [start:stop] slice notation (end index is exclusive)
print(greet[0:len(greet)])  #  = [0:8]
print(len(greet))   # len(greet) = 8
print(len(greet[7]))



# Built-In Methods [show up as purple boxes in VS code]

# String Methods - methods that only strings can perform

# .format()
# .upper()
# .lower()
# .capitalize()
# .find()

quote = 'to be or not to be'
print(quote.upper())    # .upper() makes every letter uppercase
# prints TO BE OR NOT TO BE
print(quote.lower())    # .upper() makes every letter lowercase
# prints to be or not to be
print(quote.capitalize())   # .capitalize will capitalize the first letter only
# prints To be or not to be

print(quote.find('be')) # .find() will find the index location of the first letter in a string
# prints 3 ; 'be' starts at the 3rd index (where b (the first letter in be) is located)

print(quote.replace('be', 'me')) # .replace() will replace a string with another
# prints to me or not to me ; 'be' is swapped for 'me'

print(quote)  # prints to be or not to be
# will print original string value of quote ; strings are immutable (can't be modified)

quote2 = quote.replace('be', 'me')  # creating a new string ; can't modify old string
print(quote2)


# Booleans [True (1) or False (0)] ; Conditional Logic

bool
name = 'Madhav'
is_cool = False
is_cool = True

print(bool(1))  # prints True
print(bool(0))  # prints False

print(bool(True)) 
print(bool(False)) 


name = 'Andrei Neagoie'
age = 50
relationship_status = 'single'

relationship_status = "it's complicated"
print(relationship_status)


birth_year = input('What year were you born?')
age = 2024 - int(birth_year) # Type Conversion -> int(birth_year)
# birth_year is a string type input which needs to be converted into an integer input in order to do a math operation
print(f'You are {age} years old')

'''

'''
Commenting Best Practices - https://realpython.com/python-comments-guide/
Be concise when writing comments ; Most of your code should be easily readable and easily explainable ; You should have mostly clean code and a few comments only when necessary (comment complex code). For example, use comments 
to outline a function in pseudo code.
'''

# Exercise: Password Checker

input('jayjay')
input('secret')

print('password {pass} is {pass_length} long')

list
tuple
set
set
dict

#Classes -> Custom Types

#Specialized Data Types

None # 0 ; null




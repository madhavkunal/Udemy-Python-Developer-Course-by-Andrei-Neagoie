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

# \n will add a new line
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


# Slicing -> feature that can extract parts of sequences such as strings, lists, and tuples. slicing syntax is -> sequence[start:stop:step].

# [start:stop]
print(selfish)  # prints me me me
print(selfish[0:7])     # [start:stop] will print out everything except 7th index
print(selfish[0:8])             #      will print out everything in an 8-digit index

# [start:stop:step]
print(selfish[0:8:1])   # [start:stop:step]  will step through every single digit (1)
print(selfish[0:8:2])   # will step through every second digit (2)

# [start:]
print(selfish[0:]) # does not stop; default will go to the end(prints everything)

# [:stop]
print(selfish[:8]) # starts at default 0 (prints everything)

# [::step] 
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


# Exercise: Password Checker

username = input('Username: ')
password = input('Password: ')
pass_length = len(password)
pass_stars = ('*' * pass_length)

print(f'{username}, your password {pass_stars} is {pass_length} digits long')


# Data Structure 
# Data structures are containers that hold data

# List - Ordered Sequence of Objects 
# lists are a type of data structure

list # in python lists are like arrays

li = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

li[0] = 69  # *Lists are not immutable! ; they can be altered
print(li)   # prints [69,2,3,4,5]



# List Slicing

    # List Modification

# amazon_cart = [
#                 'notebooks',
#                 'sunglasses',
#                 'toys',
#                 'grapes'
#             ]

# remember that the stop index is excluded

# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart
# new_cart[0] = 'gum'  # 'gum' is now located at [0] in both new_cart & amazon_cart
# # because unlike strings, lists are NOT immutable (they can be modified)

# print(new_cart)     # prints ['gum', 'sunglasses', 'toys', 'grapes']
# print(amazon_cart)  # prints ['gum', 'sunglasses', 'toys', 'grapes']

    # list copying

# amazon_cart = [
#                 'notebooks',
#                 'sunglasses',
#                 'toys',
#                 'grapes'
#             ]

# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[:] # new_cart is using list splicing to copy amazon_cart
# # new_cart is a new list in this case while amazon_cart maintains original values
# new_cart[0] = 'gum'  # 'gum' is now located at [0] in new_cart

# print(new_cart)     # prints ['gum', 'sunglasses', 'toys', 'grapes']
# print(amazon_cart)  # prints ['', 'sunglasses', 'toys', 'grapes']

# amazon_cart = [
#                 'notebooks',
#                 'sunglasses',
#                 'toys',
#                 'grapes'
#             ]
# print(amazon_cart[0::2])    # [start:stop:step] ; prints ['notebooks', 'toys']
# print(amazon_cart)      # prints ['notebooks', 'sunglasses', 'toys', 'grapes']

# amazon_cart[1] = 'shades' # In lists you can modify variables unlike in strings
# print(amazon_cart)      # prints ['notebooks', 'shades', 'toys', 'grapes']
# new_cart = amazon_cart[0:3] # prints ['notebooks', 'shades', 'toys']
# print(new_cart)
# new_cart[0] = 'binder' # prints ['binder', 'shades', 'toys'] 
# print(new_cart)
# print(amazon_cart[1:3]) # prints ['shades', 'toys'] 
# # starts at shades, stops at toys (toys is excluded)

'''
'''
# Matrix -> Two-Dimensional Array  # collection of values arranged in rows and columns

# matrix is not a built-in data type ; it belongs to the 'list' class

# created using numpy.array() function that converts a list of lists (2 arrays) and converts it into a matrix

# matrices are commonly used in scientific computing/Data Science/Machine Learning

matrix = [
    [1,2,3],    # sub array
    [4,5,6],    # make sure to put comma after each sub array
    [7,8,9]
]

# [start:stop:step] Remember that stop excludes the stop value (is one index ahead of the final value in an array)! Indexing starts at 0 ; [0] corresponds to first array 
# [2] corresponds to last array ; when slicing
# must use [3] at the stop to include [2]

print(matrix[0:3]) # will print entire matrix

print(matrix[0][1]) # prints 2 ; is printing the 2nd value [1] of the 1st array [0]

print(matrix[0]) # prints [1, 2, 3] ; is printing the 1st array [0]

print(matrix[2][2]) # prints 9 ; is printing the 3rd value [2] of the 3rd array [2]

print(matrix[::])

# a list is an array in python
# a list is an array in python

# Nested Indexing

# using this list: 
# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

# print(basket[1][1])
# print(basket[1][1][0])

# -  basket[1]  accesses the second element of the outer list, which is another nested list. 
#  -  basket[1][1]  accesses the second element of the inner nested list, which is another nested list. 
#  -  basket[1][1][0]  accesses the first element of the innermost nested list, which is the string "Oranges". 

''' ''' 


# List Methods [Modify a List IN PLACE] / Do NOT create a new copy of a List

basket = [1,2,3,4,5]
#append method -> appends object to the end of a list IN PLACE (does NOT create a new copy of the list)
basket.append(100)   # modifies basket / appends 100 after 5
new_list = basket   # new_list is assigned to basket
print(basket)       # prints [1, 2, 3, 4, 5, 100]
print(new_list)     # prints [1, 2, 3, 4, 5, 100]


basket = [1,2,3,4,5]
#insert method -> inserts object before index of a list IN PLACE (does NOT create a new copy of the list)
basket.insert(4,100)    # modifies basket / inserts 100 before index [4] or before 5
new_list = basket   # new_list is assigned to basket
print(basket)       # prints [1, 2, 3, 4, 5, 100, 5]
print(new_list)     # prints [1, 2, 3, 4, 5, 100, 5]

basket = [1,2,3,4,5]

#extend method -> Give the value/s to add to the end of the list
basket.extend([6, 7])  # modifies basket / appends 6 and 7 after 5
print(basket)   # prints [1, 2, 3, 4, 5, 6, 7] 

#pop method ->  Give the index to remove
basket.pop()     # removes the last element of the list
print(basket)    # prints [1, 2, 3, 4, 5, 6]

basket.pop(0)   # removes the first element of the list
print(basket)   # prints  [2, 3, 4, 5, 6]

#remove method -> Give the value to remove
basket.remove(3) # removes 3 
print(basket)    # prints [2,4,5,6]

new_list = basket.pop()     # removes 6 
print(new_list)    # prints 6
print(basket)      # prints (2,4,5)
new_list = basket
print(new_list)    # prints (2,4,5)

#clear method ->    # clears everything in the list 
basket.clear()      
print(basket)       # prints an empty list -> []

basket = [1,2,3,4,5]    # index locations = [0,1,2,3,4] *reminder: indexing starts at [0]!
#index method -> Give the value to see it's index location
print(basket.index(2))  # prints '1' because 2 is located at the 1st index

basket2 = ['a', 'b', 'c']    # index locations = [0,1,2] *reminder: indexing starts at [0]!
#index method -> Give the value to see it's index location
print(basket2.index('c'))  # prints '2' because 'c' is located at the 2nd index

# Keywords -> Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers. Examples: in  true  false

list = ['a', 'b', 'c', 'e', 'e'] 
print('c' in list)      # prints True because 'c' is indeed in the list
print('d' in list)      # prints False because 'd' is not in the list
print(list.count('d'))  #prints 0 because no occurences of 'd'
print(list.count('a')) #prints 1 because one occurence of 'a'
print(list.count('e')) #prints 2 because two occurences of 'e'

# Exercise List Methods
# SCROLL FOR ANSWERS!
# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
basket.remove("Banana")
print(basket)
# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")
print(basket)
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
print(basket)
# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")
print(basket)
# 5. Count how many apples in the basket
print(basket.count("Apples"))

# 6. empty the basket
basket.clear()
print(basket)

# Sort Method -> sorts the list IN PLACE alphanumerically

basket = ['a','b','c','d','e','d']
print(basket)
basket.sort() # (alphabetically sorts the list)
#prints basket = ['a','b','c','d','d','e']
print(basket)

basket2 = [8,7,6,5,4,3,2,1]
print(basket2)
basket2.sort() # (numerically sorts the list)
#prints basket2 = [1,2,3,4,5,6,7,8]
print(basket2)

 
#Sorted Method -> sorted produces a new alphanumerically sorted list (does not modify original list)

bucket = ['a','d','p','b','c','l','o','e']
print(bucket) #prints ['a', 'd', 'p', 'b', 'c', 'l', 'o', 'e']

print(sorted(bucket)) #prints ['a', 'b', 'c', 'd', 'e', 'l', 'o', 'p']

sortedbucket = sorted(bucket)
print(sortedbucket)
# prints ['a', 'b', 'c', 'd', 'e', 'l', 'o', 'p'] | prints sorted bucket

print(bucket) #prints ['a', 'd', 'p', 'b', 'c', 'l', 'o', 'e'] | prints original unsorted bucket

# Reverse Method -> reverses the order of a list in Place (modifies the original list)

array = [1,2,3,4,5]
array.reverse()
print(array)  # prints [5, 4, 3, 2, 1]

array2 = [3,2,9,8]
array2.reverse()
print(array2)  # prints [8, 9, 2, 3]


array3 = ['z','y','x','a','b','c']
array3.reverse()
print(array3)  # prints ['c', 'b', 'a', 'x', 'y', 'z']
print(array3[::-1]) # prints ['z', 'y', 'x', 'a', 'b', 'c']

# Range Function -> generates a sequence of numbers
print(range(1,100))
Range = range(1,100)
print(Range)
print(list(Range)) # prints a list of numbers from 1 to 99


# Join Method -> joins a list of strings into a single string

sentence = ' ' # empty string
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Madhav'])
print(new_sentence) # prints hi my name is Madhav

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend) # adds Stanley to the end of the list
print(sorted(friends)) # prints ['Amira', 'Carrie', 'Chu', 'Joy', 'Patty', 'Simon', 'Stanley']


# List Unpacking -> allows us to assign each value in a list to a variable

a,b,c,d,e = [1,2,3,4,5]
print(a) # prints 1
print(a,b,c,d,e) # prints 1 2 3 4 5


a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a,b,c) # prints 1 2 3 | each value is unpacked and assigned to a variable
print(other) # prints [4, 5, 6, 7, 8] | the rest of the values between c and d are assigned to the variable 'other'
print(d) # prints 9 | the last value is assigned to the variable 'd'


None    # 0 ; null ; tje absence of a value

weapons = None
print(weapons)


# Dictionary is a collection of unordered key-value pairs | Dictionary is a data type and data structure in Python
dict

dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary) # prints {'a': 1, 'b': 2}
print(dictionary['a']) # prints 1
print(dictionary['b']) # prints 2
# print(dictionary['c']) # prints KeyError: 'c' ; 'c' is not in the dictionary


dictionary2 = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}

print(dictionary2['a']) # prints [1, 2, 3]
print(dictionary2['b']) # prints hello
print(dictionary2['x']) # prints True
print(dictionary2) # prints {'a': [1, 2, 3], 'b': 'hello', 'x': True}


dictionary3 = {
    'weaponset': 'pistol',
    'ammunition': 100,
    'armor': 'vest',
    'loadout': [1,2,3]
}

print(dictionary3) # prints {'weaponset': 'pistol', 'ammunition': 100, 'armor': 'vest'}

print(dictionary3['weaponset']) # prints pistol
print(dictionary3['loadout'][2] ) # prints 3 ; prints the 3rd value in the list 'loadout'
print(dictionary3['loadout'][0]) # prints 1 ; prints the 1st value in the list 'loadout'


dictionary4 = {
    123: [1,2,3],
    True: 'hello',
    'x': True,
}

print(dictionary4[123]) # prints [1, 2, 3]
print(dictionary4[True]) # prints hello
print(dictionary4['x']) # prints True
print(dictionary4) # prints {123: [1, 2, 3], True: 'hello', 'x': True}


dictionary5 = {
    '123': [123],
    '123': 'hello'
}

print(dictionary5['123']) # prints hello
print(dictionary5) # prints {'123': 'hello'} ; the second key '123' overwrites the first key '123'

#Dictionary keys must be unique ; if you have two keys with the same name, the second key will overwrite the first key
#Dictionary keys must be immutable ; keys must be unique and immutable (unchangeable) ; keys can be strings, numbers, booleans or tuples

#Dictionary Methods

dictionary6 = {
    'basket': [123],
    'greet': 'hello',
}

dictionary7 = {
    'basket': [123],
    'greet': 'hello',
    'age': 20
}

#Dictionary Methods

print(dictionary6.get('age'))  # prints None ; age is not in the dictionary
print(dictionary6.get('age', 55))  # prints 55 ; age is not in the dictionary so 55 is the default value
print(dictionary7.get('age'))  # prints 20 ; age is in the dictionary

user = dict(name='John')
print(user) # prints {'name': 'John'}

dictionary7 = {
    'basket': [123],
    'greet': 'hello',
    'age': 20
}

print('basket' in dictionary7) # prints True ; 'basket' is in the dictionary    
print('size' in dictionary7) # prints False ; 'size' is not in the dictionary
print('age' in dictionary7.keys()) # prints True ; 'age' is in the dictionary
print(20 in dictionary7.values()) # prints True ; 20 is in the dictionary
print(dictionary7.items()) # prints dict_items([('basket', [123]), ('greet', 'hello'), ('age', 20)]) ; prints all the items in the dictionary
print(dictionary7) # prints {'basket': [123], 'greet': 'hello', 'age': 20}
#print(dictionary7.clear()) # prints None ; clears everything in the dictionary
#dictionary7.clear() # clears everything in the dictionary


dictionary8 = {
    'basket': [123],
    'greet': 'hello',
    'age': 20
}

dictionary9 = dictionary8.copy() # prints a copy of the dictionary
dictionary8.clear()
#print(dictionary8) # prints {}
#print(dictionary9) # prints {'basket': [123], 'greet': 'hello', 'age': 20}
print(dictionary9.pop('age')) # prints 20 ; removes age from the dictionary and returns the value of age
print(dictionary9) # prints {'basket': [123], 'greet': 'hello'}
print(dictionary9.popitem()) # prints ('greet', 'hello') ; removes an arbitrary item in the dictionary; in this case it removes basket

#dictionaries are unordered ; the order of the items in the dictionary is not guaranteed

print(dictionary9.update({'age': 55})) # prints None ; adds age to the dictionary
print(dictionary9)

print(dictionary9.update({'name': 'Rick'})) # prints None ; adds name to the dictionary

print(dictionary9) # prints {'basket': [123], 'age': 55, 'name': 'Rick'}

# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user = {
  'age': ' ',
  'username' : ' ',
  'weapon': ' ',
  'is_active': ' ',
  'clan': ' '
}

# 2 iterate and print all the keys in the above user.
print(user)

# 3 Add a new weapon to your user
user.update({'weapon': 'katana'})

# 4 Add a new key to include 'is_banned'. Set it to false
user.update({'is_banned': False})

# 5 Ban the user by setting the previous key to True
user.update({'is_banned': True})

# 6 create a new user2 my copying the previous user and update the age value and username value.

user2 = user.copy()
user2.update({'age': '55', 'username' : 'Kenshi'})
print(user2)


tuple # ordered immutable collection of objects; tuples do not support item assignment (tuples cannot be changed)

my_tuple = (1,2,3,4,5)
print(my_tuple[1]) # prints 2
print(5 in my_tuple) # prints True

dict9 = {
    'basket': [123],
    'greet': 'hello',
    'age': 20
}

print(dict9.items()) # prints dict_items([('basket', [123]), ('greet', 'hello'), ('age', 20)]) ; prints all the items in the dictionary as a tuple

# [start:stop:step] Remember that stop excludes the stop value (is one index ahead of the final value in an array)! Indexing starts at 0 ; [0] corresponds to first value

new_tuple = my_tuple[1:2] # prints (2,) ; prints a tuple with one value

print(new_tuple) # prints (2,) ; prints a tuple with one value
new_tuple = my_tuple[1:4] # prints (2, 3, 4) ; prints a tuple with three values
print(new_tuple) # prints (2, 3, 4) ; prints a tuple with three values


x,y,z, *other = (1,2,3,4,5,5,5,5)
print(x) # prints 1
print(y) # prints 2
print(z) # prints 3
print(other) # prints [4, 5, 5, 5, 5]
print(x,y,z) # prints 1 2 3

print(x,y,z, *other) # prints 1 2 3 4 5 5 5

Tuple = (1,2,3,4,5,5,5) 
print(Tuple.count(3))
print(Tuple.index(3)) # prints 2
print(Tuple.count(5)) # prints 3
print(Tuple.index(5)) # prints 4
print(len(Tuple)) # prints 7 


set # unordered collection of unique objects ; sets do not support indexing ; sets do not support duplicate values

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set) # prints {1, 2, 3, 4, 5}
print(your_set) # prints {4, 5, 6, 7, 8, 9, 10}

my_set2 = {1,2,2,2}
print(my_set2) # prints {1, 2} ; prints a set of unique values ; 2 is not repeated ; no duplicates ; the other 2's are ignored and not added to the set

my_set.add(100)
my_set.add(2)
print(my_set) # prints {1, 2, 3, 4, 5, 100} ; 2 is not repeated ; no duplicates ; the other 2 is ignored and not added to the set


my_list = [1,2,3,4,5,5,5]
print(my_list) # prints [1, 2, 3, 4, 5, 5, 5] ; 5 is repeated ; duplicates are allowed in a list
print(type(my_list)) # prints <class 'list'> ; my_list is a list type
my_set = set(my_list) # type converts my_list into a set 
print(my_set) # prints {1, 2, 3, 4, 5} ; prints a set of unique values ; 5 is not repeated ; no duplicates ; the other 5's are ignored and not added to the set
print(type(my_set)) # prints <class 'set'> ; my_set is a set type
print(1 in my_set) # prints True ; 1 is in the set

my_set = list(my_set) # type converts my_set into a list
print(my_set) # prints [1, 2, 3, 4, 5] 
my_set = set(my_set) # type converts my_set back into a set
print(my_set)
new_set = my_set.copy() # creates a copy of my_set
print(new_set) # prints {1, 2, 3, 4, 5}
my_set.clear() # clears everything in the set
print(my_set) # prints set() ; an empty set
print(new_set) # prints {1, 2, 3, 4, 5}

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) # prints {1, 2, 3} ; prints the difference between my_set and your_set ; 1-3 are unique to my_set ; 4-5 are shared between both sets
print(your_set.difference(my_set)) # prints {6, 7, 8, 9, 10} ; prints the difference between your_set and my_set ; 6-10 are unique to your_set ; 4-5 are shared between both sets

#print(my_set.discard(5)) # prints None ; removes 5 from my_set
#print(my_set) # prints {1, 2, 3, 4} ; 5 is removed from my_set

#print(my_set.difference_update(your_set)) # prints None ; removes 4-5 from my_set   
#print(my_set) # prints {1, 2, 3} ; 4-5 are removed from my_set

#print(my_set.intersection(your_set)) # prints {4, 5} ; prints the intersection between my_set and your_set ; 4-5 are shared between both sets

#print(my_set.isdisjoint(your_set)) # prints False ; my_set and your_set have shared values ; 4-5 are shared between both sets

#print(my_set.union(your_set)) # prints {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} ; prints the union of my_set and your_set ; 1-10 are all the unique values in both sets

#print(my_set | your_set) # prints {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} ; prints the union of my_set and your_set ; 1-10 are all the unique values in both sets

#print(my_set & your_set) # prints {4, 5} ; prints the intersection between my_set and your_set ; 4-5 are shared between both sets

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.issubset(your_set)) # prints True ; my_set is a subset of your_set ; 4-5 are shared between both sets
print(your_set.issubset(my_set)) # prints False ; your_set is not a subset of my_set 

print(my_set.issuperset(your_set))  # prints False ; my_set is not a superset of your_set  
print(your_set.issuperset(my_set)) # prints True ; your_set is a superset of my_set ; 4-5 is included in your_set   


# Exercise Set Methods

# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

print(school.difference(attendance_list))


#using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!


'''

#Classes -> Custom Types

#Specialized Data Types

None # 0 ; null
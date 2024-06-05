""" Functional Programming 


Object-Oriented Programming (OOP):

Strengths:
- Well-suited for modeling complex systems with many interacting objects.
- Promotes good code organization and modularity.
- Easier for beginners to grasp due to its familiarity in most programming languages.
- Can be more efficient for managing state and data changes.

Weaknesses:
- Can lead to tightly coupled code that's harder to test and maintain, especially in large projects.
- Overuse of inheritance can create complex hierarchies and make debugging difficult.
- Not always the best choice for simpler tasks or data-intensive applications.


Functional Programming (FP):

Strengths:
- Encourages immutable data and pure functions, leading to more predictable and testable code.
- Easier to parallelize operations for better performance in data-intensive tasks.
- Promotes writing smaller, reusable functions that are easier to understand and maintain.

Weaknesses:
- Can be more challenging to learn and master for those new to the paradigm.
- Not always the best choice for modeling complex systems with state changes.
- Might require additional libraries and frameworks for certain tasks.


- Here are some additional factors to consider:
* Project complexity: For complex systems with multiple interacting entities, OOP might be more natural. But for simpler tasks or data-intensive applications, FP could be a better fit.
* Team preferences: If your team has experience with a specific paradigm, it might be easier to stick with it for collaboration and knowledge sharing.

Object Oriented Programming - Focus on Classes & Objects
Functional Programming - Focus on Data Structures

Both are:
- clear and understandable
- easy to extend
- easy to maintain
- memory efficient
- DRY (Don't Repeat Yourself)


# Functional Programming

# Pure Functions-> Given the same input, the result should always be the same output. Should not produce any side effects. Pure functions are more of a guideline than an absolute.
# map, filter, zip, reduce  // common functions


my_list = [1, 2, 3]


def double(item):
    return item * 2


print(list(map(double, my_list)))

# map() takes the iterable ([1,2,3]) in the second argument and runs the function (double()) in the first argument double
print(my_list)  # prints [1,2,3] since my_list is immutable

# filter()

my_list = [1, 2, 3]

def only_odd(item):
    return item % 2 != 0


print(
    list(filter(only_odd, my_list))
)  # returns a new modified list [1,3] and not 2 since 2 is divisible by 2
print(
    my_list
)  # returns [1,2,3] - original list is not modified since lists are immutable


# filter() filters through the iterable and runs the preceding function. If the result is true, it return's the item, and if the result is false, it does not return the item.


# zip() -> zips or pairs items (with the same index in multiple of the same object types such as lists) in a tuple.

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [5, 4, 3]

print(my_list)
print(your_list)
print(their_list)

print(list(zip(my_list, your_list)))
print(list(zip(my_list, your_list, their_list)))


# reduce()

from functools import reduce

my_list = [1, 4, 7]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(my_list)

print(reduce(accumulator, my_list, 10))

# prints:
        # accumulator starts off with 10 (value given in reduce() func)   it then accumulates or adds itself to the items in the list:

10 1    acc = 10   1-first item in list  | 10 + 1 | acc = 11
11 4    acc = 11   4-second item in list | 11 + 4 | acc = 15
15 7    acc = 15   7-third item in list  | 15 + 7 | acc = 22
22

from functools import reduce

# map, reduce, zip, acc

# 1 Capitalize all of the pet names and print the list - DONE
my_pets = ["sisi", "bibi", "titi", "carla"]

CapList = [x.title() for x in my_pets]
print(CapList)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest. - DONE
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()
print(my_numbers)

print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%

scores = [73, 20, 65, 19, 76, 100, 88]


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
    return acc + item
    print(acc, item)


print(reduce(accumulator, my_numbers, scores))


from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]


def capitalize(string):
    return string.upper()


print(list(map(capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))



# lambda expressions - single use functions

from functools import reduce

my_list = [1, 2, 3]  # -> list is immutable
print(my_list)
print(list(map(lambda item: item * 2, my_list)))  # this lambda expression (* 2) will only be performed one time
print(reduce(lambda acc, item: acc+item, my_list))


# Challenge 1 - Lambda expression that squares my_list
my_list = [5,4,3]

print(list(map(lambda item: item*item, my_list)))


# Challenge 2 - List Sorting -> sort tuples based on their second value in ascending order
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])  # -> sorts tuples based on the second key value
print(a)



my_list = []

for char in 'hello':
  my_list.append(char)

print(my_list)  # my_list = ['h', 'e', 'l', 'l', 'o']


# list comprehension

my_list2 = [char for char in 'hello']
my_list3 = [num for num in range(0,101)]
my_list4 = [num*2 for num in range(0,101)]
my_list5 = [num**2 for num in range(0,101) if num % 2 == 0] #if the number in the list is an even number, than square it, leave the odd numbers as is


print(my_list2) #my_list2 = ['h', 'e', 'l', 'l', 'o']
print(my_list3) #my_list3 = [0,1,2,3 ... 99,100]
print(my_list4) #my_list4 = [0,2,4,6 ... 198,200]
print(my_list5) #my_list4 = [0,2,4,6 ... 198,200]


# sets {} only allow unique (non-duplicate) items

dictionary = {
  'a': 1,
  'b': 2
}

my_dict = {key:value**2 for key, value in dictionary.items()}   

#square the dictionary item values (1*1 = 1 ; 2*2 = 4)

print(my_dict)  #prints {'a': 1, 'b': 4}


my_dict = {num:num*2 for num in [1,2,3]}

# num is key : num * 2 is value

print(my_dict)


list = ['a','b','c','b','d','m','n','n']

duplicates = set([x for x in list if list.count(x) > 1])

print(duplicates)

"""

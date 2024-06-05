""" Object Oriented Programming. OOP.

Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects.

Objects are instances of a class. OOP allows the programmer to create their own objects that have methods and attributes. OOP is a paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

print(type(5))
print(type(5.0))
print(type('5'))
print(type([]))
print(type(()))
print(type({}))
print(type(True))
print(type(False))
print(type(None))
print(type(type))
print(type(print))
print(type(int))
print(type(float)) 
print(type(str))
print(type(list))
print(type(tuple))
print(type(dict))
print(type(bool))
print(type(type))
print(type(set))

Objects allow for the reuse of code and the ability to build more complex programs. Objects are models of real world objects. Objects are modular and can be used to build larger applications.


# Classes are a way to bring together data and functionality. The class keword is used to create a new class. The class is the blueprint for the object that will be created. Instances of the class are objects that are created from the class.

# Class names are conventionally written in CamelCase (first letter of each word is capitalized)

class BigObject:
    pass

print(type(BigObject))  # <class 'type'>

obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()

print(type(obj1))  
print(type(obj2))
print(type(obj3))
# <class '__main__.BigObject'> is printed for each object. This is the class that the objects were created from.


#   _init_ is a constructor method

class PlayerCharacter:  # class is an object constructor. PlayerCharacter is the constructor class for player objects.
    membership = True   # class object attribute (static - will not change throughout different instances)
    def __init__(self, name, age, attack):  # __init__ is a special method - a constructor method that "INstantIaTes" or makes an instance (self) of a class
        if self.membership is True:     # if player has membership
            self.name = name        # object.property = attribute   (class attribute) 
            self.age = age          # object.property = attribute   (class attribute)
            self.attack = attack    # object.property = attribute   (class attribute)
            # class attributes are dynamic and can change across instances

    def run(self):  # run is a method of object self. To call: self.run()
        return 'run'   # prints 'run'    *If we have no return statement, then it prints 'None'

    def intro(self):   # intro is an object method 
        print(f'my name is {self.name}')

    @classmethod  # function decorator -> converts a function into a class method
    # class methods are dynamic with class state (cls as first param)
    def sumFunc(cls, num1, num2):   # first parameter is cls -> class (PlayerCharacter)
        return num1 + num2

    @staticmethod # converts a function into a static method 
    # static methods are used when we don't care about the class state
    def multFunc(num1, num2):
        return(num1 * num2)

player1 = PlayerCharacter('Cindy', 31, 50)  # paramaters are (name, age, attack)
# object1 = class(attribute, attribute, attribute)   object1 is first instance of class PlayerCharacter with attributes of name: Cindy and age: 31

player2 = PlayerCharacter('John', 23, 110)  # paramaters are (name, age, attack)
# object2 = class(attribute, attribute)   object2 is second instance of class PlayerCharacter with attributes of name: John and age: 23

print(PlayerCharacter.sumFunc(4,3)) # prints 7  sumFunc() is called on the class
#sumFunc() is a class method that can be called on the class or on the instance

print(PlayerCharacter.multFunc(45,6))

print(player1)    # prints <__main__.PlayerCharacter object at x000001D9017BA090>
print(player1.name) # prints Cindy
print(player1.age)  # prints 31
print(player1.attack) # prints 50
print(player1.run) # prints <bound method PlayerCharacter.run of <__main__.PlayerCharacter object at 0x00000250E33BA600>>
print(player1.run()) # prints run 
print(player1.intro()) # prints My name is Cindy

print(player1.sumFunc(2,2)) # prints 4      sumFunc() is called on the instance
print(player1.membership)   # prints True (static -> doesn't change across instances)
#help(player1)

'''
print(player2)   # prints <__main__.PlayerCharacter object at 0x000001C43DC3A390>
print(player2.name) # prints John
print(player2.age) # prints 23
print(player2.attack) # prints 110
print(player2.run) # prints <bound method PlayerCharacter.run of <__main__.PlayerCharacter object at 0x00000250E33BA630>>
print(player2.run()) # prints run
print(player2.intro()) # prints My name is John
print(player2.membership)
#help(player2)

# player1 and player2 are 2 seperate objects of the PlayerCharacter class and have different locations in memory


# Exercise Cats Everywhere
# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*age):  # define function oldest_cat() that passes in age arguments (different ages)
    return max(age)    # iterate through the ages and return the maximum age


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

                    # run the oldest_cat() function and pass in cat age arguments (ages of all cats)
                    # oldest_cat() runs and prints the maxium age
                    # Oldest Cat is 7 years old.

# 4 Pillars of OOP

# 1. Encapsulation - Encapsulating (Binding) of data (attributes) and functions (methods) into a single class object. Classes create a blueprint for us to spawn multiple instances of an object. Allows us to create modular (reusable) code blocks.

# 2. Abstraction - Abstracting (Hiding) unnecessary, complex and/or excessive information and only showing information that is necesssary, readable, excess and concise. In code, abstraction creates minimalism and simplicity allowing us to focus on what we need to know without worrying about endless behind-the-scenes information on how each thing is implemented at lower levels of code. Lower levels of code (such as machine or binary code) are abstracted away from us and we just need to know and interact with higher level coding languages that we can easily understand and efficiently program with.

# 3. Inheritance - (Children) objects and subclasses (Derived Classes) inherit methods, attributes and functionality from their (Parent) class. Objects, subclasses and classes inherit methods, attributes and built-in functionality called dunder methods from the Base class.

# 4. Polymorphism - Refers to the way that object classes can share the same method names, but the methods will act and output differently based on which objects call them (and the functionality (attributes, data, methods and functionality) they have). Polymorphism is the ability to redefine methods for derived classes.



class User(object):
    def signIn(self):
        print("logged in")

    def attack(self):
        print("attack")


class Wizard(User):  # Wizard class inherits from User class
    def __init__(self, name, spell):
        def attack(self):
            User.attack(self)
            print(f"attacking with {self.spell}")


class Archer(User):  # Archer class inherits from User class
    def __init__(self, name, arrows):
        def attack(self):
            User.attack(self)
            print(f"attacking with power of {self.arrows}")


class HybridBorg(Wizard, Archer):  # Multiple Inheritance
    def __init__(self, name, arrows, power):
        pass


wizard1 = Wizard("Mage King", "Fire Ball")
archer1 = Archer("Robin Hood", "Metal Arrows")

hb1 = HybridBorg("borgie", 50, 100)
hb1.attack()

# print(dir(wizard1))


Introspection - the ability to introspect (examine) objects at runtime
(dynamically inspect various aspects of objects, such as their type, attributes, methods, and even the code that defines them)
with built-in functions (introspection methods) such as:

type(object): Returns the type of an object.
dir(object): Returns a list of names (attributes and methods) defined by an object.
getattr(object, attribute): Gets the value of an attribute from an object.
hasattr(object, attribute): Checks if an object has a specific attribute.
callable(object): Checks if an object is callable (a function).
inspect module: Provides advanced tools for inspecting modules, classes, functions, and more.


print(wizard1.attack())
print(archer1.attack())

# attack methods are both named attack() but they have different functionality based on the class of the object calling the attack() method. This is an example of Polymorphism


 Private Variables -> naming convention is using _ when first naming variables that are meant to be private. Signals to other programmers that variables that are named starting with _ are not meant to be modified or changed.    Ex)  self._name = name

# Dunder Methods -> built in methods where the variables start with __ and end with __


def __init__(a, b, c):
    a.b = b
    a.c = c


class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.dict = {"type": "Marvel Hero"}

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        print("deleted")

    def __call__(self):
        return "called"

    def __getitem__(self, i):
        return self.dict[i]


ironMan = Toy("red", 50)
print(ironMan.__str__())  # Create a new string object from the given object.
print(str(ironMan))
print(len(ironMan))
print(ironMan())
print(ironMan["type"])
del ironMan  #   del - deletes object


class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def sing(self, sing):
        for animal in self.animals:
            print(f"{sing}")


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Simon(Cat):
    pass


class Sally(Cat):
    pass


# 1 Add another Cat
class Tikachu(Cat):
    pass


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []
cat1 = Simon("Simon", 10)
cat2 = Sally("Sally", 15)
cat3 = Tikachu("Tikachu", 5)

my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)

# OR my_cats = [Simon('Simon', 10), Sally('Sally', 15), Tikachu('Tikachu', 5)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
print(my_cats[0:3])
my_pets.walk()
my_pets.sing("purr")

# Python Crash Course Chapter 9 Exercises


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.name}, Cuisine:{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open!")

    def set_number_served(self, number_served):
        print(f"{self.name} has served {self.number_served} customers")

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print(f"{self.name} has served {self.number_served} customers")


class IceCreamStand(Restaurant):

    def __init__(self, name):
        self.name = name
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def display_flavors(self):
        print(self.flavors)


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} has entered")

    def greet_user(self, restaurant):
        print(f"Welcome {self.first_name} {self.last_name} to {restaurant.name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.first_name} has logged in {self.login_attempts} time")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"{self.first_name} has logged in {self.login_attempts} time")


icecreamstand1 = IceCreamStand("Ben & Jerrys")
icecreamstand1.display_flavors()


restaurant = Restaurant("Dunkin", "donuts")
user = User("Paul", "McCarthy")
restaurant.set_number_served(20)  # dynamic value
restaurant.increment_number_served(20)  # dynamic value (user changes)
user.increment_login_attempts()  # attribute specific (method changes)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
print(user.login_attempts)


restaurant1 = Restaurant("Papos", "pizza")
restaurant2 = Restaurant("Giuseppe", "ice cream")
restaurant3 = Restaurant("Ching's", "noodles")

user1 = User("Bob", "Evans")
user2 = User("Larry", "Ellison")
user3 = User("Steve", "Jobs")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

user1.describe_user()
user1.greet_user(restaurant1)
user2.describe_user()
user2.greet_user(restaurant2)
user3.describe_user()
user3.greet_user(restaurant3)


# Exercise: Extending List


class SuperList(list):

    def __len__(self):
        return 1000
        print(1000)


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(super_list1)
print(issubclass(SuperList, list))  # SuperList is a subclass of list (base list)
print(issubclass(list, object))  # list is a subclass of object (base object)

"""

# MRO - Method Resolution Order - The order in which python runs methods


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())


""" A
  /   \ 
B       C
  \   /  
    D """

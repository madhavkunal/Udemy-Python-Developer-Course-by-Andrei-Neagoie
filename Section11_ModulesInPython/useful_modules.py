import datetime
from array import array
from collections import Counter, OrderedDict, defaultdict

# ** Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!

# The Capitalized words Counter and OrderedDict are classes and defaultdict is a function from the collections module (from Python Standard Library)

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = "blah blah blah"
# Counter keeps a count of how many times items are present in an object
print(Counter(li))  # prints Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
print(Counter(sentence))  # prints Counter({'b': 3, 'l': 3, 'a': 3, 'h': 3, ' ': 2})

dictionary = defaultdict(lambda: "does not exist", {"a": 1, "b": 2})
print(dictionary["a"])
print(dictionary["b"])
print(dictionary["c"])

d1 = OrderedDict()
d1["a"] = 1
d1["b"] = 2

d2 = OrderedDict()
d2["a"] = 1
d2["b"] = 2

print(d1 == d2)  # Prints true because the keys and values are the same
print(datetime.time())
print(datetime.time(5, 45, 2))
print(datetime.date.today())

arr = array("i", [1, 2, 3])
print(arr[0])

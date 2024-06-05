import re  # re - is regex module (built-in python module)

string = 'search this inside of this text please!'
pattern = re.compile("this")
pattern_exact = re.compile("search this inside of this text please!")
a = pattern.search(string)
b = pattern.findall(string)
c = pattern_exact.fullmatch(string)
d = pattern.fullmatch(string)
e = pattern.match(string)

#'this' (first match) begins at index 7 and ends at index 11
print(a) # prints <re.Match object; span=(7, 11), match='this'> 
print(a.span())  # prints (7, 11)
print(a.start()) # prints 7
print(a.end())  # prints 11
print(a.group()) # prints this
print(b) # prints ["this", "this"]
print(c)  # prints <re.Match object; span=(0, 39), match='search this inside of this text please!'>
print(d) # prints None
print(e) # prints None

# regex101.com

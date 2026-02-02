import time

#---------FUNCTIONS----------


def mydef(x, y):
    return x + y

print(mydef(1, 2))

# There are four collection data types in the Python programming language:

# 1. List is a collection which is ordered and changeable. Allows duplicate members.
# 2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# 4. Dictionary is a collection which is ordered** and changeable. No duplicate members.

#---------LISTS----------

mylist = [3, 4, 6, 7]
print(mylist[1])

# Remove List Item
mylist.remove(mylist[0])
print(mylist)

# Add list Item
mylist.append(10)
print(mylist)

# Insert item to list at specific index
mylist.insert(1, 5)
print(mylist)

# Loop through list
for i in mylist:
    print(i)

# Loop Through the Index Numbers
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for i in range(len(mylist)):
    print(mylist[i])

print()

#---------TUPLES----------
# Tuples are used to store multiple items in a single variable.
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

mytuple = ("banana", "apple", "orange", "kiwi", "pear", "strawberry")
print("here is mytuple: ", mytuple)

# Change tuple value by converting to list
mylist2 = list(mytuple)
mylist2[1] = "fig"
print("mylist2 is: ", mylist2)
mytuple = tuple(mylist2)
print("my changed tuple is now: ", mylist2)

# Unpacking tuples
(yellow, green, orange, green, green, red) = mytuple
print(green)
print(yellow)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

(yellow, green, *orange) = mytuple
print(orange)
print(yellow)

# Using a while loop on Tuples

i = 0
while i < len(mytuple):
    print("while looping goes like this: ", mytuple[i])
    i = i + 1

# Using for loop on Tuples
for i in range(len(mytuple)):
    print("mytuple is: ", mytuple[i])

# Joining tuples

basicTuple1 = ("Jonny", "Spencer")
basicTuple2 = ("James", "Anna")
basicTuple3 = basicTuple1 + basicTuple2
print("basicTuple3: ", basicTuple3)

# Multiply tuples

basicTuple3 = basicTuple3 * 2
print("Let's double basicTuple3: ", basicTuple3)
print()   




#---------Sets----------
# Sets are used to store multiple items in a single variable.
# Set items are unordered, unchangeable, and do not allow duplicate values.
myset = {"Tupac", "Notorious", "Dre", "Eminem", "Snoop"}
print("Here's my first set", myset)

# A set with strings, integers and boolean values
set1 = {"abc", 34, True, 40, "male"}

# Adding item to set
set1.add(35)
print("Adding 35 to set1: ", set1)

# Adding items from another set into current set
set2 = {"Jonny", 31, False, "Anna", 38, True}
set1.update(set2)
print("adding set1 and set2: ", set1)

# Delete set2
del set2

# Join Sets, note you can join lists/tuples into a set
set2 = {"Angela", 58, True, "Paul", 62, True}

set3 = set1.union(set2)
print("Let's union set1 and set2: ", set3)

# Join multiple sets
# myset = set1.union(set2, set3, set4)

# Updating sets (Is like joining without having to create a new set)
print("Print set1: ", set1)
print("Print set2: ", set2)
set1.update(set2)
print("Updating set1: ", set1)

print()


#---------DICTIONARIES---------
# Dictionary items are ordered, changeable, and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Create a Dictionary (method 1)
mydict = {
    "brand": "Ford",
    "electric": False,
    "model": "Mustand",
    "year": 1964,
    "colours": ["red", "white", "blue"]
    }

print("Printing full mydict: ", mydict)

print("Printing mydict brand: ", mydict["brand"])

# Create a Dictionary (method 2)

mydict1 = dict(Name = "John", age = 40, country = "Belgium")
print("mydict1: ", mydict1)

# Get a dictionary key

print("Getting keys: ", mydict.keys())

# Get a dictionary value
print("Getting values: ", mydict.values())

# Change item value

mydict["electric"] = True
print("my dict is now electric", mydict)

# Add item value
mydict["#doors"] = 4
print("mydict now specifies number of doors: ", mydict)

# Remove item
mydict.pop("model")
print("mydict has no model: ", mydict)

# Loop dictionary keys
for x in mydict:
    print("Printing each dictionary key: ", x)

# Loop dictionary values
for x in mydict.values():
    print("Printing each dictionary value: ", x)

# Copy a dictionary
mydict2 = mydict.copy()
print("copied mydict under mydict2: ", mydict2)

# Create a dictionary that contain three dictionaries:

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
        },
    "child2": {
        "name" : "Tobias",
        "year" : 2005
        },
    "child3": {
        "name" : "Linus",
        "year" : 2006
        }
    }

print("myfamily dictionary is: ", myfamily)

# Create a dictionary that contain three dictionaries:

child1 = {
    "name" : "Emil",
    "year" : 2004
    }

child2 = {
    "name" : "Tobias",
    "year" : 2005
    }

child3 = {
    "name" : "Linus",
    "year" : 2006
    }

myfamily2 = {
    "child" : child1,
    "child2" : child2,
    "child3" : child3
}
print("myfamily2 dictionary is: ", myfamily2)

#---------IF STATEMENTS----------
print()
def greatherthan(a, b):
    if a > b:
        print(a, " is bigger than ", b)
    else:
        print(b, " is bigger than ", a)

greatherthan(8, 4)

#---------MATCH----------
# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#---------WHILE LOOPS----------

def whileloop (x, y):
    while x > y:
        print(x, "is bigger than",  y)
    else:
        print(y, "is bigger than", x)

whileloop(2, 3)

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print("continue the loop: ", i)

#---------FUNCTIONS----------

# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Bob", "Jacob", "Josh")

# Decorators take a base function as an input

def timer_dec(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        brew_time = end_time - start_time
        print("Brewing time is: ", brew_time)
    return enhanced_fn

@timer_dec
def brew_tea():
    print("Tea is brewing")
    time.sleep(1)
    print("Tea is finished")

brew_tea()

# lambda function
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lamda function that doubles the number you send in
def myfn(n):
    return lambda a: a * n

mydoubler = myfn(2)

print("mydoubler is: ", mydoubler(11))

# higher order function

def upper(text):
    return text.upper()

def lower(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(upper)

# Recursion

# Recursion is when a function calls itself. Every recursive function must have two parts:
# 1. A base case - A condition that stops the recursion
# 2. A recursive case - The function calling itself with a modified argument

def countdown(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        countdown(n - 1)
countdown(5)
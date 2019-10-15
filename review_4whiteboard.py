# collections: containers to store multiple objects or things
# lists, tuples, set

# LIST
# CRUD (create, read, update, delete)
my_list = [2, 4, 3]                 # create
first_item = my_list[0]             # read
my_slice = my_list[1:3]             # read: non inclusive at end 
# if this:  [-1:-3:-1] from -1 to -3, step 1 backwards
# if this: [::-1] reverses the sequence or can just say reversed(my_list)
my_list.append(["hello", "world"])  # update, appends to end the mini embeded list
my_list[3][1]                       # read: grab index 3 and then within it, grab index 1
my_list[1] = 6                      # update: change item within list
my_list.insert(1,8)              # Update: insert object before index, first #
my_list.pop()                       # Update: Popping last item off list
my_list.extend(["Hello", "World"])  # update: extends to end each as individual items
my_list.remove("Hello")             # update: remove first value found
my_list.clear()                     # update: clears the list

del my_list                          # delete: remove the list from memory

# LOOPS
# Ability to iterate over an iterable until a condition is false

# For Loop
# for <something> in <iterable>:

for i in range(10):
    x = 1 + i      # shared scope with the file or where declared
    if i >= 7:
        break   # break will end the loop
    if i > 8:
        continue # will go to the next iteration, never reach next line
    a = i + i
print(x)

# While loop
# While a condition has been met or is true, do this code
# while <condition is true>:

n= 8
while n >= 0:
    print("Not yet")
    n -= 1
print('finally done')

# DICTIONARY
# key value collection, unordered and mutable {}
my_dictionary = {
    "name": "Adam Teacher",
    "age": 25
}

my_dictionary["name"]                   # Read
my_dictionary.get("name")               # Read: get a value
my_dictionary["name"] = "Adam Jayne"    # Update: reassigns value
my_dictionary["hobby"] = "Python"       # Update: add a key value pair if doesn't exist
my_dictionary.update({'hobby': 'Golf', "age":28}) # Update: same reassigning without = sign
# It's an add Update here.  Second is whole new dict. added
my_dictionary.keys()                    # grabs just keys
my_dictionary.values()                  # grabs just values
my_dictionary.items()                   # key value pairs into a tuple-like object

my_dictionary.get()
# FUNCTIONS
# def <func name>(<parameter>):
# arguments are data objects passed into and held by the parameter names

v=""
def change(x):
    v = "velocity"  # doesn't go out of scope unless it has to
    print(v)
    return x + 1
change(12)
print(v)

# CLASSES
# custom data type object, container of methods and attributes
# class <ClassName>(<inherited classes>):

class Animal:

    def __init__(self, kingdom):     # "constructor" that constructs an instance
        self.kingdom = kingdom
    
    def get_kingdom(self):
        return self.kingdom

class Human(Animal):
    
    def __init__(self, kingdom, name, age):
        super().__init__(kingdom)
        self.name = name
        self.age = age
    
    def speak(self):
        return f'Hello, I am a {self.name}'

# create a new human
me = Human("animal","Sir", "25")
print(me.get_kingdom)

# OOP:  Four Pillars(APIE): Abstraction, Polymorphism, Inheritence, Encapsulation
# A - dealing with the idea rather than the procedure
# P - Functions that operate differently based on the data given (program infers from data given)
# I - Bringing data and functionality from a parent class or object
# E - Bundling together data and actions that manipulate the data

# Virtual Environments: Isolated environments used to test and share projects to keep dependencies local
# Create folder: python -m venv <name>
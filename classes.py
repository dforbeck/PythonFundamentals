class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Kid:
    def blah(self):
        print('blah')

    def sleep(self):
        print('blah')

class Student(Person, Kid):
    
    school = '1150 Academy' 
    # class attribute above
    counter = 0

    #method is a function that exists in a class
    def __init__(self, name, grade, age): 
    # instance attributes above
    # initialize a student above, defining own initializer
    # gave name, grade, and age attributes to student
    # dunder init is only required method for a class
    # dunder method are on classes that are **DOUBLE** underlined
        # attribute
        super().__init__(name, age) # borrow from class above and supercedes values
        self.grade = grade
        self.counter = Student.counter
        Student.counter += 1
    
    def have_birthday(self):
        self.age +- 1
    
    def greeting(self):
        return f'Hello, my name is {self.name}.  I am in grade {self.grade}.'
    
    def change_name(self, new_name)  
    # this keeps things safe when want to manipulate, manipulate by methods or a class PLEASE

xzavier = Student("Justin", 8, 32)

print(xzavier)

s1 =Student(0,1,3)
s2 =Student(0,1,3)
s3 =Student(0,1,3)

print(s2.counter)  # will print 1


#OOP (Object oriented programming)
# APIE (4 pillars of OOP)
# Abstraction   - Hidden away lower level operations for user friendliness
#               - dewaling with ideas rather than procedure
# Polymorphism  - functions that operate differently depending on the data given
#               - same function but depends on what given
# Inheritance   - Bringing data functionality from a parent/class/object
#               - Single inheritence - single parent
#               - Multi-level inheritance- layered inheritance
#               - Multiple inheritance - class inherits several other classes 
#               - Hierarchical inhertitance - When more than one derived classes
#                are created from a single base
# Encapsulation - data and functions that are bundled together

name = "you"

def modd_name(to_change);
    to_change = "They"
    return to_change

name = modd_name(name)
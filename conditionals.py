# A conditional resolves to a boolean statement (True or False)

left = True
right = False

left == True  # this says "Is left equal to True?"

right != True # not equal to

left is right # answer is False

left is not right # answer is True

left != right # left and right are not equivalent
left == right # left and right are equivalent
left is right # left and right are the same identity
left is not right # left and right are not the same identity

#Example
age_1 = 23
age_2 = 45

# Comparison operators
age_1 > age_2
age_1 < age_2
age_1 >= age_2
age_1 <= age_2

# Logical operators
age_1 == 4 and age_2 < 22 # the and operator, both need to be true
age_1 == 4 or age_2 < 22 # or operator, only one needs to be true
not age_1 == 23 # swaps the True/False 


x = 4
name = "Ryan"

if x > 3 and name == 'Ryan':
    if True:
        print("I'm inside an if statment")
    print("X is big, and the person's name is Ryan")
elif x <= 3:
    print('Maybe x is big, IDK')
else:
    print("Otherwise, no")


# Challenge
# Take a name and age, and if the person is under 18, say "NAME, you are
# not an adult",
# if the person is 18, but not 21,say "NAME, you are an adult, but not quite yet
# if the person is 21 and older, say "You are fully an adult"
# 
# extra spicy
# If their name starts with an A, say "Cool name"

name = input("What is your name? > ")
age = int(input("What is your age? >"))# must convert age to a number now

if age < 18 and age > 0:  
# can use 'in range' to get a range of ages
# if age in range(18):  
    print(f'{name}, you are not an adult.')
elif age >= 18 and age < 21:
    print(f'{name}, you are not an adult, but not quite yet.')
elif age >=21:
    print(f'{name}, you are fully an adult.')

x = "A" in name
# Can use name[0]
if x:
# if name[0] == "a" or name[0] == "A":
# or even better>>>>
# if name[0].lower() == "a": # switches whole thing to lower case and only need to check that.
    print('A\'s rule')
else:
    print('Your name doesn\'t start with an A. That\'s Ok.  You are the best!')


you= 'person'
better_you = you.replace('p', 'P')
print(better_you)

# Challenge
# Declare a number
# If the number is divisible by 3, print Fizz
# If the number is divisible by 5, print Buzz
# If the number is divisible by both 3 and 5, print FizzBuzz
# Otherwise, just print the number

test_number = int(input("Please enter a number: >"))

if test_number % 3 == 0 and test_number % 5 ==0: # you are checking if true, so need double =
# could do % 15 , lowest common multiple instead.
#if test_number % 15 == 0:
    print('FizzBuzz')
elif test_number % 3 == 0:
    print('Fizz')
elif test_number % 5 == 0:
    print('Buzz')
else:
    print(test_number)


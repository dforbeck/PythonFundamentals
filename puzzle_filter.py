to_filter =[
    {   "name": "Anton",
        "age": 0
    },
    {   "name": "Someone",
        "age": 67
    },
    {   "name": "Sara",
        "age": 43
    }
]

def filter_by_age(value):
    return value["age"]>50

greater_than_50 = list(filter(filter_by_age, to_filter))
# Typecast it as a list, so doesn't return a Python definition
print(greater_than_50)

def im_gonna_be_callback(x):
    print(x)

def i_take_callback(cb):
    cb("Hello World")

i_take_callback(im_gonna_be_callback)

############# SESSION 2

numbers =[1,2,3,4,5]
def add_15(val):
     return val +15

# adding = lambda x: x+15
# z = adding(15)
# print(z)

#my_numbers = list(map(add_15, numbers))

#lambdas are good when only using once
my_numbers = list(map(lambda x: x + 15, numbers))

print(my_numbers)

#####





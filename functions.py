def FUNCTION_NAME(parameters):
    print(parameters)
    #whatever code block you want to repeat
    return "some data"

FUNCTION_NAME('parameter data')
print(FUNCTION_NAME("Python is cool")) # some data is returned, so printed last as return value
something = FUNCTION_NAME("I'm data")
print(something)

# Multiple parameters

def cash_register(total, tendered):
    """" this takes two numbers and compares things"""
    answer = ""
    if tendered < total:
        answer= "Hey I need more money"
    elif tendered == total:
        answer= "Have a nice day"
    else:
        answer= "I owe you some money"
    return answer

final_answer = cash_register(67, 30)
print(final_answer)

# help(cash_register)

# Default return statement

def combine(x,y,z):
    """ 
    Takes three numbers and prints the sum
    """
    print(x+y+z)

what_is_this = combine(1,2,3)
print(what_is_this)


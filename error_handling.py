# # Try Except

# def proclaim_user_birthday(name, age):
#     try:
#         new_age = age +1
#         message = f'{name} is now {new_age} years old!'
#         print(message)
#     except Exception as e:  # take exception and put in e
#         print(e)
#     print('Only when my program continues')

# proclaim_user_birthday("Me","45")
# print("I'm after proclaim")

# import pytest for later tests below.
import pytest

def find_user(user_id):  # the parameter is here
    if not isinstance(user_id, int): # check if user id is of type int
        try:
            user_id = int(user_id)
        except Exception as e:
            raise TypeError("User ID must be a number") 
            # here can specify when user made type error, ABC Id, instead of number
    return "A user"

# test for both above cases, have a user, or have the typerror
# left is what get, right is what want
def test_find_user_returns_string():
    assert find_user(2) == "A user"

def test_find_user_takes_string_returns_string():
    assert find_user("2") == "A user"

def test_find_user_typeerror_exception():
    with pytest.raises(TypeError):
        find_user("string")

# handling looking up the user here
# find_user(12)  # an argument is what you use to give a function
# find_user("12")
# find_user("a")
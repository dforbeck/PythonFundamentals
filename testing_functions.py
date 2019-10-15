# bring in pytest in a virtual environment (via pip)
# Define test with test_<whatever>.  "test_" must be the beginning.
# when you assert, you are specifying expected answer of function
# left is get, right is what want
# left is what get, right is what want

def find_largest(x,y):
 #   or return max(x,y)
    if x>y:
        return x
    else:
        return y

def test_find_largest():
    #largest between 1 and 2 should result to 2
    assert find_largest(1,2) == 2  

def test_something():
    assert "test" == "test"
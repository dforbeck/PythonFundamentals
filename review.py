# variables

# list, tuple, set, dict
def multiple_returns(a,b):
    data=0
    if a>b:
        data = b,a
    return True, data
    
print(multiple_returns(2,1))

something = {}
# something.update({"random:56"})
#OR
something["random"] = 56

# functions
def func(x, t):
    return f'{x}'

captured = func(3, 5) # assigning the call to a variable catches return

# Conditionals

# Looping

# for takes an iterable and goes for length of iterable of the loop
items = [1,2,3,4,5]
for item in items:
    k = item + 12 
print(k)   # doesn't need to be in same scope in a loop

z = True
flag =0

while z:
    flag += 1
    scoped = "Do I exist"
    if flag >34:
        z = False

print(scoped)

if scoped:
    potato = 'spuds'
else:
    potato = ""
print(potato)



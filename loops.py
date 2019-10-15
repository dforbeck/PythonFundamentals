# FOR LOOP

animals = ["Jaguar", "Racoon", "Fox", "Cat", "Toucan"]

for animal in animals:
    print(animal)

for i in range(1101):
    if i % 3 == 0 and i % 5 ==0: 
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


for i in range(30):
    for j in range(30):  # this executes 30 times each i time.  Nested for loop
        if i == j:
            pass
            # print("They match", i)


expenses = [
    ('McDonald\'s', 12.00),
    ('Steam', 49.99),
    ('Rent', 900.00)
]


total = 0.00  # must be float like others

for expense in expenses:
    total += expense[1]
    print(total)

print(total)


# WHILE

while (False): # while this execute this code
    #Code block
    print("I'm in a while loop")


x = 0
while x <100:  # the 100 sets the limit
    print(x)
    x += 4

x = 101
while x <100:  
    print(x)
    x += 4
else:
    print('While loop never ran')


products =['nvidia', 'amd', 'arm', 'intel', 'risc']
search_term = 'risc'
#Create a while loop that searches for the search term
x = 0  # starting point
while search_term != products[x] and x< len(products):
    print(x)
    print(products[x])
    x += 1 
    # do incrementation whould be at end of while loop
    # avoids unnecessary steps

# The If equivalent
if search_term in products:
    print(products.index(search_term))
else:
    print("Not found")



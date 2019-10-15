puzzle = open('frequencies.txt', 'r').read().split("\n") 
# read file and turn into a string
# split it into new line by hard return, but still tiny strings
numbers =[int(i) for i in puzzle]
# create a list of integers from a for loop

# longer method is below
# numbers =[]
# for i in puzzle:
#     numbers.append(int(i))

# What is the final frequency
# For loop
# While loop
# Python built-in function

# For
final_step = 0
for each_step in numbers:
    final_step += each_step
print(final_step)

# While
x=0
total = 0
while x < len(numbers):  
    total += numbers[x]
    x += 1 # increment after each item in loop
print(total)

# Python
built_in_total = sum(numbers)
print(built_in_total)

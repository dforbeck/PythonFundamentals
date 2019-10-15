#LISTS
# iteme separated by commas
# list items can be of any type
# mutable- can change things inside of list

names = ['Adam', 'Jane', 'John']
students = [
   'The Rock',
   'Charles',
   'The Undertaker',
   'The Big Show',
   6,
   4+1j,
   [
       'nested lists',
       'are cool',
        [
            56
        ]
   ] 
]

names[0] = "Potato" # lists are mutable
print(names[0])

names.append('Thanos') # item added to end
print(names[-1])

#print "are cool"
print(students[-1][-1])  # second -1 is the last item within mini list
print(students[-1][-1][0])  # is the last item within 2nd mini list

names.insert(1, "Debbie")  # Before index 1
print(names)

students.extend(names)  #combines lists into one list under students (first one)

names.pop() # remove and returns last item, if put something inside, then remove and return that index number
print(len(students))  # print the length of 
print(len('Python Course'))

students.remove("The Big Show") # it looks for it and removes it, only first occurrence though.
print(students)

# SLICING
# If only want a few items from list and pull into a new list
# You can slice a list or a string, same thing

new_list= students[0:3:1] 
# start on first index: stop at this index (not including this position): step by 1
# Took the first three items

#reverse_List= students[::-1]   #short hand
reversed_list= students[0:0:-1] 
# from 0 to 0 by -1 which is at end short hand
# reverse_List= students[::-1]   #short hand
# OR students.reverse()

print(reversed_list)
# the backward \n gives you a hard return after your print item ?
print(students)

reversed_again = list(reversed(students))  # must turn what reversed into a list saying, reverse and then turn into a list
print(reversed_again)

x =[1,2,3]
y =["yes", "not"]
print(x+ y) # can concatenate lists, but does not change x, no persistence, does not modify things in memory

# TUPLES
# Similar to list but can't change it, they are immutable
# they can be anything

my_tuple = (12, 32)
print(my_tuple[0])

my_name = ("Jane", "Jones")
f_name, l_name = my_name # called unpacking

tuple_names = ("Matthew", "Mark", "Patrick", "Megan", "Tom")
something = tuple_names[3:5] # is sliceable
print(something) 

tester = ("John",) # comma says I am a tuple ... hmmm.
print(tester)

# SET
# also similar to list, but it uses curly brackets
# has unique items only, no duplicates, if try, it will ignore it.
# It is an unordered unique value, but still mutable
# So, can't slice
# Don't need comma to define a single item test

states = {'Indiana', 'Alaska', 'Texas'}
states.add('90') # but not adding to a certain spot
print(states, end ='') # end Puts the next thing on the same line
states.remove("Alaska") # if not a member, remove brings error
states.discard("ALaska") # without error if not there

print(states)
#states.clear() # clears set of all values

print("Indiana" in states)  # returns a Bookean, you are finding it.

sentence = "Mary had a little lamb"
list_of_words = sentence.split() # separates by splitting based on empty space. You can put anything in ()
print(list_of_words)

another_one= "Mary had a little lamb"
print(list(another_one)) # makes a list of every character, including spaces


my_names= ["Wallaby", "Bakerfield", "colGATE", "cOcaCOla" ]
# remove Colgate
# add Crest
# change CocaCola to lowercase
# grab every other item in the list
# Print each name individually

my_names.remove("colGATE")
my_names.append("Crest")
my_names[2] = my_names[2].lower() # changing it to lower case, reassigning the value
print(my_names)

piece = my_names[0:-1:2] # Goes from beginning to end, every other one or 1:4:2
print(piece)
print(my_names[0])
print(my_names[1])
print(my_names[2])

print("\n".join(my_names))






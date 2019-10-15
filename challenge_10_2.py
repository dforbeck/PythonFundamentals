# # Fill out the truth table
# a       b       not (a and b or b)
# ----------------------------------
# False   False     true    
# True    False     true    
# False   True      false
# True    True      false

# ========================================
# # Each student that has an A in their name, print their age.
# # Make your program able to handle any list of students (this format below)

students = [("AJ", 25), ("XD", 19), ("JA", 27), ("IS", 27)]
letter = "A"

for student in students:
    if letter in student[0]:
        print(student[1])


#unpacking example
for a, b in students:
    if "a" in a.lower():
        print(a, b) # included names here

# could even do this.


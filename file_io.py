# #create new file
# new_file = open('./file_io_hub/testing.txt','x')

# #write text into files
# new_file.write("Hello World")

# new_file.close()

#with closes the file at the end.  Can create a new file like this.
with open('with_statement.py', 'w') as f:
    f.write("#I am a comment\nprint('Hello World')")

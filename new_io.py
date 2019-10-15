 #challenge
#create a file that creates a file that changes the message

other_file = open('./file_io_hub/change_text.py','x')
valid_code = """
to_change = open("./testing.txt", "w")

to_change.write("I'm sorry I cannot do that.")

to_change.close()

"""
other_file.write(valid_code)
other_file.close()

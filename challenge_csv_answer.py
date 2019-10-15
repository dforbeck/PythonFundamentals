#create variables to open the file, r for read string, read it and
# split because each one is a line and separated by a hard return
employees = open('employees.csv', 'r').read().split('\n')
access_list = open('access_list.csv', 'r').read().split('\n')

# Find out types
print(type(access_list))

# remove the first line since using indeces, not headers
employees.pop(0)
employees.pop()
access_list.pop(0)
access_list.pop()

# Format into usable information, with truncated file, only pos. #4
modified_employees = []
for row in employees:
    info = row.split(',')
    modified_employees.append(info[4])
    print(modified_employees)

# Format into usable information, with truncated file, only pos. #0
modified_access_list = []
for row in access_list:
    info = row.split(',')
    modified_access_list.append(info[0])
   
#Check access against employee
unauthorized = []
for ip in modified_access_list:
    if ip not in modified_employees:
        unauthorized.append(ip)

print(len(unauthorized))










############################
# COULD USE BELOW INSTEAD TO CREATE DICTIONARY
# turn it into a dictionary using the headers
def convert_to_list_of_dictionaries(the_list):
    # remove and grab the headers from file and create a list from it
    keys = the_list.pop(0).split(',')
    to_return =[] # empty list
    # turn rows into dictionaries
    for row in the_list:
        entry = {}
        values = row.split(",") # pieces made here
        # load up the dictionary next
        # enumerate returns an iterable of tuples
        for i, key in enumerate(keys):  
            entry[key] = values[i]
        to_return.append(entry) # append each row/entry
    return to_return
        

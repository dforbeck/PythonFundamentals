# To create a virtual environment: <python> -m venv <a-name-here>
#To activate virtual environment:
#   Windows: <name>/Scripts/activate
#   Mac(Linux): source <a-name>/bin/activate
# To verify: Terminal should have the virtual environment on the left
#
import requests
from pprint import pprint

# capture it in a variable
#response = requests.get('https://api.spacexdata.com/v3/rockets')
#print the status of request
#print(response)

#obtain data
#data = response.json()
#print(type(data))

#print list keys
#for entry in data:
#    print(entry.keys(),"\n")  #"\n" is new line

# # print rocket names from API
# for entry in data:
#     print(entry['rocket_name'], "\n")


###################
#Challenge: Find a character in Morty API

# API base URL
api_URL= 'https://rickandmortyapi.com/api/'

# capture it in a variable
char_getrequest = requests.get(api_URL + "character")

# Can check if response is 200 
#if char_getrequest.ok()
#OR
#print the status of request
print(char_getrequest)

# try/except block to find out if have what need
try:
    data = char_getrequest.json()
except Exception:
    data = None
print(data)

#What type of data type
print(type(data))

# print top level keys
print(data.keys())

#print contents of info key
print(data['info'])

#print type of contents of results key
print(type(data['results']))

#print the length of results list, sometimes limited
print(len(data['results'][-1]))

#print the last result in list
print(data['results'][-1])

#print how many items in database
print(data['info']['count'])

# set variable to capture the number of current character choices
choices = data['info']['count']

#Ask for the user choice
choice = input(f'Pick a number between 1 and {choices} >')

# set variable to capture the choice
chosen = requests.get(api_URL + 'character/' + choice)

# capture data of chosen one
chosen_one = chosen.json()

# print the name of the chosen, by this point
# print chosen object
print(chosen.headers)

# should have the 'name' key picked up
print(chosen_one['name'])




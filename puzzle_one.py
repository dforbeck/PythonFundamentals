# Morning Warmup

# Bronze 
# Create two variables containing floats and print the result of floor division

variable_one = 2.6
variable_two = 2.7

variable_three = 2.6 // 2.7
print(variable_three)

# Silver and Gold
# Catering service
# prompt user for an event type, and the number of guests
# if the event is a banquet, the min number of attendees is 30
# if the event is a wedding, the min number of attendees is 25
# Catering business will not work for anything else at this time
# When below min, display message that expresses there are too few attendees.

event_type = input("What is your event type? Banquet(1) or Wedding(2) Type 1 or 2 ?  > ")
#could have used an input("""").lower() if got the text and wanted all lower case.
number_of_guests = int(input("How many guests will come to your event?  >"))

if (event_type == "1" and number_of_guests < 30) or (event_type == "2" and number_of_guests < 25):
    print("Sorry, your party is too small at this time.  We cannot accept your reservation.")
else:
    print("Thank you for your reservation")
    



from puzzle_two_data import contracted_items
from puzzle_two_data import purchased_items

def calculate_savings(prev_price, current_price, amount, tax):
    """
    Function's purpose is to calculate and report savings on a purchase

    prev_price          (float number describing the price befores savings)
    current_price       (float number describing the price at purchasing)
    amount              (int number denoting how many were purchased)
    tax                 (float number describing the state's tax percentage)

    This function should return a float number describing how much was saved
    or a string stating "no savings occurred"
    """
    tax_percentage = 1 + tax
    previous_total = (prev_price * amount) * tax_percentage
    current_total = (current_price * amount) * tax_percentage
    savings = previous_total - current_total

    if savings > 0:
        return savings 
        # if want to get savings out and exit the function
        # return exits the function
    else:
        return ("Sorry. No savings occurred.")

# OR 
# return savings if savings >0 else "Sorry. No savings occurred."

# print(calculate_savings(12.0, 10.0, 2.0, .05))  # test prices
# print(calculate_savings(11.0, 20.0, 2.0, .05))  # test prices

tax = float((input("What is the tax rate? Example .075 for 7.5% >"))

## need for loop
if contracted_items["id"] == purchased_items["id"]:   
    calculate_savings(contracted_items['price'], purchased_items['price'], purchased_items['count'], tax)
else:
    print("No luck")
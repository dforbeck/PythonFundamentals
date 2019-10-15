"""
Calc: the ability to add, subtract, multiply 
and divide and will be a command line app
"""
from calc import calculate

calculate()
while True:
    print(
        """
        Calc Menu
        1.Run operation
        2.Quit
        """)
    choice = input('>')
    if choice == '1':
        calculate()
    elif choice == '2':
        exit()  # built in python



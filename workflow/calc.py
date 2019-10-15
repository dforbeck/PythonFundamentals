def calculate() :
    x = float(input("#: "))
    y = float(input("#: "))
    op = input("op:")

    result = 0
    if op == "+":
        result =  x + y
    elif op == "-":
        result = x-y
    elif op == "*":
        result = x*y
    elif op == "/":
        result = x/y
    else:
        print("Invalid Op")

    print(result)
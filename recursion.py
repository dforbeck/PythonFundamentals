# my_items =[1, 2, 3, 6, 89]

# def recursive_sum(numbers):
#     if len(numbers) == 1:
#         return numbers[0]
#     else:
#         return numbers[0] + recursive_sum(numbers[1:])

# print(recursive_sum(my_items))
# print(sum(my_items))

# Fibonacci numbers
# starts with 0 and 1, subsequent number is sum of previous 2
# 0,1,
def fib(numbers, current=1, previous=0, count=0): 
# numbers is however long we want to go, like first 100
    if count < numbers:
        return fib(numbers, current+previous, current, count+1)
    else:
        return current

print(fib(4))

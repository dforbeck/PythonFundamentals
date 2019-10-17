#visualgo.net has good visualization
# if left is > right, swap
def bubble_sort(numbers):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(numbers)-1): # gets indeces
            if numbers[i] > numbers[i+1]: # if left > right
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i] # swapping
                swapped = True # true, swapped, so do it all over again
    # time complexity is O(n^2)

my_list = [5,2,90,6,32]

bubble_sort(my_list)

print(my_list)
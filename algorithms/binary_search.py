def binary_search(numbers, item, first=0, last=None):
    #assume sorted list, have to use recursive algorithm
    # find midpoint of list by (first+last)//2
    # check if midpoint is equal, but if mid > search, go left [:mid]
    # if mid < search, go right, then go back to beginning. [mid+1:]
    # slice is beginning to midpoint 
    if not last:
        last = len(numbers) -1 
    if item == numbers[first]:
        return first
    elif item == numbers[last]:
        return last
    
    midpoint = (first + last)//2

    if item == numbers[midpoint]:
        return midpoint
    elif item > numbers[midpoint]:  # if item looking for is greater than mid
        return binary_search(numbers,item, midpoint+1, last) # start again with new slice of data
    elif item < numbers[midpoint]:
       return binary_search(numbers, item, first +1, midpoint-1)

my_list=[1,2,3,4,5,6,7]
print(binary_search(my_list,5))


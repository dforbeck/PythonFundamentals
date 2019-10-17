def selection_sort(numbers):
# finds lowest element and puts it at beginning (it's now sorted), then then next smallest, and the smallest is now that one and puts it next to the last one.  They are now sorted.  Now goes on to find next lowest.
# Tag you're it thing.
    for i in range(len(numbers)): # length is noninclusive, so 4 times, including 0

        lowest_value_index = i

        for j in range(i+1, len(numbers)):
            if numbers[j]< numbers[lowest_value_index]:
                lowest_value_index = j # mark if lowest number
        
        numbers[i], numbers[lowest_value_index]= numbers[lowest_value_index], numbers[i]  # swap


my_list = [5,2,90,6,32]

selection_sort(my_list)

print(my_list)
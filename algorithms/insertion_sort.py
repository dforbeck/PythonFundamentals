def insertion_sort(numbers):
# sorts as go up the list, putting things in their place.  
# Literally yanking an item out to check where should go.

    for i in range(1, len(numbers)):
        item_to_insert = numbers.pop(i)  # take it out and hold

        j = i -1

        while j >= 0 and numbers[j] > item_to_insert:
            j -= 1

        numbers.insert(j +1, item_to_insert)  # pop into the right side

my_list = [5,2,90,6,32, 1]

insertion_sort(my_list)

print(my_list)
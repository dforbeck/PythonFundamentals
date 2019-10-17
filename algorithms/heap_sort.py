def heapify(numbers, heap_size, root_index):
    largest = root_index
    lef_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if lef_child < heap_size and numbers[lef_child] > numbers[largest]:
        largest = lef_child
    
    if right_child < heap_size and numbers[right_child] > numbers[largest]:
        largest = right_child

    if largest != root_index:
        numbers[root_index], numbers[largest] = numbers[largest], numbers[root_index]
        heapify(numbers, heap_size, largest)

def heap_sort(numbers):
    n = len(numbers)

    for i in range(n, -1, -1):
        heapify(numbers, n, i)
    
    for i in range(n-1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)


my_list = [5,2,90,6,32, 1]

heap_sort(my_list)

print(my_list)



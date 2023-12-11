def find_smallest(arr):
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(find_smallest([1, 232, 23, 45, 21, 34, 53, 655, 235, 347, 123, 98]))

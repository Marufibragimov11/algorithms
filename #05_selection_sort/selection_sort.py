"""
                                    Selection Sort
is a simple sorting algorithm that works by repeatedly selecting the smallest
(or largest, depending on the order) element from the unsorted portion of the list and
swapping it with the element at the beginning of the unsorted portion.
This process continues until the entire list is sorted.
"""


# First example of selection sort algorithm
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


print(selection_sort([1, 232, 23, 45, 21, 34, 53, 655, 235, 347, 123, 98]))


# Second example of selection sort algorithm
def find_smallest(arr):
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # Finds the smallest element in the array and adds it to the new array
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([1, 232, 23, 45, 21, 34, 53, 655, 235, 347, 123, 98]))

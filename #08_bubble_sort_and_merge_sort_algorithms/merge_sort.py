from colorama import Fore, Back, Style


def merge_sort(array):
    if len(array) > 1:

        # Finding the middle of the array
        mid = len(array) // 2

        # Dividing the array elements
        left = array[:mid]
        print(Back.GREEN + str(left))

        # into 2 halves
        right = array[mid:]
        print(Back.RED + str(right))

        # Calling function to sort elements for left side using recursion
        merge_sort(left)

        # Calling function to sort elements for left side using recursion
        merge_sort(right)

        i = j = k = 0

        # Copy the data to temporary array left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        print(Back.CYAN + str(left))
        print(Back.BLUE + str(right))


arr = [34, 25, 20, 5, 44, 12, 9]
merge_sort(arr)


def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

"""
Linear Search
Start at the beginning: The algorithm starts at the beginning of the list.
Check each element: It compares each element in the list with the target element.
Found or not: If the current element matches the target element, the search ends,
and the position/index of the element is returned. If the end of the list is reached without finding the element,
the search concludes, indicating that the element is not present.
"""


def linear_search(n):
    my_list = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]
    for i in range(len(my_list)):
        if my_list[i] == n:
            return i
    return None


print(linear_search(56))

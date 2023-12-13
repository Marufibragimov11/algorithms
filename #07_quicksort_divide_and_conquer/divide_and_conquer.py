# Function to find sum of array using while loop
def summ(array):
    total = 0
    for i in array:
        total += i
    return total


print(summ([5, 8, 12, 22]))


# Function to find sum of array using recursion
def sum_recursion(array):
    if len(array) <= 1:
        return array[0]
    else:
        return array[0] + sum_recursion(array[1:])


print(sum_recursion([5, 8, 12, 22]))

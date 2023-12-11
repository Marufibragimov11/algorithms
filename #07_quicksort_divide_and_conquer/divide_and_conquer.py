def summa(array):
    if len(array) == 1:
        return array
    elif len(array) == 0:
        return None
    else:
        integer = array[0] + summa(array)
        return integer


print(summa([5, 8, 12, 22]))
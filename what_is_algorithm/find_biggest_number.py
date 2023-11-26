def find_biggest_number(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


print(find_biggest_number(4, 5, 3))

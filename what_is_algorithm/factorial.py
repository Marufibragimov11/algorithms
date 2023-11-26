def factorial(N):
    i = 1
    fact = 1
    while i != N + 1:
        fact *= i
        i += 1
    return fact


print(factorial(5))

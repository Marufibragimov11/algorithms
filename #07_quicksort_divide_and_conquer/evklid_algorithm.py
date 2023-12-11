def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Example usage:

result = gcd(45, 27)
print(f"The GCD of {45} and {27} is: {result}")

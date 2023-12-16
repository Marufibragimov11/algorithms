import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "!@#$&"

all = lower + upper + numbers + symbols
print(all)


def generate_password(length):
    password = "".join(random.sample(all, length))
    return password


print("Your new generated password is: ", generate_password(8))

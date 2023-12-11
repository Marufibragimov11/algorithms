"""
                                    Stack
LIFO data type
LIFO (Last In First Out)
Added to the top of the list and will get from the top
"""


def greet(name):
    print(f"Hello, {name}!")
    greet2(name)
    print("Getting ready to say bye...")
    bye()


def greet2(name):
    print(f"How are you, {name}?")


def bye():
    print("Ok bye!")


greet("Steve")
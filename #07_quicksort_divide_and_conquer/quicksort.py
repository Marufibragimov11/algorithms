from random import randrange


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        less = [i for i in array if i <= pivot]
        greater = [i for i in array if i > pivot]
        print(f"{less} + [{pivot}] + {greater}")
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    array_1 = [1, 5, 12, 0, -5, 66]
    print(array_1)
    print(quicksort(array_1))

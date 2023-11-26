import time


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12

start_time = time.time()
result = binary_search(arr, target)
end_time = time.time()

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

runtime = end_time - start_time
print(f"Runtime: {runtime} seconds")

def binary_search(elements, item):
    low = 0
    high = len(elements) - 1

    while low <= high:
        mid = (low + high)
        guess = elements[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


elements = list(range(1, 101))

print(binary_search(elements, 50))

# EXERCISES

# 1.1 Suppose you have a sorted list of 128 names, and you’re searching through it using binary search.
# What’s the maximum number of steps it would take?

# log128 = 7, because 2^7 = 128

# 1.2 Suppose you double the size of the list.
# What’s the maximum number of steps now?

# log256 = 8, because 2^8 = 256




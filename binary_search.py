def binary_search(elements, item):
    low = 0
    high = len(elements) - 1

    while low <= high:
        mid = int((low + high) / 2)
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

# ANSWER: log128 = 7, because 2^7 = 128

# 1.2 Suppose you double the size of the list.
# What’s the maximum number of steps now?

# ANSWER: log256 = 8, because 2^8 = 256

# Give the run time for each of these scenarios in terms of Big O.
# 1.3 You have a name, and you want to find the person’s phone number in the phone book.
# ANSWER: O(log n)

# 1.4 You have a phone number, and you want to find the person’s name in the phone book.
# (Hint: You’ll have to search through the whole book!)
# ANSWER: O(n)

# 1.5 You want to read the numbers of every person in the phone book.
# ANSWER: O(n)

# 1.6 You want to read the numbers of just the As.
# (This is a tricky one! It involves concepts that are covered more in chapter 4.
# Read the answer—you may be surprised!)
# ANSWER: Don't know this yet.


# Theory time

# If a list has 1000 elements it would take 1000 guesses to find an element in worst case.
# So whenever we have number of maximum guesses and the size of array equal we call that LINEAR TIME. O(n)

# Binary search is different because it runs in LOGARITHMIC TIME, which means for an array that has 100
# elements maximum number of guesses in the worst case is 7. O(log n)

# Big O is the special notation that tells us how fast an algorithm is.

# O(n) - n stands for number of operations.


arr = [1, 2, 3, 4, 5, 6, 7, 8]


def binary_search_recursive(data, target, low, high):
    if low > high:
        return None
    else:
        mid = int((low + high) / 2)
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            # go to the left side of an array
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            # go to the right side of an array
            return binary_search_recursive(data, target, mid + 1, high)


print(binary_search_recursive(arr, 6, 0, len(arr)))





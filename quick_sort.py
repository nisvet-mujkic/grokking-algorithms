# Theory
# Big O for this sorting algorithm is O(n * log n)

# divide and conquer technique, p.s. its a recursive technique :O

# EXERCISES
# 4.1 Write out the code for the earlier sum function.

array = [1, 7, 2]


def sum_array(array, array_size):
    if array_size == 1:
        return array[0]
    else:
        return array[array_size - 1] + sum_array(array, array_size - 1)


# 4.2 Write a recursive function to count the number of items in a list.


def count_items(array, count=0):
    return 0


# 4.3 Find the maximum number in a list.


def max_number(array, array_size):
    if array_size == 1:
        return array[0]
    else:
        return max(array[array_size - 1], max_number(array, array_size - 1))


# print(max_number(array, len(array)))
# print(sum_array(array, len(array)))

# 4.4 Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too.
# Can you come up with the base case and recursive case for binary search?

# QUICK SORT #


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [num for num in array if num < pivot]

        greater = [num for num in array if num > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([5, 1, 2, 8, 11, 22]))




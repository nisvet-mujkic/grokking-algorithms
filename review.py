arr = [1, 2, 3, 4, 5, -4, -2, 6, 7, 8, 9, 10]


def bs_recursive(array, target, low, high):
    if high >= low:
        mid = int(low + (high - low) / 2)
        print(mid)
        if target == array[mid]:
            return mid

        elif target < array[mid]:
            return bs_recursive(array, target, low, mid - 1)

        else:
            return bs_recursive(array, target, mid + 1, high)
    else:
        return None


# print(bs_recursive(arr, 388, 0, len(arr) - 1))


def find_smallest(array):
    smallest_index = 0
    smallest_element = array[0]

    for i in range(1, len(array)):
        if array[i] < smallest_element:
            smallest_index = i
            smallest_element = array[i]

    return smallest_index


print(find_smallest(arr))


def selection_sort(array):
    sorted_array = []

    for i in range(len(array)):
        smallest = find_smallest(array)
        sorted_array.append(array.pop(smallest))

    return sorted_array


print(selection_sort(arr))

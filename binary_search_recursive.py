
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

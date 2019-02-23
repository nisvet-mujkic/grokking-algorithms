
arr = [1, 2, 3, 4, 5, 6, 7, 8]


def binary_search_recursive(data, target, low, high):
    if high >= low:
        mid = int(low + (high - low) / 2)

        if target == data[mid]:
            return mid

        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)

        else:
            return binary_search_recursive(data, target, mid + 1, high)
    else:
        return None

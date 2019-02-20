# THEORY
# recursion - function calls itself
# If you don't have a base case (where the function will end) you will end with an infinite loop


def print_recursive(num):
    print(num)
    if num == 0:
        return
    else:
        print_recursive(num - 1)


# print_recursive(10)

# Without IF statement this function will continue to run "forever".
# Key to remember:
# Every recursive function has two parts:
# 1) base case - tell when the function should stop
# 2) recursive case - when the function should call itself
# Stack is very important concept when it comes to recursion
# Stack is a data structure with a two functions PUSH (add item on top of the stack) and pop (remove it from top)


def greet(name):
    print(f"Hi {name}")
    greet2(name)
    print("END")
    bye()


def greet2(name):
    print(f"How are you {name}?")


def bye():
    print("BYE")


# greet("Nisvet")


# Each time you call a function from another function the calling function is paused
# in partially completed state
# classic one, function for calculating factorial of some number


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))

# Linear recursion = each recursion call is made only once

arr = [1, 2, 3, 21, 334, 5, 6, 7, 8, -2]


def sum_recursion(array, array_length):
    if array_length == 0:
        return 0
    else:
        return array[array_length - 1] + sum_recursion(array, array_length - 1)


# print(sum_recursion(arr, len(arr)))


def reverse_array(array, start, stop):
    if start < stop - 1:
        array[start], array[stop - 1] = array[stop - 1], array[start]
        reverse_array(array, start + 1, stop - 1)


# print(arr)

# reverse_array(arr, 0, len(arr))

# print(arr)

# Write a short recursive Python function that finds the
# minimum and maximum values in a sequence without using any loops.


def find_min_max_recursive(array, length, min_value, max_value):
    if length == 0:
        return min_value, max_value
    else:
        if array[length - 1] < min_value:
            min_value = array[length - 1]
        elif array[length - 1] > max_value:
            max_value = array[length - 1]
        return find_min_max_recursive(array, length - 1, min_value, max_value)


print(find_min_max_recursive(arr, len(arr), arr[0], arr[len(arr) - 1]))

# Write a short recursive Python function that takes a character string s and outputs its reverse.
# For example, the reverse of pots&pans would be snap&stop.

s = "pots&pans"


def reverse_string(s, length):
    if length == 1:
        return s[length - 1]
    else:
        return s[length - 1] + reverse_string(s, length - 1)


print(reverse_string(s, len(s)))

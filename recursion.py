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
    print("Hehe")
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


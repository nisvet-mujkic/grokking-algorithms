# Theory time
# one of the simplest data structures
# most often it has only push and pop methods, but there are also top(), is_empty() and len() function

# Design pattern ALERT here: Adapter pattern
# applies to any context where we want to modify an existing class so that its methods match those
# of a related, but different class or interface.
# npr stack mozemo implementirati uz pomoc Liste, tako sto cemo npr za top() koristiti pyton way -> list[-1]
# ili za is_empty() -> len(list) == 0


# Implementation of Stack (by using Python list beneath)

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class StackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            return Empty('Stack is empty')
        return self._data[-1]

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            return Empty('Stack is empty')
        return self._data.pop()


S = StackArray()
S.push(5)
S.push(3)
S.push(2)

while not S.is_empty():
    print(S.pop())


def is_matched(expression):
    left_delimiters = '({['
    right_delimiters = ')}]'
    stack = StackArray()
    for char in expression:
        if char in left_delimiters:
            stack.push(char)
        elif char in right_delimiters:
            if stack.is_empty():
                return False
            if right_delimiters.index(char) != left_delimiters.index(stack.pop()):
                return False
    return stack.is_empty()


print(is_matched('()(()){([()])}{{}}'))
print(is_matched('[(5+x)-(y+z)]'))








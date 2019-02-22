# Theory
# FIFO, first in first out, only the element that has been in queue the longest is executed next
# all sorts of waiting lists, responses

# has two core functions
# .enqueue(e) add element to the element of the list
# .dequeue() removes and returns first element

# additional ones are: first(), is_emtpy(), len()

# Implementation


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def enqueue(self, element):
        # if self._size == len(self._data):
        # self._size()
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        return answer

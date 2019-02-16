# Theory
# the Big O notation for this algorithm is O(n^2)
# O(n) means that you touch every element of the list once.
# For example if oyu want to sort your playlist from most played to least played
# you have to go multiple times through list, because you first find the most played then the second played
# and so on. So basically you end up with O(n * n) => O(n^2)
# P.S. constants in Big O notations are ignored so even if you check one less element each time
# you go through the list you still end up with O(n * n)

# ALGORITHM IMPLEMENTATION #


def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):  # skipping 0 index because we assumed that is the smallest index
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    sorted_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        sorted_array.append(array.pop(smallest))
    return sorted_array


# TESTING #

numbers_list = [9, 7, 6, 11, 33, 1, 77, -2, 4]

# print(selection_sort(numbers_list))


# EXERCISE

# Imagine you have a shop and you are selling some kind of items.
# You want to know which items bring you the most profit nad you want it sorted from least to most purchased


class ShopItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __lt__(self, other):  # overloading < operator; first time doing this in Python
        return self.quantity < other.quantity

    def __repr__(self):  # built-in function used to compute the "official" string reputation of an object
        return str(self)

    def __str__(self):
        return f"{self.name}: {self.quantity}"


s1 = ShopItem("Orange Juice", 54)
s2 = ShopItem("Chocolate Bars", 22)
s3 = ShopItem("Red Bull", 77)
s4 = ShopItem("Monster Energy", 14)

shop_items = [s1, s2, s3, s4]


print(selection_sort(shop_items))













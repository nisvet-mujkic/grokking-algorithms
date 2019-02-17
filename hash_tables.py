# THEORY
# We want to retrieve item in time of O(1) no matter how big the list is

# Hash function => you pass a string to this function and you get back a number.
# speaking correctly is maps string to a number (index in a array)
# it stores an item in a array at some index and later you use that index to retrieve that same item
# HASH TABLE = hash function + array

# aka hash maps, maps, dictionaries, associative arrays

# python has this built-in, its called dictionaries

book = dict()
# book = {} shorther way of writing line 13
book["apple"] = 1.1
book["orange"] = 2.6

print(book["orange"])

# hash table is build from the key and the value, by using the key we can access the value it holds

book["apple"] = 3

print(book["apple"])


# Practice, some kind of voting machine

voting_machine = {}


def has_voted(name):
    if voting_machine.get(name):
        print(f"{name} has already given his vote.")
    else:
        voting_machine[name] = True
        print(f"{name} has successfully voted.")


has_voted("Nisvet")
has_voted("Faruk")
has_voted("Omer")
has_voted("Nisvet")

print(voting_machine)

# collision => when two or more keys get the same slot to assign their value
# solution: if this happen you can start a linked list on that slot

# average case for insert, delete and search with hash tables is O(1) - constant time
# but the worst case is O(n)

# hash tables are really good and really fast if you have an average case
# but really bad if you have the worst case
# you can have avg case if you avoid collision, and you can avoid collision by:
# having a low load factor ( number_of_items_in_hash_table / total_number_of_slots )
# having a good hashing function

# if load factor is equal to 1 that means that hash table if full, if it is greater than 1 that
# means that hash table has no space left for storing the elements, when this happens you usually need
# to do the resizing (rule of thumb: make hash table two times bigger) and place old elements in new hash table



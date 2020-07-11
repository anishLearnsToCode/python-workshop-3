"""
List / Array
Iterable
"""

numbers = []
print(type(numbers))

# adding elements
# append adds at the last index (value)
numbers.append(10)
numbers.append(45)
print(numbers)

# insert (index, value)
numbers.insert(0, 45)
print(numbers)

# remoing an element
# pop (no arg) --> removes from last index
# remove(value)
# del keyword removes variable

# Sorting a list
# list_name.sort()

# splicing
# list[start : stop : step]
# by default start = 0, stop = len(list), step = 1

# reversing a list
# list[::-1]

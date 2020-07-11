"""
For Loops
for var in iterable_object:
    code
    code
"""

for number in range(10, -1, -2):
    print(number)

n = int(input())
acc = 1
for number in range(1, n + 1):
    acc *= number
print(acc)

for character in 'banana':
    print(character)

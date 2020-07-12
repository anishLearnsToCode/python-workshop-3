"""
Lists / Arrays
f : Integer --> Anything
    index --> value
    (unique) --> (not unique)

Dictionary / HashMap / HashTable / Map
Mutable
not immutable
f : Anything --> Anything
    key --> value
    (unique) --> (not unique)
"""

words = {
    'i': 100,
    'am': 50,
    'batman': 2
}

print(type(words))
print(words)

val = words['am']
print(val)
print(type(val))

print(words.get('i'))

print(words)
words['i'] = 200
print(words)

words['ball'] = 5
print(words)
words['ball'] = 80
print(words)

del words['ball']
print(words)

# del words
# print(words)

keys = words.keys()
print(type(keys))
print(keys, end='\n\n')

values = words.values()
print(type(values))
print(values, end='\n\n')

items = words.items()
print(type(items))
print(items)

for key in words.keys():
    print(key)

s = 0
for value in words.values():
    s += value
print(s)

for item in words.items():
    key = item[0]
    value = item[1]
    print('key: ' + str(key) + ' value: ' + str(value))

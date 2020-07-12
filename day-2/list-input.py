# string = input()
# print(type(string))
# print(string)
#
# string = string.split(' ')
# print(string)
#
# for index in range(len(string)):
#     string[index] = int(string[index])
#
# print(string)

"""
Map Function
(function, iterable)
"""
numbers = list(map(float, input().split(' ')))
val2 = [int(number) for number in input().split(' ')]
print(numbers)
print(val2)

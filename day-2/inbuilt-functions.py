def max(numbers):
    result = -float("inf")
    for number in numbers:
        if number > result:
            result = number
    return result


def min(numbers):
    minimum = float('inf')
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


def abs(number):
    return number if number > 0 else -number


def all(iterable):
    for element in iterable:
        if not bool(element):
            return False
    return True


# print(max([1, 2, 3, 4, 10.45]))
# print(min([-1, -2, -3, -100, 45, -67]))
# print(abs(-5))
# print(abs(5))
# print(all([0, 19]))
# print(all([]))
# print(all('hello'))
# print(all(['hello', 'world', 90]))


def my_any(iterable):
    return True if len(iterable) == 0 else any(iterable)


print(my_any([]))
print(any([]))

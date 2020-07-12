"""
Functions

def function_name(argument1, argument2, argument3, ...):
    code
    return val1, val2, val3 ...  (not compulsory)

having arguments is also not compulsory
"""


def hello():
    print('hello')


def helloWorld(name):
    print('hello ' + name)


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def permutation(n, r): # nPr = n! / (n - r)!
    return factorial(n) // factorial(n - r)


def combination(n, r): # nCr n! / r! * (n - r)! --> nPr / r!
    return permutation(n, r) // factorial(r)


# a = 10
# hello()
# hello()
# hello()
# helloWorld('john doe')
# helloWorld('anish')
# print(factorial(0))
# print(factorial(4))
# print(factorial(5))
# val = factorial(10)
# print(val + 78)
print(combination(4, 0))
print(combination(4, 1))
print(combination(4, 2))
print(combination(4, 3))
print(combination(4, 4))

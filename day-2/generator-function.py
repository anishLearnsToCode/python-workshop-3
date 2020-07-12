"""
Generator Functions / List Comprehension
{x | x is in between 1 and 10}
{ x^2 | for all x 1 <= x <= 10 }
{1, 4, 9, 16, 25 ...}
{x^2 | for all x (1, 10)}
"""

squares = [x for x in range(0, 20, 2) if x % 3 == 0]
print(squares)

# numbers = []
# for x in range(1, 11):
#     numbers.append(x ** 2)
# print(numbers)

"""
Ternary Statement
val1 if condition else val2
if condition is true --> val1 otherwise --> val2
"""

number = int(input())

if number % 2 == 0:
    print('even')
else:
    print('odd')

print('even' if number % 2 == 0 else 'odd')

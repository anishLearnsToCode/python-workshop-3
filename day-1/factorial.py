"""
Factorial
N! = 1 * 2 * 3 * ... * N
N! = N * (N-1)!
0! = 1
"""

n = int(input())

acc = 1
i = 1
while i <= n:
    acc *= i        # acc = acc * i
    i += 1          # i = i + 1

print(acc)

n = int(input())
acc = 1
for number in range(1, n + 1):
    acc *= number
print(acc)

"""
N
1 + 2 + 3 + 4 + ... + N
N (N + 1) / 2
"""

n = int(input())
acc = 0
i = 1
while i <= n:
    acc += i
    i += 1

print(acc)

n = int(input())
acc = 1
for number in range(1, n + 1):
    acc += number
print(acc)

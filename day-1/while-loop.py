"""
While loop

while condition:
    code
    code

condition check --> if true --> code --> condition --> if true --> code --> condition --> if true --> code --> condition
    --> if false --> exit loop
"""

"""
Operation synatx
i = i + 1 --> i += 1
i = i * number --> i *= number
divident = divident / divisor --> divident /= divisor
var = var [operation] var2 --> var [operation]= var2
num = num % 5 --> num %= 5
"""

i = 0
while i < 5:
    print('hello world  : ' + str(i))
    i += 1      # i is being updated i <-- i + 1

print('outside loop')

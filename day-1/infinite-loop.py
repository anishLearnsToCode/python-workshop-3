# i = 1
# while True:
#     print('hello world : ' + str(i))
#     i += 1

hello = 'hello'
iterable = hello.__iter__()
print(type(iterable))

# print(iterable.__next__())
# print(iterable.__next__())
# print(iterable.__next__())
# print(iterable.__next__())
# print(iterable.__next__())
# print(iterable.__next__())

iterable = hello.__iter__()
while True:
    try:
        var = iterable.__next__()
        print(var)
    except:
        # print("An exception occurred")
        break

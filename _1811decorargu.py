# import time

# def totaltime(fun):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         print(args,kwargs)
#         fun(*args,*kwargs)
#         end = time.time()
#         print("total",end - start)
        
#     return wrapper

# @totaltime
# def add(a,b):
#     print(a+b)

# add(4,7)


# def infinite():
#     i = 1
#     while True:
#         yield i
#         i += 1

# b = infinite()
# print(b)

# for i in b:
#     print(i)


import sys

a = []

for i in range(1,10000001):
    a.append(i)

def millions():
    for i in range(1,10000000001):
        yield i
        yield i

b = millions()

print(sys.getsizeof(a))
print(sys.getsizeof(b))


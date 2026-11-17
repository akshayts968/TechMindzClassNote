# # # decorators

# def saymyname(myname):  #stub
#     def wrapper():

#         print("say my name")
#         myname()
#         print("you are right")
#         return 5
#     return wrapper

# @saymyname
# def myname():
#     print("mohan")

# val = myname()
# print(val)

import time

def totaltime(fun):
    def wrapper():
        start = time.time()
        fun()
        end = time.time()
        print("total",end - start)
        
    return wrapper

@totaltime
def myname():
    print("das")

myname()
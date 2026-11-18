# 18/11/2026
#

# def add(*args):  # recieves the data as tuple
#     print(args)

# add(5,2,6,2,6,2,6,"l")
# 

# def fullname(*args,**kwargs):
#     print(args,kwargs)


# fullname(1,5,5,5,5,8,4,88,fname="sachin",mname = "ramesh",lname = "tendulkar",sports="cricket")


def fullname(*args,**kwargs):
    print(args,kwargs)
    # print(f"{kwargs['fname']} {kwargs['mname']} {kwargs['lname']}")

fullname(1,5,5,5,5,8,4,88,fname="sachin",mname = "ramesh",lname = "ten",sports="cricket")


def fullname(*args,**kwargs):
    # print(len(argks),len(kwargs))
    # print(f"{kwargs['fname']} {kwargs['mname']} {kwargs['lname']}")
    print(args,kwargs)
    sum = 0
    for i in args:
        sum+= i

fullname(1,5,5,5,5,8,4,88,fname="sachin",mname = "ramesh",lname = "ten",sports="cricket")

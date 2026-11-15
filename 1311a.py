# 13/11/2026

# lamda function
# recursion
# variable scope


# Lamda


# x = lambda n : n**2
# print(x(2))

# add3 = lambda a,b,c : a+b+c
# print(add3(4,5,6))


# product of 3 number

# prod3 = lambda a,b,c : a*b*c
# print(prod3(5,2,3))



# Area of triangle
# area_triangle = lambda a,b : 0.5*a*b
# print(area_triangle(5,6))



# Perimeter of a circle
# peri_circle = lambda r : 2*3.14*r
# print(peri_circle(5))


# Square root of a number

# squareroot = lambda x : x ** 0.5
# print(squareroot(2061))


# Average of 5 number

# avg5 = lambda a,b,c,d,e : (a+b+c+d+e)/5

# print(avg5(12,55,6,2,3))


# Fullname of a person (fname mname lname)
# fullname = lambda fn,mn,ln: fn + " " + mn+ " " + ln
# print(fullname("mohan","das","kumar"))


# Check if a person is eligible to vote or not




# votecheck = lambda age : age >= 18 # or "InE" 
# print(votecheck(2))






# votecheck = lambda age : "Eligible" if age >= 18 else "Not Eligible"
# print(votecheck(19))






# age = 115
# print("Eligible") if age >=18 else print("Ineligible") if_else simple






# val  = votecheck(17)
# if val:
#     print("Eligible")
# else:
#     print("Not eligible")



# Recursion



# def counttozero(n):
#     print(n)
#     if n == 0:
#         return
#     return counttozero(n - 1)

# counttozero(10)

# Sum of n number using recursion

# def sum(n,val):
#     if n == 0:
#         return val
#     val += n
#     return sum(n-1,val)

# val = 0
# print(sum(10,val))


# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)

# print(sum(10))




# Factorial of a number using recursion


# def fact(n):
#     if n == 1:
#         return n
#     return n * fact(n-1)

# print(fact(5))



# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# print(fact(5))


# Find all prime number between an interval HW


# Scope of a variable

# Scope - area in which it is recognised

# name = "mohan"
# def myname():
#     name="das"
#     print(name)
#     def nickname():
#         name="gouri"
#         print(name)
#     nickname()

# myname()
# print(name)

# # # Output

# # das
# # gouri
# # mohan





# name = "mohan"
# def myname():
#     name="das"
#     print(name)
#     def nickname():
#         print(name)
#     nickname()

# myname()
# print(name)

# # Output

# # das
# # das
# # mohan







name = "mohan"
def myname():
    print(name)
    def nickname():
        print(name)
    nickname()

myname()
print(name)
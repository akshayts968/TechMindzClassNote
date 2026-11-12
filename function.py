# 12/11/2026

# Function

# functions are block of code which executed when it is called


# def functionname(<parameter>):
#     code to be executed

# def greet():
#     print("Hello good morning")


# greet() # Calling a function
# greet()
# greet()
# greet()

# argument

# values to be passed to a function

# def addz(a,b):
    # print(a+b)
# addz(1,2)

# parameter  value get in function
# arguments value given in function call

# def square(a):
#     print(a*a)

# square(5)

# def multiplyfour(a,b,c,d):
#     print(a*b*c*d)

# multiplyfour(10,1,10,2)





# Positional argument 
# Keyword argument


# def addz(a,b):
#     print(a+b)

# addz(5,2) # Positional argument
# addz(b = 2, a = 5) # Keyword argument


# def addz(a = 0,b = 0): # Default value
#     print(a+b)

# addz(4)


# factorial of a number using function



# def fact(a):
#     factval = 1
#     for i in range(1,a+1):
#         factval *= i
#     print(factval)


# fact(7)


# def addz(a,b):
#     return (a + b)


# def subz(a,b):
#     return (a - b)

# def multiply(a,b):
#     return (a*b)

# def div(a,b):
#     return (a/b)


# def main():
#     count = 0
#     check = True
#     while(check):
#         if  count == 0:
#             a = int(input("Enter first value: "))
#             count = 1
#         op = input("Operation: ")
#         if op not in "+-*/":
#             break
#         b = int(input("Enter 2nd value: "))
        
#         if op == "+":
#             a = addz(a,b)
#             print(a)
#         elif op == "-":
#             a = subz(a,b)
#             print(a)
#         elif op == "*":
#             a = multiply(a,b)
#             print(a)
#         elif op == "/":
#             a = div(a,b)
#             print(a)
    


def addz(a,b):
    return a + b


def subz(a,b):
    return a - b

def multiply(a,b):
    return a*b

def div(a,b):
    return a/b


def main():
    val = 0
    check = True
    while(check):
        
        a = int(input("Enter first value: "))
        b = int(input("Enter 2nd value: "))
        op = int(input("Enter operation \n1.Add: \n2.Sub: \n3.Mul: \n4.Div: \n5.Exit: \n"))
        if op == 1:
            val = addz(a,b)
            print(val)
        elif op == 2:
            val = subz(a,b)
            print(val)
        elif op == 3:
            val = multiply(a,b)
            print(val)
        elif op == 4:
            val = div(a,b)
            print(val)
        elif op == 5:
            print("Program Ended")
            break
        else:
            print("Invalid")
            break


main()
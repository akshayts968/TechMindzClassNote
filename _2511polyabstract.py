# 25/11/2026

# Polymorphism
# Operator OverLoading




# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2

#     def __add__(self, otr):
#         t1 = self.m1 * self.m2
#         t2 = otr.m1 * otr.m2
#         return {t1,t2}


# s1 = Student(10,5)
# s2 = Student(8,4)
# print(s1 + s2)





# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2

#     def __add__(self, otr):
#         t1 = self.m1 + otr.m1
#         t2 = self.m2 + otr.m2
#         return f"Add Value {t1} {t2}"
#     def __sub__(self, otr):
#         t1 = self.m1 - otr.m1
#         t2 = self.m2 - otr.m2
#         return f"Sub Value {t1} {t2}"

#     def __mul__(self, otr):
#         t1 = self.m1 * otr.m1
#         t2 = self.m2 * otr.m2
#         return f"Mul Value {t1} {t2}"

#     def __truediv__(self, otr):
#         t1 = otr.m1 / self.m1
#         t2 = otr.m2 / self.m2
#         return f"True Div Value {t1} {t2}"

#     def __gt__(self, otr):
#         t1 = self.m1 > otr.m1
#         t2 = self.m2 > otr.m2
#         return f"Greater Than Value {t1} {t2}"

# s1 = Student(10,5)
# s2 = Student(8,4)
# print(s1 + s2)
# print(s1 - s2)
# print(s1 * s2)
# print(s1 // s2)
# print(s1 > s2)


# # print(int.__truediv__(5,2)) # 2.5

# # method overloading

# class A:
#     def __init__(self):
#         pass
#     def hello(self,a):    # override by 3rd hello
#         print(a)
#     def hello(self,a,b):    # override by 3rd hello
#             print(a+b)
#     def hello(self,a,b,c):
#             print(a+b+c)


# a = A()

# a.hello(2,5,6)
# a.hello(2)  # Error as hello method override as variable reassign
# a.hello(2,3)    # Error as hello method override as variable reassign

# Overloading with *args

# class A:
#     def __init__(self):
#         pass
#     def hello(self,*args):    
#         print(args)


# a = A()
# a.hello(2,5,6)
# a.hello(2)  
# a.hello(2,3)





# # Method overriding



# class A:
#     def __init__(self):
#         pass
#     def hello(self):  
#         print("A says hello")


# class B(A):
#     def __init__(self):
#         pass
#     def hello(self):   
#         print("B says hello")


# b = B()
# b.hello()
# c = B
# c.hello(1)  without () the obj can pass as self






# Abstarct

from abc import ABC,abstractmethod


# class Animal(ABC):
#     def __init__(self):
#         pass

#     @abstractmethod
#     def make_sound(self):
#         print("Animal make sound")



# class Dog(Animal):
#     def __init__(self):
#         pass

#     def make_sound(self):
#         print("Woff")


# d = Dog()
# d.make_sound()



class Payment(ABC):
    def __init__(self):
        pass
    @abstractmethod    
    def pay(self):
        print("payment done")

class Upi(Payment):
    
    def __init__(self):
        pass

    def pay(self):
        print("payed by upi")



class Card(Payment):
    def __init__(self):
        pass

    def pay(self):
        print("payed by card")




a = Card()
a.pay()

a = Upi()
a.pay()
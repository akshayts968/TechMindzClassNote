# 23/11/2026

# OOPS



# attributes  -- variables
# behaviours methods -- function

# class
# blueprint


# class Car:
#     def start(): #methods
#         print("Car has started")

#     def stop():
#         print("Car stopped")

# car1 = Car
# car2 = Car
# car3 = Car


# car1.start()


# car2.stop()




# class Car:
#     def __init__(self):  # Initialize an object
#         self.name = "swift"
#         self.color = "yellow"

#     def start(self): #methods
#         print("Car has started")

#     def stop(self):
#         print("Car stopped")

# car1 = Car()
# print(car1.name)
# print(car1.color)


# car2 = Car()
# print(car2.name)
# print(car2.color)



# # car1.__init__() 



# class Car:
#     def __init__(self,name,color,year):  # Initialize an object
#         self.name = name
#         self.color = color
#         self.year = year
#     def start(self): #methods
#         print(f"{self.name} has started")

#     def stop(self):
#         print(f"{self.name} stopped")
#     def check(self,otr):
#         print(self.name)
#         print(otr.name)
#         print(self.year < otr.year)

# car1 = Car("Swift","Yellow",2018)
# car2 = Car("City","Red",2016)

# car1.check(car2)


# Create a Student class with 6 attribute

# name 
# m1
# m2
# m3
# m4
# m5

# # 3 Methods
# sumofmarks()
# avgofmarks()
# display()

# class Student:
#     def __init__(self,name,m1,m2,m3,m4,m5):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#         self.m5 = m5
#         # self.sum = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
#     def sum_of_marks(self):
#         sum = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
#         print(f"{self.name} has a Total of {sum} out of 250")
#     def average_of_marks(self):
#             sum = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
#             avg = sum / 5
#             print(f"{self.name} has an Average of {avg}")

#     def display(self):
#          print(f"Student name : {self.name}")
#          print(f"M1 : {self.m1}\nM2 : {self.m2}\nM3 : {self.m3}\nM4 : {self.m4}\nM5 : {self.m5}")
#          self.sum_of_marks()
#          self.average_of_marks()
#         #  print(self.sum)
# E = Student("Eashwar",45,50,38,40,36)
# # E.sum_of_marks()
# # E.average_of_marks()
# E.display()



# A = Student("Akshay",45,46,38,40,36)
# # E.sum_of_marks()
# # E.average_of_marks()
# A.display()




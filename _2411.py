# 24/11/2026

# Inheritance



# single level
# multi level
# multiple


# # single level

# class Person1: # Parent class / Super class
#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")

#     def write(self):
#         print("Person can write")

# class Person2(Person1): # Child class
#     def __init__(self):
#         pass

#     def run(self):
#         print("person can run")

#     def jump(self):
#         print("Person can jump")

#     def speak(self):
#             print("Person 2 can speak")


# p2 = Person2()
# p2.write()

# Multi level

# class Person3(Person2): 
#     def __init__(self):
#         pass
#     def fly(self):
#         print("person can fly")

#     def swim(self):
#         print("Person can swim")

#     def speak(self):
#             print("Person 3 can speak")
#             super().speak()

# class Person4(Person3): 
#     def __init__(self):
#         pass

#     def sleep(self):
#         print("person can sleep")

#     def eat(self):
#         print("Person can eat")

#     def speak(self):
#         print("Person 4 can speak")
#         super().speak()



# # p4 = Person4()
# # p4.speak()










# Multiple Inheritance



class Person1: # Parent class / Super class
    def __init__(self):
        pass
    def read(self):
        print("person can read")

    def write(self):
        print("Person can write")

class Person2: # Child class
    def __init__(self):
        pass

    def run(self):
        print("person can run")

    def jump(self):
        print("Person can jump")

    def speak(self):
            print("Person 2 can speak")



class Person3: 
    def __init__(self):
        pass
    def fly(self):
        print("person can fly")

    def swim(self):
        print("Person can swim")

    def speak(self):
            print("Person 3 can speak")
            # super().speak()

class Person4(Person2,Person1,Person3): 
    def __init__(self):
        pass

    def sleep(self):
        print("person can sleep")

    def eat(self):
        print("Person can eat")

    def speak(self):
        print("Person 4 can speak")
        super().speak()  # how to use Person1 and Person3


person = Person4()
person.speak()




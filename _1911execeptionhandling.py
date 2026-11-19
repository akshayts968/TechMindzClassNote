# 19/11/2026
# Exception


# try:
#     a = 5
#     b = 0
#     print(a/b)
# except Exception as e:
#     print("An error occured",e)

# print("hari")



# try:
#     a = int(input("Enter a num "))
#     b = 5
#     print(a/b)
# except ZeroDivisionError:
#     print("Cant divide by Zero")
# except ValueError:
#     print("Check Values")
# except TypeError:
#     print("Check Types")
# finally:
#     print("This will always execute")

# print("hari")

class Myerror(Exception):
    pass


age = 17
if age < 18:
    raise(Myerror("Age should be greater than 18"))
    #raise(ValueError("Age should be greater than 18"))
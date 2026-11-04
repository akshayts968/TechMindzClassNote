

# # Inverted Right triangle
# for i in range(5):
#     for j in range(6-i-1,0,-1):
#         print("*",end="")
#     print()

#      *
#     ***
#    *****
#   *******

# Inverted Pyramid

# for i in range(5,0,-1):
#     for k in range(i,0,-1):
#         print("",end=" ")
#     for j in range(1,6,2):
#         print(j,end="")
#     print()


# Pyramid

# for j in range(1,6,2):
#     for k in range(6-j,0,-2):
#         print(" ",end="")
#     for i in range(0,j):
#         print("*",end="")
#     print()

# # Output

#    *
#   ***
#  *****

# Inverted Pyramid


# # for j in range(5,0,-2):
#     for k in range(5-j,0,-2):
#         print(" ",end="")
#     for i in range(j,0,-1):
#         print("*",end="")
#     print()

# Output
# *****
#  ***
#   *


# # Diamond

# for j in range(1,6,2):
#     for k in range(6-j,0,-2):
#         print(" ",end="")
#     for i in range(0,j):
#         print("*",end="")
#     print()
# for j in range(5,0,-2):
#     for k in range(6-j,0,-2):
#         print(" ",end="")
#     for i in range(j,0,-1):
#         print("*",end="")
#     print()

# #  Output

#    *
#   ***
#  *****
#  *****
#   ***
#    *


# # Hollow Square

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4:
#             print("*",end="")
#         elif (j == 0) or (j == 4):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

#  Output

# *****
# *   *
# *   *
# *   *
# *****
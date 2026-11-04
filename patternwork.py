

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




# num = 14

# for j in range(1,num,2):
#     for k in range(num-j,0,-2):
#         print(" ",end="")
#     for i in range(0,j):
#         print("*",end="")
#     print()

# # Output

#    *
#   ***
#  *****




# Inverted Pyramid




# num = 9
# for j in range(num,0,-2):
#     for k in range(num-j,0,-2):
#         print(" ",end="")
#     for i in range(j,0,-1):
#         print("*",end="")
#     print()

# Output
# *****
#  ***
#   *


# # Diamond



# num = 9
# for j in range(1,num + 1,2):
#     for k in range(num + 1 - j,0,-2):
#         print(" ",end="")
#     for i in range(0,j):
#         print("*",end="")
#     print()
# for j in range(num,0,-2):
#     for k in range(num + 1 - j,0,-2):
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


# # Hollow Right Triangle


# num = 8
# for i in range(num):
#     for j in range(i+1):
#         if j == 0 or i == num - 1:
#             print("*",end="")
#         elif j == i:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


# #  Output
# # *
# # **
# # * *
# # *  *
# # *   *
# # *    *
# # *     *
# # ********



# # Palindrome Number Pyramid

# #     1
# #    121
# #   12321
# #  1234321
# # 123454321


# num = 9

# for i in range(num):
#     for j in range(num-i,0,-1):
#         print(end=" ")
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range(i+1,0,-1):
#         print(l,end="")
#     print()


# #  Output


# #          1
# #         121
# #        12321
# #       1234321
# #      123454321
# #     12345654321
# #    1234567654321
# #   123456787654321
# #  12345678987654321


# # ButterFly


# num = 7

# for i in range(num):
#     for j in range(i+1):
#         print("*",end="")
#     con = num - i - 1
#     for k in range(2*con):
#         print(end=" ")
#     for j in range(i+1):
#             print("*",end="")
#     print()

# for i in range(num-1,0,-1):
#     for j in range(i):
#         print("*",end="")
#     con = num - i
#     for k in range(2*con):
#         print(end=" ")
#     for j in range(i):
#             print("*",end="")
#     print()

# #  Output

# # *            *
# # **          **
# # ***        ***
# # ****      ****
# # *****    *****
# # ******  ******
# # **************
# # ******  ******
# # *****    *****
# # ****      ****
# # ***        ***
# # **          **
# # *            *




# # X

# # *    *
# #  *  *
# #   *
# #  *  *
# # *    *

# num = 7
# for i in range(num):
#     for j in range(num):
#         if i == j:
#             print(end="*")
#         elif i + j + 1 == num:
#             print(end="*")
#         else:
#             print(end=" ")
#     print() 
# #  Output

# # *     *
# #  *   * 
# #   * *  
# #    *   
# #   * *  
# #  *   * 
# # *     *
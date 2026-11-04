# 04/11/2026 Nested Loop and Continue Break
# Day 7


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# Output

# *
# **
# ***
# ****
# *****



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# Output

# 1
# 22
# 333
# 4444
# 55555


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# Output

# 1
# 12
# 123
# 1234
# 12345


# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print("*",end="")
#     print()

# Output

# *****
# ****
# ***
# **
# *

# num = 5
# for i in range(num):
#     for k in range(num-i-1):
#         #   print(num-i-1)
#           print(" ",end="")
#     for j in range(i+1):
#            print("*",end=" ")
#     print()

# Output


#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *



# # Chess Board Pattern


# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             print("W",end=" ")
#         else:
#             print("B",end=" ")
#     print()


# Output

# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 



# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()



# Output

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *



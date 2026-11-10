# # Pattern printing

# # matrix
# # row and col


# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or i == 5 or j == 3:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


# # *****
# #   *  
# #   *  
# #   *  
# # *****


# # pass
# # break
# # continue


# a = 5
# if a > 1:
#     pass # Temp

# for i in range(1,11):
#     print(i)
#     if i == 7:
#         break
# print("hari")


# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # hari


for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            print("*")
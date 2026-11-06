# 06/1/2026
# Day 9
# Control statement for iterable


# a = "mohandas"
# b = [11,12,13,14,15]
# c= (9,8,7,6,5,4,3,2,1)


# for i in c:
#     print(i)

# for i in range(0,len(a)):
#     print(i,a[i])


# for i in range(len(b)):
#     print(i,b[i])

# for i in range(len(c)):
#     print(i,c[i])


# # Print vowels and their position from the given string
# # data = "hari"
# data = input("Enter a String ")

# # for i in range(len(data)):
# #     if data[i]=='a' or data[i]=='e' or data[i]=='i' or data[i]=='o' or data[i]=='u':
# #         print(data[i]," at index ",i)



# # Thus is more better than above
# vowel = "aeiou"

# for i in range(len(data)):
#     if data[i] in vowel:
#         print(data[i]," at index ",i)


# # Create a list of 100 number

# arr = []
# # brr = []
# for i in range(1,101):
#     arr.append(i)
#     # brr.insert(0,i)
# # for i in range(100):
# #     arr.append(i+1)
# print(arr)
# # print(brr)



# # Create a list of even and odd numbers

# earr = []
# oarr = []
# for i in range(100):
#     if (i+1) % 2 == 0:
#         earr.append(i+1)
#     else:
#         oarr.append(i+1)

# print(earr,oarr)



# # Remove Duplicates from the list


# b = [1,2,3,4,5,3,2,1,1,1,1,2,2,2,3,3,4,4,5,6]

# a = []
# for i in range(len(b)):
#     if b[i] not in a:
#         a.append(b[i])
# b = a
# print(b)


# data = "abcdefghijkl"
# rev =""
# length = len(data)
# for i in range(len(data)):
#     rev=rev+data[length-1-i]

# print(rev)


# Reverse a List

# b = [10,11,12,13,14]
# a = []
# length = len(b)
# for i in range(length):
#     print(b[length-i-1])
#     a.append(b[length-i-1])
# print(a)






# # Check if a number is Prime: 

# size = int(input("Enter the count: "))
# arr = []
# for i in range(size):
#     data = int(input("Enter the number: "))
#     arr.append(data)
# print(arr)
# for i in range(len(arr)):
#     num = arr[i]
#     check = True
#     i = 2
#     length = num - 1
#     while(check and i < num):
#         if num % i == 0:
#             check = False
#         i = i+1

#     if check:
#         print(num,"It is Prime")
#     else:
#         print(num,"It is not Prime")


    
# num = int(input("Enter a Num: "))
# check = True
# if num == 1:
#     check = False
# else:
#     i = 2
#     length = num - 1
#     while(check and i < num):
#         if num % i == 0:
#             check = False
#         i = i+1

# if check:
#     print(num,"It is Prime")
# else:
#     print(num,"It is not Prime")
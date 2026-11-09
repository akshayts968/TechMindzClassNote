# 09/11/2026
# Day 10
# # Convert a List to  2 Equal list

# c = [11,12,13,14,15,16,17,18,19,20,21]

# a = []
# b = []

# length = len(c)
# print(length)
# mid  = length // 2
# if length % 2 == 1:
#     mid = mid + 1
# for i in range(length):
#     if i < mid:
#         a.append(c[i])
#     else:
#         b.append(c[i])

# print(a,b)
# # print(len(a),len(b))
# # print(length/2,length//2,int(length/2))


# # Find largest and smallest from the list

# z = [11,-1,0,-88,999,300,-100,4,2,600]

# largest = z[0]
# smallest = z[0]

# for i in z:
#     if i > largest:
#         largest = i
#     elif i < smallest:
#         smallest = i

# print(largest,smallest)


# # # Sort the list

# z = [11,-1,0,-88,999,300,-100,4,2,600]
# for i in range(len(z)):
#     temp = z[i]
#     for j in range(1,len(z)):
#         if temp > z[j]:
#             0
#         print(z)

# print(z)




# #Split()

# data = "hello my name is mohan "
# rmwhite = ""
# #1 remove whitespace from the given string

# for i in data:
#     if not i == " ":
#         rmwhite = rmwhite + i
# print(rmwhite)


# #2. create a list of words from the list

# words = []
# temp=""
# for i in range(len(data)):
#     if data[i] == " " and len(temp):
#         words.append(temp)
#         temp = ""
#     elif (i == len(data) - 1) and len(temp):
#         temp = temp + data[i]
#         words.append(temp)
#     else:
#         temp = temp + data[i]

# # print(data[len(data) - 1])
# print(words)

# # Admin@CarnivalTMZ

# bills = [5,5,5,10,20]
# remain = []
# check = True
# for i in range(len(bills)):
#     if bills[i] == 5:
#         remain.append(5)
#     elif bills[i] == 10:
#         temp = 10
#         for j in range(remain):
#             if remain[j] == 5:
#                 temp-=remain[j]



# # Split

# data = "hello my name is mohan "
# z = data.split()
# print(z)  # ['hello', 'my', 'name', 'is', 'mohan']
# z = data.split("m")
# print(z)  # ['hello ', 'y na', 'e is ', 'ohan ']


# #Join

# b = " ".join(z) #join with space

# print(b) #hello  y na e is  ohan 


# b = "+".join(z) #join with +

# print(b)  # hello +y na+e is +ohan 


# Count Divisor

l = 2
r = 8
k = 2
count = 0
for i in range(l,r+1):
    if i % k == 0:
        count += 1

print(count)

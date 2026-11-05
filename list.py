# 05/11/2026


# Day 8

# Lists
# Collection Of data

# []

# students = ["mohan","das","angel","afsal","rajisree","gowri"]
# print(students)
# print(type(students))


# # Properties

# # Can have any elements at any size

# a = [1,1.1,"mohan",[1,2,3,4],1,1]

# print(a)


# # List are ordered

# a = [1,2,3,4]
# b = [4,3,2,1]

# print(a == b)

# a = [1,1.1,'''mohan''',[1,2,3,4],1,1]
# print(a)


# Indexing


# List are indexed
# Start at zero
# a = [11,12,13,14,15]
# print(a[4]) --> 15

# name = "mohandas"
# print(name[5]) --> d


# # [startindex:stopindex:step]
# b = [11,12,13,14,15,16,17,18,19,20]
# print(b[1:9:2])  #[12, 14, 16, 18]

#   0 1 2 3 4 5 6 7
# a= "mohandas"
# print(a[4:]) # ndas
# print(a[:6]) # mohand
# print(a[::-1]) # sadnahom



# print(a[8::-1])  # sadnahom
# print(a[7::-1])  # sadnahom
# print(a[10::-1])  # sadnahom
# print(a[100::-1])  # sadnahom can be any number but print from end index 7 in this case


# # List can be nested

# a = [11,12,[100,200,300,["mohan",["hari"],"das"],500],14,15]
# b = a[2] # [100,200,300,["mohan",["hari"],"das"],500]
# print(b[3]) # ['mohan', ['hari'], 'das']
# print(a[2][3][1][0]) # hari
# # print(a[2][3][1][0][::-1]) # irah

# List are mutable

# s = [11,12,13,14,15]
# s[0] = "mohan" 
# print(s)  # ['mohan', 12, 13, 14, 15]
 

# s = "mohandas"
# print(s[18::-1])  # sadnahom

# s= s+s
# print(s)  # mohandasmohandas



# add


# append(item)


# adds an element to the end of the list


# a = [11,12,13,14,15,16,17,18,19,20]
# a.append(100)   # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100]
# a.append([100])  #[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, [100]]
# print(a)

# extend add an iterable to the list



# extend(iterable)


# a = [11,12,13,14]
# # a.extend([4,5,6]) # [11, 12, 13, 14, 4, 5, 6]
# # a.extend([4,5,6,[5,2]]) # [11, 12, 13, 14, 4, 5, 6, [5, 2]]
# a.extend("das") # [11, 12, 13, 14, 'd', 'a', 's']
# print(a)

# insert(index,item) add element at that index

# a = [11,12,13]
# a.insert(0,15)
# print(a) # [15, 11, 12, 13]


# Delete

#remove(item)

# a = [1,2,3,4,51,2,1,1,2,3]
# a.remove(1)
# print(a)  # [2, 3, 4, 51, 2, 1, 1, 2, 3] remove first occurance of 1


# pop

# pop()  removes last element from the list
# a = [11,12,13,14,15]
# a.pop()   # remove last element in the list
# print(a)  # [11, 12, 13, 14]


#pop(index)
# a = [11,12,13,14,15]
# a.pop(0) # remove element from llst of that index
# print(a) # [12, 13, 14, 15]


# tuple

# collection of data

data = (0,2,3,4,"hi",3.4)
# data[0] = "das" # Error tuple immutable

print(data)
print(type(data))
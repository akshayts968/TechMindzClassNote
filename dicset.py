# 10/11/2026

# Day 11



#  sets
# set are collection of data
# a = {}

# set are unordered
# set un indexed
# does not contain duplicate values
# mutable
# a = {1,3,2,2,5,3,2} --> {1,3,2,5}

# fruits = {'apple','orange','pineapple'}

# for i in  fruits:
#     print(i)


# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}

# print(a.union(b))
# print(a | b)


# print(a.intersection(b))
# print(a & b)

# print(a-b)  #{1, 2, 3}
# print(b-a)  #{8, 9, 7}


# a = a-b  
# print(a)   #{1, 2, 3}
# print(b-a)  # {4, 5, 6, 7, 8, 9}



# Dictionary

# key value pair datatype


# data = {}
# print(type(data)) # <class 'dict'>
# z = {3,4,45,5,6,8,9,90}
# data = {'name':"mohan","age":24,"location":"kochi"}


# print(data)
# print(type(data))


# # has no index

# print(data['name'])

# # dict is mutable

# user_data = {}
# user_data['name'] = 'das'
# user_data['age'] = 24
# user_data['email'] = "das@23.com"
# user_data['phone'] = 2552522
# user_data['location'] = "kochi"
# user_data['name'] = "kumar"
# print(user_data)  # {'name': 'kumar', 'age': 24, 'email': 'das@23.com', 'phone': 2552522, 'location': 'kochi'}





# # restrictions


# # both keys

# # 1. dict key have to be unique

# a = {'name':'kumar','phone':5151,'name':'mohan'}
# print(a) # {'name': 'mohan', 'phone': 5151}

# # 2.key must be immutable type ,cant use list as it is mutable


# # inbilt methods


# a = {'name':'kumar','phone':5151,'name':'mohan','age':24,'location':"kochi"}
# print(a['name'])
# print(a.get('name'))
# print(a.keys())
# print(a.values())
# print(a.items())
# # dict_keys(['name', 'phone'])
# # dict_values(['mohan', 5151])
# # dict_items([('name', 'mohan'), ('phone', 5151)])

# a.pop("phone")   #removes a specific key and value
# a.popitem()     # removes the last key ValueError

# print(a)       # {'name': 'mohan', 'age': 24}

# a = {'name':'kumar','phone':5151,'name':'mohan','age':24,'location':"kochi"}
# print(a['name'])
# print(a.get('name'))
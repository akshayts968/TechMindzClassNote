# 03/11/2026

# For loop

# for i in range(start,stop,step):

# Default Start = 0 and default Step = 1

# range(1,10,1)   -->    start,stop,step   1 to 9            print stop - 1
# range(1,10)     -->    start,stop,step = 1 default
#range(20)        -->    start = 0,stop = 20,step = 1
# range(20,0,-1)  -->    start = 20,stop = 1,step = -1   20 to 1           print stop - (step = -1)



# # Sum of first 10 numbers

# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)




# # Factorial of a Number

# prod = 1
# num = int(input("Enter a num: "))
# for i in range(1,num+1):
#     prod = prod * i
# print(prod)


# # Find sum and average of N numbers


# count = int(input("Enter the count: "))
# sum = 0
# for i in range (count):
#     num = int(input("Enter the num: "))
#     sum = sum + num

# print("Sum: ",sum,"\nAvg: ",sum/count)





# # Check if a Number is amstrong or Not 


# num = int(input("Enter a num: "))
# count = 0
# cpy = num
# while num > 0:
#     count = count + 1
#     num = num // 10

# # print(count)


# sum = 0
# num = cpy
# while num > 0: 
#     digit = num % 10  
#     # prod = 1
#     # for i in range(count):  
#     #     prod = prod * digit
#     sum = sum + digit**count
#     num = num // 10

# if sum == cpy: 
#     print(cpy," it is amstrong")
# else:
#     print(cpy," it is not amstrong")

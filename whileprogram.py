# #Count no of digit

# num = int(input("Enter the number: "))

# count = 0
# while num > 0:
#     count = count + 1
#     num = num // 10

# print(count)


# # Find first and last digit of a number
# num = int(input("Enter the num: "))
# last = num % 10
# first = 0
# while num > 0:  
#     first = num % 10
#     num = num // 10

# print(first,last)

# # Check for palindrome a number

# num = int(input("Enter the num: "))
# rev = 0
# cpy = num

# while num > 0:
#     rev = rev * 10 + num % 10
#     num = num // 10

# if rev == cpy:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")

# # Print N to 1


# num = int(input("Enter the num: "))

# while num > 0:
#     print(num)
#     num = num - 1

# # Product of digit of a number

# num = int(input("Enter a num: "))
# prod = 1
# while num > 0:
#     prod = prod * (num % 10)
#     num = num // 10
# print(prod)


# # Sum of even digit in a number


# num = int(input("Enter the num: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     if digit%2 == 0:
#         sum = sum + digit
#     num = num // 10

# print(sum)

# # Sum of First N odd Number

# num = int(input("Enter the no: "))
# i = 1
# odd = 1
# sum = 0
# while i <= num:
#     sum = sum + odd
#     odd = odd + 2
#     i = i + 1

# print(sum)
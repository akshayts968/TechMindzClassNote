num = int(input("Enter a num: "))
prod = 1
while num > 0:
    prod = prod * (num % 10)
    num = num // 10
print(prod)
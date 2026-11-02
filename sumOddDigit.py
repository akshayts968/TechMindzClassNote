num = int(input("Enter the num: "))
sum = 0
while num > 0:
    digit = num % 10
    if digit%2 == 1:
        sum = sum + digit
    num = num // 10

print(sum)
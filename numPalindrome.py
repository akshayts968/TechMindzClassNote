num = int(input("Enter the num: "))
rev = 0
cpy = num

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

if rev == cpy:
    print("It is palindrome")
else:
    print("It is not palindrome")
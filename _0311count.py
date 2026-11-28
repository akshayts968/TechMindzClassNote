# 03/11/2026 Day 6
# Count the digit in a Number



num = int(input("Enter a num : "))
count = 0
while num > 0:
    count = count + 1
    num = num // 10
print(count)
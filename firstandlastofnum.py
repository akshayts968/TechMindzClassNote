num = int(input("Enter the num: "))
last = -1
first = 0
while num > 0:  
    if last == -1:
        last =  num % 10 
    first = num % 10
    num = num // 10

print(first,last)

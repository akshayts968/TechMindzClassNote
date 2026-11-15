def prime(start,end):
    if start > end:
        return
    check = int(start**0.5 + 1)
    for i in range(2,check):
        if start % i == 0:
            # print(start," ",i)
            return prime(start+1,end)

    print(start," is prime")
    prime(start+1,end)



def main():
    interval = input("Enter interval by space : ")
    interval = interval.split()
    start,end = int(interval[0]),int(interval[1])
    prime(start ,end)
    
    

main()
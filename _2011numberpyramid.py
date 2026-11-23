n = 19
mid = n//2 # 4
for j in range(1,mid + 2):  # 1 2 3 4 5
    sp = mid + 1 - j 
    for k in range(sp):
        print(end=" ")
    for l in range(1,j+1):
        print(l,end="")
    for l in range(j-1,0,-1):
        print(l,end="")
    print()

for i in range(mid,0,-1):
    sp = (mid + 1) - i
    for j in range(sp):
        print(end=" ")
  
    for l in range(1,i+1):
        print(l,end="")
    for l in range(i-1,0,-1):
        print(l,end="")
    print()


# OutPut

#          1
#         121
#        12321
#       1234321
#      123454321
#     12345654321
#    1234567654321
#   123456787654321
#  12345678987654321
# 12345678910987654321
#  12345678987654321
#   123456787654321
#    1234567654321
#     12345654321
#      123454321
#       1234321
#        12321
#         121
#          1
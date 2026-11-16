import random

count1 = random.randint(1,6)
print(f"count is {count1}")
sum1 = 0
for i in range(count1):
    val = random.randint(1,6)
    # print(f"value {val}")
    sum1 += val
    print(f"Sum  is {sum1}")

count2 = random.randint(1,6)
print(f"count is {count2}")
sum2 = 0
for i in range(count2):
    val = random.randint(1,6)
    # print(f"value {val}")
    sum2 += val
    print(f"Sum  is {sum2}")


if sum1 == sum2:
    print("Draw")
elif sum1 > sum2:
    print("Player one Wins")
else:
    print("Player Two Wins")
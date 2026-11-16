import random

# list = ["Rock","Paper","Scissor"]
# while True:
#     print("Rock paper Scissor Game \nchoose value\n1.Rock\n2.Paper\n3.Scissor\n4.Exit")
#     user = int(input("Enter value: "))
#     if user < 4:
#         user = list[user-1]
#         computer = random.choice(list)
#         print(computer,user)
#         if computer == user:
#             print("Draw")
#         elif computer == "Rock" and user == "Paper" or computer == "Paper" and user == "Scissor" or computer == "Scissor" and user == "Rock":
#             print("User Win")
#         elif user == "Rock" and computer == "Paper" or user == "Paper" and computer == "Scissor"  or user == "Scissor" and computer == "Rock":
#             print("Computer Win")
#     elif user == 4:
#         print("Exit")
#         break
#     else:
#         print("Error")

# import random

# list = ["Rock","Paper","Scissor"]
# while True:
#     print("Rock paper Scissor Game \nchoose value\n1.Rock\n2.Paper\n3.Scissor\n4.Exit")
#     user = int(input("Enter value: "))
#     if user < 4:
#         computer = random.randint(1,3)
#         print(list[computer - 1],list[user - 1])
#         if computer == user:
#             print("Draw")
#         elif computer == 1 and user == 2 or computer == 2 and user == 3 or computer == 3 and user == 1:
#             print("User Win")
#         elif user == 1 and computer == 2 or user ==2 and computer == 3  or user == 3 and computer == 1:
#             print("Computer Win")
#     elif user == 4:
#         print("Exit")
#         break
#     else:
#         print("Error")



ch = ["rock","paper","scissor"]

computer = random.choice(ch)
player = ""
while player not in ch:
    player = input("enter your choice rock/paper/scissor---").lower()

print(f"computer choose {computer}")
print(f"player choose {player}")

if player == computer:
    print("Draw!!!!!!")
elif player == "rock":
    if computer == "scissor":
        print("player wins . rock beat scissor")
    else:
        print("computer wins . paper covers rock")
elif player == "scissor":
    if computer == "rock":
        print("computer wins . rock beat scissor")
    else:
        print("player wins . paper covers rock")
elif player == "paper":
    if computer == "rock":
        print("player wins . paper covers rock")
    else:
        print("computer wins . scissor cuts paper")